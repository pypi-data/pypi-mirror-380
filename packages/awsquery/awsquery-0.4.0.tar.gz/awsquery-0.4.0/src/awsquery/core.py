"""Core AWS operations for AWS Query Tool."""

import re
import sys
from typing import Any, Dict, List, Optional, Tuple, Union

import boto3
from botocore.exceptions import ClientError, NoCredentialsError

from .filters import extract_parameter_values, filter_resources
from .utils import convert_parameter_name, debug_print, get_client, normalize_action_name


class CallResult:
    """Track successful responses throughout call chain"""

    def __init__(self) -> None:
        """Initialize CallResult with tracking lists."""
        self.successful_responses: List[Any] = []
        self.final_success: bool = False
        self.last_successful_response: Optional[Any] = None
        self.error_messages: List[str] = []


def execute_with_tracking(service, action, parameters=None, session=None):
    """Execute AWS call with tracking for keys mode"""
    result = CallResult()

    try:
        response = execute_aws_call(service, action, parameters, session)

        # Check if response indicates a validation error (for multi-level calls)
        if isinstance(response, dict) and "validation_error" in response:
            result.final_success = False
            result.error_messages.append(f"Validation error: {response['validation_error']}")
        else:
            # Successful response
            result.successful_responses.append(response)
            result.last_successful_response = response
            result.final_success = True
            debug_print(f"Tracking: Successful call to {service}.{action}")  # pragma: no mutate
    except Exception as e:
        result.final_success = False
        result.error_messages.append(f"Call failed: {str(e)}")
        debug_print(f"Tracking: Failed call to {service}.{action}: {e}")  # pragma: no mutate

    return result


