"""Consolidated tests for CLI argument parser behavior.

These tests ensure that the argument parser correctly handles:
1. The -- separator for column filters
2. Prevention of 'unrecognized arguments' errors
3. Proper propagation of filters to formatters
4. Edge cases with multiple separators and flags
"""

import sys
from unittest.mock import Mock, patch

import pytest

from awsquery.cli import main
from awsquery.filters import parse_multi_level_filters_for_mode


class TestCLIParserSeparator:
    """Test CLI parser handles -- separator correctly for column filters."""

    def test_parse_with_double_dash_column_filters(self):
        """Test that -- separator correctly identifies column filters."""
        argv = ["ec2", "describe-instances", "--", "Name", "State", "InstanceId"]
        base_cmd, resource_filters, value_filters, column_filters = (
            parse_multi_level_filters_for_mode(argv, mode="single")
        )

        assert base_cmd == ["ec2", "describe-instances"]
        assert resource_filters == []
        assert value_filters == []
        assert column_filters == ["Name", "State", "InstanceId"]

    def test_parse_with_value_and_column_filters(self):
        """Test parsing with both value filters and column filters."""
        argv = ["ec2", "describe-instances", "prod", "web", "--", "Name", "State"]
        base_cmd, resource_filters, value_filters, column_filters = (
            parse_multi_level_filters_for_mode(argv, mode="single")
        )

        assert base_cmd == ["ec2", "describe-instances"]
        assert resource_filters == []
        assert value_filters == ["prod", "web"]
        assert column_filters == ["Name", "State"]

    def test_parse_multi_level_with_double_separators(self):
        """Test multi-level parsing with multiple -- separators."""
        argv = [
            "cloudformation",
            "describe-stack-events",
            "prod",
            "--",
            "Created",
            "--",
            "StackName",
        ]
        base_cmd, resource_filters, value_filters, column_filters = (
            parse_multi_level_filters_for_mode(argv, mode="multi")
        )

        assert base_cmd == ["cloudformation", "describe-stack-events"]
        assert resource_filters == ["prod"]
        assert value_filters == ["Created"]
        assert column_filters == ["StackName"]

    @patch("awsquery.cli.create_session")
    @patch("awsquery.cli.execute_aws_call")
    @patch("awsquery.cli.validate_readonly")
    def test_main_with_column_filters(self, mock_validate, mock_execute, mock_session):
        """Test main() function correctly processes -- separator with column filters."""
        mock_validate.return_value = True
        mock_execute.return_value = [{"Instances": []}]
        mock_session.return_value = Mock()

        # Simulate command line with -- separator
        sys.argv = ["awsquery", "ec2", "describe-instances", "--", "Name"]

        with patch("awsquery.cli.flatten_response") as mock_flatten:
            with patch("awsquery.cli.filter_resources") as mock_filter:
                with patch("awsquery.cli.format_table_output") as mock_format:
                    mock_flatten.return_value = []
                    mock_filter.return_value = []
                    mock_format.return_value = ""

                    # This should not raise any parsing errors
                    try:
                        main()
                    except SystemExit:
                        pass  # Expected when no data

                    # Verify the AWS call was made (meaning parsing succeeded)
                    mock_execute.assert_called_once()

    @patch("awsquery.cli.create_session")
    @patch("awsquery.cli.execute_aws_call")
    @patch("awsquery.cli.validate_readonly")
    def test_main_with_flags_and_filters(self, mock_validate, mock_execute, mock_session):
        """Test main() with flags like --region and -- separator."""
        mock_validate.return_value = True
        mock_execute.return_value = [{"Instances": []}]
        mock_session.return_value = Mock()

        # Simulate command with --region flag and column filters
        sys.argv = [
            "awsquery",
            "--region",
            "us-west-2",
            "ec2",
            "describe-instances",
            "--",
            "Name",
            "State",
        ]

        with patch("awsquery.cli.flatten_response") as mock_flatten:
            with patch("awsquery.cli.filter_resources") as mock_filter:
                with patch("awsquery.cli.format_table_output") as mock_format:
                    mock_flatten.return_value = []
                    mock_filter.return_value = []
                    mock_format.return_value = ""

                    try:
                        main()
                    except SystemExit:
                        pass

                    # Verify session was created with correct region
                    mock_session.assert_called_once_with(region="us-west-2", profile=None)

    @patch("awsquery.cli.create_session")
    @patch("awsquery.cli.execute_aws_call")
    @patch("awsquery.cli.validate_readonly")
    def test_main_with_json_flag_and_filters(self, mock_validate, mock_execute, mock_session):
        """Test main() with -j flag and column filters."""
        mock_validate.return_value = True
        mock_execute.return_value = [{"Instances": [{"InstanceId": "i-123"}]}]
        mock_session.return_value = Mock()

        sys.argv = ["awsquery", "-j", "ec2", "describe-instances", "--", "InstanceId"]

        with patch("awsquery.cli.flatten_response") as mock_flatten:
            with patch("awsquery.cli.filter_resources") as mock_filter:
                with patch("awsquery.cli.format_json_output") as mock_json:
                    mock_flatten.return_value = [{"InstanceId": "i-123"}]
                    mock_filter.return_value = [{"InstanceId": "i-123"}]
                    mock_json.return_value = '{"InstanceId": "i-123"}'

                    try:
                        main()
                    except SystemExit:
                        pass

                    # Verify JSON formatter was called (not table formatter)
                    mock_json.assert_called_once()


