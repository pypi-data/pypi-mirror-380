"""Filtering logic for AWS Query Tool."""

from __future__ import annotations

import sys
from typing import Dict, List

from .formatters import flatten_dict_keys, transform_tags_structure
from .utils import convert_parameter_name, debug_print, simplify_key


def parse_filter_pattern(filter_text):
    """Parse filter pattern to extract ^ and $ operators and determine matching mode.

    Returns:
        tuple: (filter_pattern, match_mode) where match_mode is one of:
               'exact', 'prefix', 'suffix', 'contains'
    """
    if not filter_text:
        return "", "contains"

    # Check for prefix operator (^ at start) - support both ASCII and modifier circumflex
    # U+005E (^) is the standard ASCII circumflex
    # U+02C6 (ˆ) is the modifier letter circumflex that some keyboards produce
    has_prefix = filter_text.startswith("^") or filter_text.startswith("ˆ")
    # Check for suffix operator ($ at end)
    has_suffix = filter_text.endswith("$")

    # Extract the actual pattern by removing ^ or ˆ from start and $ from end
    pattern = filter_text
    if has_prefix:
        pattern = pattern[1:]  # Remove ^ or ˆ
    if has_suffix:
        pattern = pattern[:-1]  # Remove $

    # Determine match mode based on ^ and $ operators
    if has_prefix and has_suffix:
        mode = "exact"
    elif has_prefix:
        mode = "prefix"
    elif has_suffix:
        mode = "suffix"
    else:
        mode = "contains"

    return pattern, mode


def matches_pattern(text, pattern, mode):
    """Check if text matches pattern according to the given mode.

    Args:
        text: The text to check
        pattern: The pattern to match against
        mode: One of 'exact', 'prefix', 'suffix', 'contains'

    Returns:
        bool: True if text matches pattern according to mode
    """
    text_lower = str(text).lower()
    pattern_lower = str(pattern).lower()

    if mode == "exact":
        return text_lower == pattern_lower
    elif mode == "prefix":
        return text_lower.startswith(pattern_lower)
    elif mode == "suffix":
        return text_lower.endswith(pattern_lower)
    else:  # contains
        return pattern_lower in text_lower


def filter_resources(resources, value_filters):
    """Filter resources by value filters (ALL must match)"""
    if not value_filters:
        return resources

    # Parse filter patterns once
    parsed_filters = []
    for filter_text in value_filters:
        pattern, mode = parse_filter_pattern(filter_text)
        parsed_filters.append((pattern, mode))
        debug_print(f"Applying value filter: {filter_text} (mode: {mode})")  # pragma: no mutate

    # Apply tag transformation before filtering
    transformed_resources = []
    for resource in resources:
        transformed = transform_tags_structure(resource)
        transformed_resources.append(transformed)

    filtered: List[Dict] = []
    for resource in transformed_resources:
        flattened = flatten_dict_keys(resource)

        searchable_items = []

        searchable_items.extend([key for key in flattened.keys()])
        searchable_items.extend([str(value) for value in flattened.values()])

        if len(filtered) + len([r for r in resources if r != resource]) < 3:
            debug_print(f"Sample flattened keys: {list(flattened.keys())[:5]}")  # pragma: no mutate
            debug_print(f"Sample searchable items: {searchable_items[:10]}")  # pragma: no mutate

        matches_all = True
        for pattern, mode in parsed_filters:
            if not pattern:  # Empty pattern matches everything
                continue

            # Check if any item matches the pattern with the given mode
            matched = False
            for item in searchable_items:
                if matches_pattern(item, pattern, mode):
                    matched = True
                    matching_items = [
                        i for i in searchable_items if matches_pattern(i, pattern, mode)
                    ]
                    debug_print(
                        f"Filter '{pattern}' (mode: {mode}) matched: {matching_items[:3]}"
                        f"{'...' if len(matching_items) > 3 else ''}"
                    )  # pragma: no mutate
                    break

            if not matched:
                matches_all = False
                break

        if matches_all:
            filtered.append(resource)

    debug_print(
        f"Found {len(filtered)} resources matching filters (out of {len(resources)} total)"
    )  # pragma: no mutate
    return filtered


def parse_multi_level_filters_for_mode(argv, mode="single"):
    """Parse command line args with -- separators for proper filtering based on mode

    Mode behavior:
        single: resource_filters=[], everything else as value/column filters
        multi: proper semantic meaning of separators:
               - Args before first -- = resource filters
               - Args between first and second -- = value filters
               - Args after second -- = column filters
    """
    separator_positions = []
    for i, arg in enumerate(argv):
        if arg == "--":
            separator_positions.append(i)

    segments = []
    start = 0

    for pos in separator_positions:
        segments.append(argv[start:pos])
        start = pos + 1

    segments.append(argv[start:])

    first_segment = segments[0] if segments else []

    third_segment: List[str]
    if len(segments) == 1:
        second_segment = []
        third_segment = []
    elif len(segments) == 2:
        second_segment = segments[1]
        third_segment = []
    else:
        second_segment = segments[1]
        third_segment = segments[2]

    base_command = []
    service_found = False
    action_found = False
    extra_args = []

    for arg in first_segment:
        if arg.startswith("-"):
            base_command.append(arg)
        elif not service_found:
            base_command.append(arg)
            service_found = True
        elif not action_found:
            base_command.append(arg)
            action_found = True
        else:
            extra_args.append(arg)

    if mode == "single":
        resource_filters: List[str] = []

        if len(segments) == 1:
            value_filters = extra_args
            column_filters = []
        elif len(segments) == 2:
            value_filters = extra_args
            column_filters = second_segment
        else:
            value_filters = extra_args + second_segment
            column_filters = third_segment

    elif mode == "multi":
        if len(segments) == 1:
            # No separators: all args are resource filters (before first --)
            resource_filters = extra_args
            value_filters = []
            column_filters = []
        elif len(segments) == 2:
            # One separator: args split between resource and value filters
            resource_filters = extra_args
            value_filters = second_segment
            column_filters = []
        else:
            # Two or more separators: full three-way split
            resource_filters = extra_args
            value_filters = second_segment
            column_filters = third_segment

    else:
        raise ValueError(f"Invalid mode '{mode}'. Must be 'single' or 'multi'.")

    debug_print(
        f"Multi-level parsing (mode={mode}) - Base: {base_command}, "
        f"Resource: {resource_filters}, Value: {value_filters}, "
        f"Column: {column_filters}"
    )  # pragma: no mutate

    return base_command, resource_filters, value_filters, column_filters


