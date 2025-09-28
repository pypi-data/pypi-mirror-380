"""Utility functions for AWS Query Tool."""

import sys

import boto3


class AWSQueryError(Exception):
    """Base exception for AWS Query Tool"""


class ValidationError(AWSQueryError):
    """Error in parameter validation"""


class SecurityError(AWSQueryError):
    """Security policy violation"""


class CredentialsError(AWSQueryError):
    """AWS credentials issue"""


class OperationError(AWSQueryError):
    """AWS operation failed"""


def convert_parameter_name(parameter_name):
    """Convert parameter name from camelCase to PascalCase for AWS API compatibility"""
    if not parameter_name:
        return parameter_name

    return (
        parameter_name[0].upper() + parameter_name[1:]
        if len(parameter_name) > 0
        else parameter_name
    )


def pascal_to_kebab_case(pascal_case_str):
    """Convert PascalCase to kebab-case (e.g., 'ListStacks' -> 'list-stacks')"""
    if not pascal_case_str:
        return pascal_case_str

    import re

    # Insert hyphens before uppercase letters (except the first one)
    kebab_case = re.sub(r"(?<!^)(?=[A-Z])", "-", pascal_case_str)
    return kebab_case.lower()


class DebugContext:
    """Context manager for debug output"""

    def __init__(self, enabled=False):
        """Initialize debug context with optional enabled state."""
        self.enabled = enabled

    def print(self, *args, **kwargs):
        """Print debug messages with [DEBUG] prefix and timestamp when enabled"""
        if self.enabled:
            import datetime

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            debug_prefix = f"[DEBUG] {timestamp}"

            if args:
                first_arg = f"{debug_prefix} {args[0]}"
                remaining_args = args[1:]
                print(first_arg, *remaining_args, file=sys.stderr, **kwargs)
            else:
                print(debug_prefix, file=sys.stderr, **kwargs)

    def enable(self):
        """Enable debug output"""
        self.enabled = True

    def disable(self):
        """Disable debug output"""
        self.enabled = False


# Global debug context
_debug_context = DebugContext()


def debug_print(*args, **kwargs):
    """Print debug messages with [DEBUG] prefix and timestamp when debug mode is enabled"""
    _debug_context.print(*args, **kwargs)


def set_debug_enabled(value):
    """Set debug mode on or off"""
    if value:
        _debug_context.enable()
    else:
        _debug_context.disable()


def get_debug_enabled():
    """Get current debug mode state"""
    return _debug_context.enabled


# Simple debug_enabled property for module-level access
class _DebugEnabled:
    """Simple debug enabled property without backward compatibility complexity"""

    def __bool__(self):
        return _debug_context.enabled

    def __eq__(self, other):
        return _debug_context.enabled == other

    def __repr__(self):
        return str(_debug_context.enabled)


debug_enabled = _DebugEnabled()


def sanitize_input(value):
    """Basic input sanitization"""
    if not isinstance(value, str):
        return str(value)
    # Note: $ is not included as it's used for suffix matching in filters
    dangerous = ["|", ";", "&", "`", "(", ")", "[", "]", "{", "}"]
    for char in dangerous:
        value = value.replace(char, "")
    return value.strip()


def normalize_action_name(action):
    """Convert CLI-style action names to boto3 method names"""
    normalized = action.replace("-", "_")

    import re

    normalized = re.sub("([a-z0-9])([A-Z])", r"\1_\2", normalized)

    normalized = normalized.lower()

    return normalized


def simplify_key(full_key):
    """Extract the last non-numeric attribute from a flattened key

    Examples:
    - "Instances.0.NetworkInterfaces.0.SubnetId" -> "SubnetId"
    - "Buckets.0.Name" -> "Name"
    - "Owner.DisplayName" -> "DisplayName"
    - "ReservationId" -> "ReservationId"
    """
    if not full_key:
        return full_key

    parts = full_key.split(".")

    for part in reversed(parts):
        if not part.isdigit():
            return part

    return parts[-1] if parts else full_key


def get_aws_services():
    """Get list of available AWS services"""
    try:
        session = boto3.Session()
        return sorted(session.get_available_services())
    except Exception as e:
        print(f"ERROR: Failed to get AWS services: {e}", file=sys.stderr)
        return []


def get_service_actions(service):
    """Get available actions for a service"""
    try:
        client = boto3.client(service)
        operations = client.meta.service_model.operation_names
        read_ops = [
            op
            for op in operations
            if any(op.lower().startswith(prefix) for prefix in ["describe", "list", "get"])
        ]
        return sorted(read_ops)
    except Exception as e:
        print(f"ERROR: Failed to get actions for {service}: {e}", file=sys.stderr)
        return []


def create_session(region=None, profile=None):
    """Create boto3 session with optional region/profile"""
    debug_print(
        f"create_session called with region={repr(region)}, profile={repr(profile)}"
    )  # pragma: no mutate
    session_kwargs = {}
    if region and region.strip():
        session_kwargs["region_name"] = region
        debug_print(f"Added region_name={region} to session")  # pragma: no mutate
    if profile and profile.strip():
        session_kwargs["profile_name"] = profile
        debug_print(f"Added profile_name={profile} to session")  # pragma: no mutate
    debug_print(f"Creating session with kwargs: {session_kwargs}")  # pragma: no mutate
    return boto3.Session(**session_kwargs)


def get_client(service, session=None):
    """Get boto3 client from session or create default"""
    if session:
        return session.client(service)
    return boto3.client(service)