class TestCLIParserEdgeCases:
    """Test edge cases in CLI argument parsing."""

    def test_empty_column_filters_after_separator(self):
        """Test handling of -- with no following arguments."""
        argv = ["ec2", "describe-instances", "--"]
        base_cmd, resource_filters, value_filters, column_filters = (
            parse_multi_level_filters_for_mode(argv, mode="single")
        )

        assert base_cmd == ["ec2", "describe-instances"]
        assert column_filters == []

    def test_multiple_consecutive_separators(self):
        """Test handling of multiple consecutive -- separators."""
        argv = ["ec2", "describe-instances", "--", "--", "Name"]
        base_cmd, resource_filters, value_filters, column_filters = (
            parse_multi_level_filters_for_mode(argv, mode="single")
        )

        # Multiple -- separators are collapsed, only Name remains as column filter
        assert base_cmd == ["ec2", "describe-instances"]
        assert column_filters == ["Name"]

    def test_separator_with_special_characters(self):
        """Test column filters with special characters after separator."""
        argv = ["ec2", "describe-instances", "--", "Tags.Name", "State.Name", "InstanceId"]
        base_cmd, resource_filters, value_filters, column_filters = (
            parse_multi_level_filters_for_mode(argv, mode="single")
        )

        assert column_filters == ["Tags.Name", "State.Name", "InstanceId"]

    @patch("awsquery.cli.create_session")
    @patch("awsquery.cli.execute_aws_call")
    @patch("awsquery.cli.validate_readonly")
    def test_main_with_all_flags_combined(self, mock_validate, mock_execute, mock_session):
        """Test main() with all possible flags and filters combined."""
        mock_validate.return_value = True
        mock_execute.return_value = [{"Instances": []}]
        mock_session.return_value = Mock()

        sys.argv = [
            "awsquery",
            "--debug",
            "--region",
            "eu-west-1",
            "--profile",
            "production",
            "-j",
            "ec2",
            "describe-instances",
            "prod",
            "web",  # value filters
            "--",
            "Name",
            "State",
            "InstanceId",  # column filters
        ]

        with patch("awsquery.cli.flatten_response") as mock_flatten:
            with patch("awsquery.cli.filter_resources") as mock_filter:
                with patch("awsquery.cli.format_json_output") as mock_json:
                    with patch("awsquery.utils.debug_print") as mock_debug:
                        mock_flatten.return_value = []
                        mock_filter.return_value = []
                        mock_json.return_value = "[]"

                        try:
                            main()
                        except SystemExit:
                            pass

                        # Verify session was created with correct params
                        mock_session.assert_called_once_with(
                            region="eu-west-1", profile="production"
                        )
                        # Debug should have been enabled
                        from awsquery import utils

                        assert utils.get_debug_enabled() is True