def execute_aws_call(service, action, parameters=None, session=None):
    """Execute AWS API call with pagination support and optional parameters"""
    normalized_action = normalize_action_name(action)

    try:
        client = get_client(service, session)
        operation = getattr(client, normalized_action, None)

        if not operation:
            operation = getattr(client, action, None)
            if not operation:
                raise ValueError(
                    f"Action {action} (normalized: {normalized_action}) "
                    f"not available for service {service}"
                )

        call_params = parameters or {}

        # Try pagination first, fall back to direct call
        try:
            paginator = client.get_paginator(normalized_action)
            results = []
            for page in paginator.paginate(**call_params):
                results.append(page)
            return results
        except Exception as e:
            # Check for specific error types
            if "OperationNotPageableError" in str(type(e)):
                debug_print(
                    f"Operation not pageable, falling back to direct call"
                )  # pragma: no mutate
                return [operation(**call_params)]
            elif type(e).__name__ == "ParamValidationError" or (
                isinstance(e, ClientError)
                and hasattr(e, "response")
                and e.response.get("Error", {}).get("Code")  # pylint: disable=no-member
                in ["ValidationException", "ValidationError"]
            ):
                debug_print(
                    f"Validation error during pagination, re-raising: {e}"
                )  # pragma: no mutate
                raise e
            else:
                debug_print(
                    f"Pagination failed ({type(e).__name__}), falling back to direct call"
                )  # pragma: no mutate
                return [operation(**call_params)]

    except NoCredentialsError:
        print("ERROR: AWS credentials not found. Configure credentials first.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        if type(e).__name__ == "ParamValidationError":
            error_info = parse_validation_error(e)
            if error_info:
                return {"validation_error": error_info, "original_error": e}
            else:
                print(f"ERROR: Could not parse parameter validation error: {e}", file=sys.stderr)
                sys.exit(1)

        if isinstance(e, ClientError):
            error_info = parse_validation_error(e)
            if error_info:
                return {"validation_error": error_info, "original_error": e}
            else:
                print(f"ERROR: AWS API call failed: {e}", file=sys.stderr)
                sys.exit(1)

        print(f"ERROR: Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


def _execute_multi_level_call_internal(
    service: str,
    action: str,
    resource_filters: List[str],
    value_filters: List[str],
    column_filters: List[str],
    session: Optional[Any] = None,
    hint_function: Optional[str] = None,
    hint_field: Optional[str] = None,
    with_tracking: bool = False,
) -> Union[Tuple[Optional[CallResult], List[Any]], List[Any]]:
    """Unified implementation for multi-level calls with optional tracking"""
    debug_print(f"Starting multi-level call for {service}.{action}")  # pragma: no mutate
    debug_print(
        f"Resource filters: {resource_filters}, "  # pragma: no mutate
        f"Value filters: {value_filters}, Column filters: {column_filters}"  # pragma: no mutate
    )  # pragma: no mutate

    call_result = CallResult() if with_tracking else None

    # First attempt - main call
    response = None
    try:
        response = execute_aws_call(service, action, parameters=None, session=session)

        if isinstance(response, dict) and "validation_error" in response:
            if with_tracking and call_result is not None:
                call_result.error_messages.append(
                    f"Initial call validation error: {response['validation_error']}"
                )
            error_info = response["validation_error"]
            parameter_name = error_info["parameter_name"]
            debug_print(
                f"Validation error - missing parameter: {parameter_name}"
            )  # pragma: no mutate
        else:
            # Initial call succeeded
            if with_tracking and call_result is not None:
                call_result.successful_responses.append(response)
                call_result.last_successful_response = response
                call_result.final_success = True
                debug_print(
                    f"Tracking: Initial call to {service}.{action} succeeded"
                )  # pragma: no mutate

            from .formatters import flatten_response

            resources = flatten_response(response)
            debug_print(f"Final call returned {len(resources)} resources")  # pragma: no mutate

            if value_filters:
                filtered_resources = filter_resources(resources, value_filters)
                debug_print(
                    f"After value filtering: {len(filtered_resources)} resources"
                )  # pragma: no mutate
            else:
                filtered_resources = resources

            return (call_result, filtered_resources) if with_tracking else filtered_resources

    except Exception as e:
        if with_tracking and call_result is not None:
            call_result.error_messages.append(f"Initial call failed: {str(e)}")
        debug_print(f"Initial call failed: {e}")  # pragma: no mutate

    # Multi-level resolution needed
    if response and isinstance(response, dict) and "validation_error" in response:
        error_info = response["validation_error"]
        parameter_name = error_info["parameter_name"]
        debug_print(f"Validation error - missing parameter: {parameter_name}")  # pragma: no mutate

        print(f"Resolving required parameter '{parameter_name}'", file=sys.stderr)

        # Use hint function if provided
        if hint_function:
            hint_normalized = normalize_action_name(hint_function)
            possible_operations = [hint_normalized]
            # Convert hint function to CLI format for display
            from .utils import pascal_to_kebab_case

            hint_function_cli = pascal_to_kebab_case(hint_function)
            print(
                f"Using hint function '{hint_function_cli}' for parameter resolution",
                file=sys.stderr,
            )
        else:
            possible_operations = infer_list_operation(service, parameter_name, action)

        list_response = None
        successful_operation = None

        for operation in possible_operations:
            try:
                debug_print(f"Trying list operation: {operation}")  # pragma: no mutate
                print(f"Calling {operation} to find available resources...", file=sys.stderr)

                list_response = execute_aws_call(service, operation, session=session)

                if isinstance(list_response, list) and list_response:
                    successful_operation = operation
                    debug_print(f"Successfully executed: {operation}")  # pragma: no mutate
                    if with_tracking and call_result is not None:
                        call_result.successful_responses.append(list_response)
                    break

            except Exception as e:
                debug_print(f"Operation {operation} failed: {e}")  # pragma: no mutate
                continue

        if not list_response or not successful_operation:
            error_msg = f"Could not find working list operation for parameter '{parameter_name}'"
            if with_tracking and call_result is not None:
                call_result.error_messages.append(error_msg)
                print(f"ERROR: {error_msg}", file=sys.stderr)
                print(f"ERROR: Tried operations: {possible_operations}", file=sys.stderr)
                return call_result, []
            else:
                print(f"ERROR: {error_msg}", file=sys.stderr)
                print(f"ERROR: Tried operations: {possible_operations}", file=sys.stderr)
                sys.exit(1)

        from .formatters import flatten_response

        list_resources = flatten_response(list_response)
        debug_print(
            f"Got {len(list_resources)} resources from {successful_operation}"
        )  # pragma: no mutate

        if resource_filters:
            filtered_list_resources = filter_resources(list_resources, resource_filters)
            debug_print(
                f"After resource filtering: {len(filtered_list_resources)} resources"
            )  # pragma: no mutate
        else:
            filtered_list_resources = list_resources

        print(f"Found {len(filtered_list_resources)} resources matching filters", file=sys.stderr)

        if not filtered_list_resources:
            error_msg = f"No resources found matching resource filters: {resource_filters}"
            if with_tracking and call_result is not None:
                call_result.error_messages.append(error_msg)
                print(f"ERROR: {error_msg}", file=sys.stderr)
                return call_result, []
            else:
                print(f"ERROR: {error_msg}", file=sys.stderr)
                sys.exit(1)

        parameter_values = extract_parameter_values(
            filtered_list_resources, parameter_name, hint_field
        )

        if not parameter_values:
            error_msg = f"Could not extract parameter '{parameter_name}' from filtered results"
            if with_tracking and call_result is not None:
                call_result.error_messages.append(error_msg)
                print(f"ERROR: {error_msg}", file=sys.stderr)
                return call_result, []
            else:
                print(f"ERROR: {error_msg}", file=sys.stderr)
                sys.exit(1)

        expects_list = parameter_expects_list(parameter_name)

        if expects_list:
            param_value = parameter_values
        else:
            if len(parameter_values) > 1:
                print(f"Multiple {parameter_name} values found matching filters:", file=sys.stderr)
                display_values = parameter_values[:10]
                for value in display_values:
                    print(f"- {value}", file=sys.stderr)

                if len(parameter_values) > 10:
                    remaining = len(parameter_values) - 10
                    print(
                        f"... and {remaining} more "
                        f"(showing first 10 of {len(parameter_values)} total)",
                        file=sys.stderr,
                    )

                print(f"Using first match: {parameter_values[0]}", file=sys.stderr)
            elif len(parameter_values) == 1:
                print(f"Using: {parameter_values[0]}", file=sys.stderr)

            param_value = parameter_values[0]

        debug_print(f"Using parameter value(s): {param_value}")  # pragma: no mutate

        try:
            client = get_client(service, session)
            converted_parameter_name = get_correct_parameter_name(client, action, parameter_name)
            debug_print(
                f"Parameter name resolution: {parameter_name} -> {converted_parameter_name}"
            )  # pragma: no mutate
        except Exception as e:
            debug_print(
                f"Could not create client for parameter introspection: {e}"
            )  # pragma: no mutate
            converted_parameter_name = convert_parameter_name(parameter_name)
            debug_print(
                f"Fallback parameter name conversion: "
                f"{parameter_name} -> {converted_parameter_name}"
            )  # pragma: no mutate

        parameters = {converted_parameter_name: param_value}

        # Final call with resolved parameters
        try:
            final_response = execute_aws_call(service, action, parameters, session)

            if isinstance(final_response, dict) and "validation_error" in final_response:
                error_msg = (
                    f"Still getting validation error after parameter resolution: "
                    f"{final_response['validation_error']}"
                )
                if with_tracking and call_result is not None:
                    call_result.error_messages.append(error_msg)
                    print(f"ERROR: {error_msg}", file=sys.stderr)
                    return call_result, []
                else:
                    print(f"ERROR: {error_msg}", file=sys.stderr)
                    sys.exit(1)
            else:
                # Final call succeeded
                response = final_response
                if with_tracking and call_result is not None:
                    call_result.successful_responses.append(final_response)
                    call_result.last_successful_response = final_response
                    call_result.final_success = True
                    debug_print(
                        f"Tracking: Final call to {service}.{action} succeeded"
                    )  # pragma: no mutate

        except Exception as e:
            if with_tracking and call_result is not None:
                call_result.error_messages.append(f"Final call failed: {str(e)}")
                debug_print(f"Final call failed: {e}")  # pragma: no mutate
                return call_result, []
            else:
                debug_print(f"Final call failed: {e}")  # pragma: no mutate
                sys.exit(1)

    # Process final response
    final_response_to_use = (
        call_result.last_successful_response
        if with_tracking and call_result is not None
        else response
    )
    if final_response_to_use:
        from .formatters import flatten_response

        resources = flatten_response(final_response_to_use)
        debug_print(f"Final call returned {len(resources)} resources")  # pragma: no mutate

        if value_filters:
            filtered_resources = filter_resources(resources, value_filters)
            debug_print(
                f"After value filtering: {len(filtered_resources)} resources"
            )  # pragma: no mutate
        else:
            filtered_resources = resources

        return (call_result, filtered_resources) if with_tracking else filtered_resources
    else:
        return (call_result, []) if with_tracking else []


def execute_multi_level_call_with_tracking(
    service,
    action,
    resource_filters,
    value_filters,
    column_filters,
    session=None,
    hint_function=None,
    hint_field=None,
):
    """Handle multi-level API calls with automatic parameter resolution and tracking"""
    return _execute_multi_level_call_internal(
        service,
        action,
        resource_filters,
        value_filters,
        column_filters,
        session,
        hint_function,
        hint_field,
        with_tracking=True,
    )


def execute_multi_level_call(
    service,
    action,
    resource_filters,
    value_filters,
    column_filters,
    session=None,
    hint_function=None,
    hint_field=None,
):
    """Handle multi-level API calls with automatic parameter resolution"""
    return _execute_multi_level_call_internal(
        service,
        action,
        resource_filters,
        value_filters,
        column_filters,
        session,
        hint_function,
        hint_field,
        with_tracking=False,
    )


def parse_validation_error(error):
    """Extract missing parameter info from ValidationError"""
    error_message = str(error)

    pattern = r"Value null at '([^']+)'"
    match = re.search(pattern, error_message)

    if match:
        parameter_name = match.group(1)
        return {"parameter_name": parameter_name, "is_required": True, "error_type": "null_value"}

    pattern = r"'([^']+)'[^:]*: Member must not be null"
    match = re.search(pattern, error_message)

    if match:
        parameter_name = match.group(1)
        return {
            "parameter_name": parameter_name,
            "is_required": True,
            "error_type": "required_parameter",
        }

    pattern = r"Either (\w+) or \w+ must be specified"
    match = re.search(pattern, error_message)

    if match:
        parameter_name = match.group(1)
        return {
            "parameter_name": parameter_name,
            "is_required": True,
            "error_type": "either_parameter",
        }

    pattern = r"Missing required parameter in input: ['\"]([^'\"]+)['\"]"
    match = re.search(pattern, error_message)

    if match:
        parameter_name = match.group(1)
        return {
            "parameter_name": parameter_name,
            "is_required": True,
            "error_type": "missing_parameter",
        }

    debug_print(f"Could not parse validation error: {error_message}")  # pragma: no mutate

    return None


def infer_list_operation(service, parameter_name, action):
    """Infer the list operation from parameter name first, then action name as fallback"""

    possible_operations = []

    if parameter_name.lower() not in ["name", "id", "arn"]:
        resource_name = parameter_name
        suffixes_to_remove = ["Name", "Id", "Arn", "ARN"]
        for suffix in suffixes_to_remove:
            if resource_name.endswith(suffix):
                resource_name = resource_name[: -len(suffix)]
                break

        resource_name = resource_name.lower()

        if resource_name.endswith("y"):
            plural_name = resource_name[:-1] + "ies"
        elif resource_name.endswith(("s", "sh", "ch", "x", "z")):
            plural_name = resource_name + "es"
        else:
            plural_name = resource_name + "s"

        possible_operations.extend(
            [
                f"list_{plural_name}",
                f"describe_{plural_name}",
                f"get_{plural_name}",
                f"list_{resource_name}",
                f"describe_{resource_name}",
                f"get_{resource_name}",
            ]
        )

        debug_print(
            f"Parameter-based inference: '{parameter_name}' -> '{resource_name}' -> "
            f"{len(possible_operations)} operations"
        )  # pragma: no mutate
    else:
        debug_print(
            f"Parameter '{parameter_name}' is too generic, skipping parameter-based inference"
        )  # pragma: no mutate

    prefixes = ["describe", "get", "update", "delete", "create", "list"]
    action_lower = action.lower().replace("-", "_")

    action_resource = action_lower
    for prefix in prefixes:
        if action_lower.startswith(prefix + "_"):
            action_resource = action_lower[len(prefix) + 1 :]
            break

    if action_resource.endswith("s") and len(action_resource) > 1:
        action_plural = action_resource
    elif action_resource.endswith("y"):
        action_plural = action_resource[:-1] + "ies"
    elif action_resource.endswith(("sh", "ch", "x", "z")):
        action_plural = action_resource + "es"
    else:
        action_plural = action_resource + "s"

    action_operations = [
        f"list_{action_plural}",
        f"describe_{action_plural}",
        f"get_{action_plural}",
        f"list_{action_resource}",
        f"describe_{action_resource}",
        f"get_{action_resource}",
    ]

    for op in action_operations:
        if op not in possible_operations:
            possible_operations.append(op)

    debug_print(
        f"Action-based inference: '{action}' -> '{action_resource}' -> "
        f"added {len(action_operations)} operations"
    )  # pragma: no mutate
    debug_print(f"Total possible operations: {possible_operations}")  # pragma: no mutate

    return possible_operations


def parameter_expects_list(parameter_name):
    """Determine if parameter expects list or single value"""
    list_indicators = ["s", "Names", "Ids", "Arns", "ARNs"]

    for indicator in list_indicators:
        if parameter_name.endswith(indicator):
            return True

    return False


def get_correct_parameter_name(client, action, parameter_name):
    """Get the correct case-sensitive parameter name for an operation.

    By introspecting the service model.
    """
    try:
        action_words = action.replace("-", "_").replace("_", " ").split()
        pascal_case_action = "".join(word.capitalize() for word in action_words)

        operation_model = client.meta.service_model.operation_model(pascal_case_action)

        debug_print(
            f"Introspecting parameter name for {action} (PascalCase: {pascal_case_action})"
        )  # pragma: no mutate

        if operation_model.input_shape:
            members = operation_model.input_shape.members
            debug_print(f"Available parameters: {list(members.keys())}")  # pragma: no mutate

            if parameter_name in members:
                debug_print(f"Found exact match: {parameter_name}")  # pragma: no mutate
                return parameter_name

            for member_name in members:
                if member_name.lower() == parameter_name.lower():
                    debug_print(
                        f"Found case-insensitive match: {parameter_name} -> {member_name}"
                    )  # pragma: no mutate
                    return member_name

            pascal_case = parameter_name[0].upper() + parameter_name[1:]
            if pascal_case in members:
                debug_print(
                    f"Found PascalCase match: {parameter_name} -> {pascal_case}"
                )  # pragma: no mutate
                return pascal_case

            debug_print(
                f"No parameter match found for '{parameter_name}' in {list(members.keys())}"
            )  # pragma: no mutate
        else:
            debug_print(f"Operation {pascal_case_action} has no input shape")  # pragma: no mutate

        debug_print(f"Using original parameter name: {parameter_name}")  # pragma: no mutate
        return parameter_name

    except Exception as e:
        debug_print(f"Could not introspect parameter name: {e}")  # pragma: no mutate
        fallback = convert_parameter_name(parameter_name)
        debug_print(
            f"Falling back to PascalCase: {parameter_name} -> {fallback}"
        )  # pragma: no mutate
        return fallback


def show_keys_from_result(call_result):
    """Show keys only if final call succeeded"""
    if call_result.final_success and call_result.last_successful_response:
        from .formatters import extract_and_sort_keys, flatten_response

        resources = flatten_response(call_result.last_successful_response)
        if not resources:
            return "Error: No data to extract keys from in successful response"

        # Use non-simplified keys to show full nested structure
        sorted_keys = extract_and_sort_keys(resources, simplify=False)
        return "\n".join(f"  {key}" for key in sorted_keys)
    else:
        if call_result.error_messages:
            error_msg = "; ".join(call_result.error_messages)
            return f"Error: No successful response to show keys from ({error_msg})"
        else:
            return "Error: No successful response to show keys from"