def extract_parameter_values(resources, parameter_name, field_hint=None):
    """Extract parameter values from list operation results"""
    if not resources:
        return []

    values = []

    if resources and isinstance(resources[0], str):
        debug_print(
            f"Resources are simple strings, using them directly for parameter '{parameter_name}'"
        )  # pragma: no mutate
        return resources

    # Apply tag transformation before parameter extraction
    transformed_resources = []
    for resource in resources:
        transformed = transform_tags_structure(resource)
        transformed_resources.append(transformed)

    # If field hint is provided, use it as the primary search target
    if field_hint:
        debug_print(
            f"Using field hint '{field_hint}' for parameter extraction"
        )  # pragma: no mutate

        for resource in transformed_resources:
            flat = flatten_dict_keys(resource)

            # Try exact match first
            if field_hint in flat:
                value = flat[field_hint]
                if value:
                    values.append(str(value))
                    continue

            # Try case-insensitive match
            for key, value in flat.items():
                if key.lower() == field_hint.lower() and value:
                    values.append(str(value))
                    break
            else:
                # Try partial match
                matching_keys = [k for k in flat.keys() if field_hint.lower() in k.lower()]
                if matching_keys:
                    key = matching_keys[0]
                    value = flat[key]
                    if value:
                        values.append(str(value))

        debug_print(f"Field hint extraction found {len(values)} values")  # pragma: no mutate
        return values

    # Fall back to default heuristic search
    pascal_case_name = convert_parameter_name(parameter_name)
    search_names = [parameter_name, pascal_case_name]

    debug_print(f"Looking for parameter values using names: {search_names}")  # pragma: no mutate

    for resource in transformed_resources:
        flat = flatten_dict_keys(resource)

        found_value = None
        for search_name in search_names:
            if search_name in flat:
                value = flat[search_name]
                if value:
                    found_value = str(value)
                    break

        if found_value:
            values.append(found_value)
            continue

        for search_name in search_names:
            for key, value in flat.items():
                if key.lower() == search_name.lower() and value:
                    found_value = str(value)
                    break
            if found_value:
                break

        if found_value:
            values.append(found_value)
            continue

        for search_name in search_names:
            matching_keys = [k for k in flat.keys() if search_name.lower() in k.lower()]
            if matching_keys:
                key = matching_keys[0]
                value = flat[key]
                if value:
                    values.append(str(value))
                    break

        if found_value:
            continue

        # Standard field fallback when parameter-specific field not found
        standard_fields = []
        param_lower = parameter_name.lower()

        if param_lower.endswith("name"):
            standard_fields.append("Name")
        elif param_lower.endswith("id"):
            standard_fields.append("Id")
        elif param_lower.endswith(("arn", "ARN")):
            standard_fields.extend(["Arn", "ARN"])
        elif param_lower.endswith("key"):
            standard_fields.append("Key")
        elif param_lower.endswith("value"):
            standard_fields.append("Value")
        else:
            # Common AWS resource types that typically have a Name field
            resource_types_with_names = [
                "bucket",
                "cluster",
                "instance",
                "volume",
                "snapshot",
                "image",
                "vpc",
                "subnet",
                "queue",
                "topic",
                "table",
                "function",
                "role",
                "user",
                "group",
                "policy",
                "stack",
                "template",
                "pipeline",
                "repository",
                "branch",
                "commit",
                "build",
                "project",
                "job",
                "task",
                "service",
                "container",
                "node",
                "nodegroup",
                "database",
                "endpoint",
                "domain",
                "certificate",
                "key",
                "secret",
                "parameter",
            ]

            if param_lower in resource_types_with_names:
                standard_fields.append("Name")
                debug_print(
                    f"Parameter '{parameter_name}' is a resource type, will try Name field"
                )  # pragma: no mutate

        if standard_fields:
            debug_print(
                f"No specific field found for '{parameter_name}', "
                f"trying standard fields: {standard_fields}"
            )  # pragma: no mutate
            for standard_field in standard_fields:
                if standard_field in flat:
                    value = flat[standard_field]
                    if value:
                        debug_print(
                            f"Found standard field '{standard_field}' "
                            f"for parameter '{parameter_name}'"
                        )  # pragma: no mutate
                        values.append(str(value))
                        found_value = str(value)
                        break

                for key, value in flat.items():
                    if key.lower() == standard_field.lower() and value:
                        debug_print(
                            f"Found standard field '{key}' (case-insensitive) "
                            f"for parameter '{parameter_name}'"
                        )  # pragma: no mutate
                        values.append(str(value))
                        found_value = str(value)
                        break

                if found_value:
                    break

    debug_print(
        f"Extracted {len(values)} values for parameter '{parameter_name}': "
        f"{values[:3]}{'...' if len(values) > 3 else ''}"
    )  # pragma: no mutate

    return values