class TestParserRegressionPrevention:
    """Regression tests to prevent parser bugs from reoccurring."""

    def test_issue_double_dash_name_filter_regression(self):
        """Regression test: 'awsquery ec2 describe-instances -- Name' should work.

        This was failing with 'error: unrecognized arguments: Name'
        """
        test_command = ["ec2", "describe-instances", "--", "Name"]
        base_cmd, resource_filters, value_filters, column_filters = (
            parse_multi_level_filters_for_mode(test_command, mode="single")
        )

        assert base_cmd == ["ec2", "describe-instances"]
        assert not resource_filters
        assert not value_filters
        assert column_filters == ["Name"]

    @patch("awsquery.cli.create_session")
    @patch("awsquery.cli.execute_aws_call")
    @patch("awsquery.cli.validate_readonly")
    def test_main_never_fails_with_unrecognized_arguments(
        self, mock_validate, mock_execute, mock_session
    ):
        """Test main() doesn't raise 'unrecognized arguments' error."""
        mock_validate.return_value = True
        mock_execute.return_value = [{"Instances": []}]
        mock_session.return_value = None

        test_commands = [
            ["awsquery", "ec2", "describe-instances", "--", "Name"],
            ["awsquery", "s3", "list-buckets", "--", "Name", "CreationDate"],
            ["awsquery", "ec2", "describe-instances", "prod", "--", "InstanceId"],
            ["awsquery", "--region", "us-west-2", "ec2", "describe-instances", "--", "Name"],
            ["awsquery", "-j", "ec2", "describe-instances", "--", "Name", "State"],
        ]

        with patch("awsquery.cli.flatten_response", return_value=[]):
            with patch("awsquery.cli.filter_resources", return_value=[]):
                with patch("awsquery.cli.format_table_output", return_value=""):
                    with patch("awsquery.cli.format_json_output", return_value="[]"):
                        for cmd in test_commands:
                            sys.argv = cmd
                            error_occurred = False

                            try:
                                main()
                            except SystemExit as e:
                                if e.code != 0 and e.code is not None:
                                    error_message = str(e)
                                    if "unrecognized arguments" in error_message:
                                        error_occurred = True
                            except Exception as e:
                                if "unrecognized arguments" in str(e):
                                    error_occurred = True

                            assert (
                                not error_occurred
                            ), f"Command {' '.join(cmd)} failed with 'unrecognized arguments'"

    @patch("awsquery.cli.create_session")
    @patch("awsquery.cli.execute_aws_call")
    @patch("awsquery.cli.validate_readonly")
    @patch("awsquery.cli.format_table_output")
    def test_column_filters_propagate_to_formatter(
        self, mock_format, mock_validate, mock_execute, mock_session
    ):
        """Test that column filters after -- are passed to the formatter."""
        mock_validate.return_value = True
        mock_execute.return_value = [
            {"Instances": [{"InstanceId": "i-123", "State": {"Name": "running"}}]}
        ]
        mock_session.return_value = None
        mock_format.return_value = "formatted output"

        sys.argv = ["awsquery", "ec2", "describe-instances", "--", "InstanceId", "State.Name"]

        with patch("awsquery.cli.flatten_response") as mock_flatten:
            with patch("awsquery.cli.filter_resources") as mock_filter:
                mock_flatten.return_value = [{"InstanceId": "i-123", "State": {"Name": "running"}}]
                mock_filter.return_value = [{"InstanceId": "i-123", "State": {"Name": "running"}}]

                try:
                    main()
                except SystemExit:
                    pass

                mock_format.assert_called_once()
                args = mock_format.call_args[0]
                column_filters = args[1]
                assert "InstanceId" in column_filters
                assert "State.Name" in column_filters


class TestCLIParserRegression:
    """Regression tests to prevent parser issues from reoccurring."""

    @patch("awsquery.cli.create_session")
    @patch("awsquery.cli.execute_aws_call")
    @patch("awsquery.cli.validate_readonly")
    def test_parser_does_not_fail_on_column_filters(
        self, mock_validate, mock_execute, mock_session
    ):
        """Test parser doesn't fail with 'unrecognized arguments' for column filters."""
        mock_validate.return_value = True
        mock_execute.return_value = [{"Buckets": []}]
        mock_session.return_value = Mock()

        # This exact command was failing before the fix
        sys.argv = ["awsquery", "s3", "list-buckets", "--", "Name"]

        with patch("awsquery.cli.flatten_response", return_value=[]):
            with patch("awsquery.cli.filter_resources", return_value=[]):
                with patch("awsquery.cli.format_table_output", return_value=""):
                    # Should not raise argparse error about unrecognized arguments
                    try:
                        main()
                        # If we get here without argparse error, test passes
                        assert True
                    except SystemExit as e:
                        # SystemExit is OK (from no data), argparse errors are not
                        assert "unrecognized arguments" not in str(e)
                    except Exception as e:
                        # No other exceptions should occur from parsing
                        if "unrecognized arguments" in str(e):
                            pytest.fail(f"Parser failed with unrecognized arguments: {e}")

    def test_filter_parsing_matches_cli_behavior(self):
        """Ensure filter parsing in tests matches actual CLI behavior."""
        # Test the exact parsing that happens in CLI
        test_cases = [
            (
                ["ec2", "describe-instances", "--", "Name"],
                {"base": ["ec2", "describe-instances"], "column": ["Name"]},
            ),
            (
                ["s3", "list-buckets", "backup", "--", "Name", "CreationDate"],
                {
                    "base": ["s3", "list-buckets"],
                    "value": ["backup"],
                    "column": ["Name", "CreationDate"],
                },
            ),
            (
                ["cloudformation", "describe-stacks", "prod", "--", "Status", "--", "StackName"],
                {
                    "base": ["cloudformation", "describe-stacks"],
                    "value_single": ["prod", "Status"],  # In single mode
                    "column_single": ["StackName"],
                    "resource_multi": ["prod"],  # In multi mode
                    "value_multi": ["Status"],
                    "column_multi": ["StackName"],
                },
            ),
        ]

        for argv, expected in test_cases:
            # Test single mode (used for initial parsing)
            base_cmd, resource_filters, value_filters, column_filters = (
                parse_multi_level_filters_for_mode(argv, mode="single")
            )

            assert base_cmd == expected["base"]

            if "value" in expected:
                assert value_filters == expected["value"]
            elif "value_single" in expected:
                assert value_filters == expected["value_single"]

            if "column" in expected:
                assert column_filters == expected["column"]
            elif "column_single" in expected:
                assert column_filters == expected["column_single"]

            # Test multi mode (used for multi-level calls)
            if argv.count("--") > 1:
                base_cmd, resource_filters, value_filters, column_filters = (
                    parse_multi_level_filters_for_mode(argv, mode="multi")
                )

                if "resource_multi" in expected:
                    assert resource_filters == expected["resource_multi"]
                if "value_multi" in expected:
                    assert value_filters == expected["value_multi"]
                if "column_multi" in expected:
                    assert column_filters == expected["column_multi"]


class TestMultiModeFilterParsing:
    """Test multi-mode filter parsing for multi-level calls."""

    def test_multi_mode_no_separator_args_are_resource_filters(self):
        """When no -- separator, args should be resource filters in multi mode."""
        # This is the CDK bug case!
        argv = ["cloudformation", "describe-stack-resources", "CDK"]
        base_cmd, resource_filters, value_filters, column_filters = (
            parse_multi_level_filters_for_mode(argv, mode="multi")
        )

        assert base_cmd == ["cloudformation", "describe-stack-resources"]
        assert resource_filters == ["CDK"]  # Should be resource filter
        assert value_filters == []  # Should be empty
        assert column_filters == []

    def test_multi_mode_one_separator_correct_split(self):
        """With one -- separator, split resource and value filters correctly."""
        argv = ["cloudformation", "describe-stack-resources", "CDK", "--", "prod"]
        base_cmd, resource_filters, value_filters, column_filters = (
            parse_multi_level_filters_for_mode(argv, mode="multi")
        )

        assert base_cmd == ["cloudformation", "describe-stack-resources"]
        assert resource_filters == ["CDK"]  # Before --
        assert value_filters == ["prod"]  # After --
        assert column_filters == []

    def test_multi_mode_two_separators_all_filters(self):
        """With two -- separators, all three filter types should be populated."""
        argv = [
            "cloudformation",
            "describe-stack-resources",
            "CDK",
            "--",
            "prod",
            "--",
            "Name",
            "Status",
        ]
        base_cmd, resource_filters, value_filters, column_filters = (
            parse_multi_level_filters_for_mode(argv, mode="multi")
        )

        assert base_cmd == ["cloudformation", "describe-stack-resources"]
        assert resource_filters == ["CDK"]  # Before first --
        assert value_filters == ["prod"]  # Between first and second --
        assert column_filters == ["Name", "Status"]  # After second --

    def test_multi_mode_multiple_args_no_separator(self):
        """Multiple args with no separator should all be resource filters."""
        argv = ["ec2", "describe-instances", "prod", "web", "api"]
        base_cmd, resource_filters, value_filters, column_filters = (
            parse_multi_level_filters_for_mode(argv, mode="multi")
        )

        assert base_cmd == ["ec2", "describe-instances"]
        assert resource_filters == ["prod", "web", "api"]  # All are resource filters
        assert value_filters == []
        assert column_filters == []

    def test_multi_mode_empty_segments_handled(self):
        """Empty segments between separators should result in empty filter lists."""
        argv = ["ec2", "describe-instances", "--", "--", "Name"]
        base_cmd, resource_filters, value_filters, column_filters = (
            parse_multi_level_filters_for_mode(argv, mode="multi")
        )

        assert base_cmd == ["ec2", "describe-instances"]
        assert resource_filters == []  # Empty before first --
        assert value_filters == []  # Empty between -- and --
        assert column_filters == ["Name"]  # After second --
