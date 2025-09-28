# awsquery - AWS API Query Tool

AWS CLI tool to run any awscli read command and filter the resulting Values and JSON for custom table output.

The following command will find all ec2 instances where `prod`and `web` are found somewhere in the Value
of any key of the whole response. For all matching resources it will extract all fields that match
any of the second filters, so anything that matches `Tags.Name`, `State`, `InstanceId` or `vpcid`.
```
awsquery ec2 describe-instances prod web -- Tags.Name State InstanceId vpcid
```

This creates endless flexibility to shape your aws cli calls, filter any output and present exactly
the data you need during review, debugging or development.

## Features

- **Smart Multi-Level Calls**: Automatically resolves missing parameters by inferring and calling list operations
- **Flexible Filtering**: Multi-level filtering with `--` separators for resource, value, and column filters
- **Partial Matching**: All filters use case-insensitive partial matching (both value and column filters)
- **Keys Discovery**: Show all available fields from any API response with `-k`/`--keys` (fixed to show keys from successful responses)
- **Debug Mode**: Comprehensive debug output with `-d`/`--debug` featuring structured output with timestamps and DebugContext tracking
- **Security Validation**: Enforces ReadOnly AWS operations with comprehensive validation
- **Smart Auto-completion**: Enhanced tab completion with split matching and prefix priority for AWS services and actions
- **Smart Parameter Extraction**: Handles both specific fields and standard AWS field patterns (Name, Id, Arn)
- **Intelligent Response Processing**: Clean extraction of list data, ignoring metadata
- **Tabular Output**: Customizable column display with automatic filtering
- **Pagination Support**: Handles large AWS responses automatically
- **Region/Profile Support**: AWS CLI-compatible `--region` and `--profile` arguments for session management
- **Tag Transformation**: Automatic conversion of AWS Tags list to key-value pairs for better readability
- **Default Column Filters**: Configuration-based default columns for common AWS queries
- **Parameter Passing**: Direct parameter passing to AWS APIs with `-p`/`--parameter` for advanced use cases
- **Hint-Based Resolution**: Function selection hints with `-i`/`--input` for multi-step calls, including field extraction targeting

## Installation

### Via pip (Recommended)

```bash
pip install awsquery
```

### Development Installation

```bash
git clone https://github.com/yourusername/awsquery.git
cd awsquery
pip install -e ".[dev]"
```

### Enable Shell Autocomplete

awsquery supports tab completion for AWS services and actions through argcomplete.

#### Setup

##### Bash
```bash
# Add to ~/.bashrc or ~/.bash_profile
eval "$(register-python-argcomplete awsquery)"
```

##### Zsh
```bash
# Add to ~/.zshrc
autoload -U bashcompinit && bashcompinit
eval "$(register-python-argcomplete awsquery)"
```

##### Fish
```bash
# Add to ~/.config/fish/config.fish
register-python-argcomplete --shell fish awsquery | source
```

After adding the appropriate line to your shell configuration, restart your shell or source the file:
```bash
source ~/.bashrc  # or ~/.zshrc, etc.
```

Now you can use enhanced tab completion with smart matching:
```bash
awsquery <TAB>              # Shows available services
awsquery ec2 <TAB>          # Shows available ec2 actions
awsquery s3 list-<TAB>      # Shows s3 list actions
awsquery ec2 desc-inst<TAB> # Smart completion: "desc-inst" matches "describe-instances"
awsquery cloudformation des-sta<TAB> # Matches "describe-stacks"
```

The autocomplete system now features:
- **Split matching**: "desc-inst" matches "describe-instances"
- **Prefix priority**: Exact prefix matches are prioritized over substring matches
- **Security filtering**: Only shows ReadOnly operations

## Usage

### Basic Query
```bash
# Query EC2 instances with filtering
awsquery ec2 describe-instances

# Filter by values (partial match, case-insensitive on ANY field)
awsquery ec2 describe-instances prod web

# Specify output columns (partial match, case-insensitive)
awsquery ec2 describe-instances prod -- Name State InstanceId

# List S3 buckets containing "backup" (matches if "backup" appears anywhere in any field)
awsquery s3 list-buckets backup

# JSON output format
awsquery -j s3 list-buckets
```

### Keys Discovery
```bash
# Show available fields/keys from an API response
awsquery -k ec2 describe-instances
awsquery --keys s3 list-buckets
```

### Discovery and Debug
```bash
# List available services
awsquery

# Debug mode for troubleshooting with enhanced DebugContext output
# Shows structured debug information with timestamps and execution flow
awsquery -d ec2 describe-instances
```

## Command Structure

```
awsquery [-j|--json] [-k|--keys] [-d|--debug] [-p PARAM] [-i HINT] [--region REGION] [--profile PROFILE] SERVICE ACTION [VALUE_FILTERS...] [-- TABLE_OUTPUT_FILTERS...]
```

- **SERVICE**: AWS service name (ec2, s3, iam, etc.)
- **ACTION**: Service action (describe-instances, list-buckets, etc.)
- **VALUE_FILTERS**: Space-separated filters - ALL must match, using case-insensitive partial matching on any field
- **TABLE_OUTPUT_FILTERS**: Column selection - partial, case-insensitive matching on column names
- **-j, --json**: Output results in JSON format instead of table
- **-k, --keys**: Show all available keys for the command
- **-d, --debug**: Enable debug output for troubleshooting
- **-p, --parameter PARAM**: Pass parameters directly to AWS API (key=value format)
- **-i, --input HINT**: Hint for multi-step function selection (e.g., "desc-clus" or "desc-clus:fieldname")
- **--region REGION**: AWS region to use for requests (e.g., us-west-2)
- **--profile PROFILE**: AWS profile to use from ~/.aws/credentials

## Security

- **ReadOnly Enforcement**: Only AWS ReadOnly operations are permitted
- **Input Sanitization**: Prevents injection attacks through parameter validation
- **Operation Validation**: All actions validated before execution
- **Wildcard Matching**: Supports AWS IAM wildcard patterns (e.g., `ec2:Describe*`)
- **Session Isolation**: Each profile/region maintains separate boto3 sessions
- **Security Testing**: Comprehensive test suite validates security constraints

## Examples

```bash
# Find instances with "prod" AND "web" in any field (partial match)
# e.g., matches "production-web-server", "web.prod.example.com"
awsquery ec2 describe-instances prod web

# Show only columns matching Name, State and InstanceId (partial match)
# e.g., "Name" matches "InstanceName", "Tags.Name", "SecurityGroupName"
awsquery ec2 describe-instances prod web -- Name State InstanceId

# Find S3 buckets with "backup" anywhere in the data
# e.g., matches "my-backup-bucket", "bucket-backup-2024", "backups"
awsquery s3 list-buckets backup

# Multi-level CloudFormation query with parameter resolution
# Filters: "prod" in stack data, columns containing "Created" or "StackName"
awsquery cloudformation describe-stack-events prod -- Created StackName

# Targeted field extraction with hint for multi-step calls
awsquery elbv2 describe-tags -i desc-clus:clusterarn prod

# Discover all available keys
awsquery -k ec2 describe-instances

# JSON output with filtering (partial column name matching)
awsquery -j ec2 describe-instances prod -- InstanceId State.Name

# Debug mode with enhanced output showing parameter resolution and API calls
awsquery -d cloudformation describe-stack-resources workers -- EKS

# Use specific AWS region
awsquery --region eu-west-1 ec2 describe-instances

# Use specific AWS profile
awsquery --profile production s3 list-buckets

# Combine region and profile
awsquery --region us-east-2 --profile dev ec2 describe-vpcs

# View transformed tags (partial match on column names)
# Shows any column containing "Tags.Name" or "Tags.Environment"
awsquery ec2 describe-instances -- Tags.Name Tags.Environment

# CloudTrail LookupEvents with complex parameter structures
# Filter events by event name with automatic type conversion
awsquery cloudtrail lookup-events -p LookupAttributes=AttributeKey=EventName,AttributeValue=ConsoleLogin

# Multiple CloudTrail attributes using semicolon separation
awsquery cloudtrail lookup-events -p LookupAttributes=AttributeKey=EventName,AttributeValue=AssumeRole;AttributeKey=Username,AttributeValue=admin

# CloudTrail with time range and resource type filtering
awsquery cloudtrail lookup-events -p StartTime=2024-01-01 -p EndTime=2024-01-31 -p LookupAttributes=AttributeKey=ResourceType,AttributeValue=AWS::S3::Bucket

### Advanced Parameter Passing

# Pass specific parameters to AWS API calls
awsquery ec2 describe-instances -p MaxResults=10
awsquery ec2 describe-instances -p InstanceIds=i-123,i-456 -p MaxResults=5

# Complex parameter structures for SSM with automatic type conversion
awsquery ssm describe-parameters -p ParameterFilters=Key=Name,Option=Contains,Values=Ubuntu,2024

# Multiple complex structures using semicolon separation
awsquery ssm describe-parameters -p ParameterFilters=Key=Name,Option=Contains,Values=Ubuntu;Key=Type,Option=Equal,Values=String

# Complex structures with nested arrays and type conversion
awsquery ec2 describe-instances -p Filters=Name=instance-state-name,Values=running,stopped;Name=tag:Environment,Values=prod,staging

### Hint-Based Multi-Step Resolution

# Use hints to guide automatic parameter resolution
# When describe-tags needs resource ARNs, hint at using describe-clusters
awsquery elbv2 describe-tags -i desc-clus prod

# CloudFormation stack resources with hint for stack selection
awsquery cloudformation describe-stack-resources -i desc-stacks production

# ECS service details with task definition hint
awsquery ecs describe-services -i desc-task web-service

# Field-specific extraction with function:field format
awsquery elbv2 describe-tags -i desc-clus:clusterarn prod  # Extract ClusterArn specifically
awsquery eks describe-fargate-profile -i desc-clus:rolearn  # Extract RoleArn instead of default
```

## Configuration

### AWS Credentials

Ensure AWS credentials are configured via:
- `~/.aws/credentials` (supports multiple profiles)
- Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
- IAM roles (if running on EC2/ECS/Lambda)
- AWS SSO profiles

### Default Filters Configuration

The tool uses `default_filters.yaml` to define default columns for common queries. This comprehensive configuration file (3000+ lines)
provides extensive pre-configured filters for dozens of AWS services, loaded from the package directory to provide you with standard
columns if you don't add any.

Example configuration:
```yaml
ec2:
  describe_instances:
    columns:
      - InstanceId
      - Tags.Name
      - State.Name
      - InstanceType
      - PrivateIpAddress

s3:
  list_buckets:
    columns:
      - Name
      - CreationDate
```

## Development

### Running Tests

```bash
# Install development dependencies
make install-dev

# Run all tests
make test

# Run tests with coverage
make coverage

# Run specific test categories
make test-unit
make test-integration
make test-critical  # Run all tests (comprehensive test suite)

# Code formatting and linting
make format
make format-check  # Check without modifying
make lint
make type-check    # Run mypy type checking
make security-check  # Run security analysis

# Mutation testing
make mutmut        # Run mutation tests
make mutmut-results # Show mutation test results
make mutmut-html   # Generate HTML mutation test report

# Pre-commit hooks
make pre-commit  # Run all pre-commit hooks

# Continuous Integration
make ci  # Run comprehensive CI pipeline (tests, linting, type-check, security)
```


### Docker Usage

```bash
# Build development container
make docker-build

# Open interactive shell
make shell

# Run tests in Docker
make test-in-docker

# Clean Docker artifacts
make docker-clean
```

### Development Workflow

```bash
# Watch tests (auto-run on file changes)
make watch-tests

# Build distribution packages
make build

# Clean build artifacts
make clean

# Publish to Test PyPI
make publish-test

# Publish to PyPI (production)
make publish

# Version management
make version  # Show current version
make release  # Create a new release with version bump
```

## Advanced Usage

### Filter Matching Behavior

All filters in awsquery use **case-insensitive matching** with optional anchoring:

#### Filter Operators
- `^` at the start: matches values that START WITH the pattern (prefix match)
  - Both `^` (U+005E) and `ˆ` (U+02C6) are supported for keyboard compatibility
- `$` at the end: matches values that END WITH the pattern (suffix match)
- `^...$`: matches values that EXACTLY equal the pattern (exact match)
- No operators: matches values that CONTAIN the pattern (partial match)

#### Value Filters (before `--`)
- Match against ANY field in the response data
- ALL specified filters must match (AND logic)
- Case-insensitive matching with optional anchoring

```bash
# "prod" matches: "production", "prod-server", "my-prod-app" (contains)
awsquery ec2 describe-instances prod

# "^prod" matches: "production", "prod-server" (starts with)
awsquery ec2 describe-instances ^prod

# "prod$" matches: "my-prod", "dev-prod" (ends with)
awsquery ec2 describe-instances prod$

# "^prod$" matches: only exactly "prod" (exact match)
awsquery ec2 describe-instances ^prod$

# Both filters must match (AND logic)
awsquery ec2 describe-instances ^prod web$
```

#### Column Filters (after `--`)
- Match against column/field names in the output
- Case-insensitive matching with optional anchoring
- Multiple columns can be specified

```bash
# "Instance" matches: "InstanceId", "InstanceType", "InstanceName" (contains)
awsquery ec2 describe-instances -- Instance

# "^Instance" matches: "InstanceId", "InstanceType" (starts with)
awsquery ec2 describe-instances -- ^Instance

# "Name$" matches: "InstanceName", "GroupName", "Tags.Name" (ends with)
awsquery ec2 describe-instances -- Name$

# "^State.Name$" matches: only exactly "State.Name" (exact match)
awsquery ec2 describe-instances -- ^State.Name$

# Multiple patterns
awsquery ec2 describe-instances -- ^Instance Name$ State
```

### Multi-Level API Calls

The tool automatically handles parameter resolution for nested API calls:

```bash
# Automatically fetches stack list, then events for matching stacks
awsquery cloudformation describe-stack-events production

# Three-level call: list stacks → get resources → filter results
awsquery cloudformation describe-stack-resources prod -- Lambda
```

### Parameter Passing (`-p`/`--parameter`)

Pass parameters directly to AWS API calls using the `-p` flag. This is useful for fine-tuning API behavior:

```bash
# Limit results for large responses
awsquery ec2 describe-instances -p MaxResults=20

# Filter specific resources by ID
awsquery ec2 describe-instances -p InstanceIds=i-1234567890abcdef0,i-0987654321fedcba0

# Multiple parameters (can use multiple -p flags)
awsquery elbv2 describe-load-balancers -p PageSize=10 -p Names=my-alb

# Complex parameter structures (for APIs like SSM)
awsquery ssm describe-parameters -p ParameterFilters=Key=Name,Option=Contains,Values=Ubuntu
```

**Parameter Format:**
- Simple: `Key=Value`
- Lists: `Key=Value1,Value2,Value3`
- Complex structures: Use semicolons to separate multiple objects (e.g., `Key1=Val1,Val2;Key2=Val3`)
- Type conversion: Numbers and booleans are automatically converted
- Nested structures: Comma-separated values within objects, semicolon-separated objects
- CloudTrail example: `LookupAttributes=AttributeKey=EventName,AttributeValue=Login;AttributeKey=Username,AttributeValue=admin`

### Hint-Based Resolution (`-i`/`--input`)

Guide multi-step parameter resolution with function hints:

```bash
# Basic function hint - guides which list operation to use
awsquery cloudformation describe-stack-resources -i list-sta production

# Field extraction hint - specify exact field to extract
awsquery elbv2 describe-tags -i desc-clus:clusterarn prod

# Override default field selection
awsquery eks describe-fargate-profile -i desc-clus:rolearn my-cluster
```

**Key Features:**
- **Smart matching**: "desc-inst" matches "describe-instances"
- **Field targeting**: Use `function:field` to extract specific fields
- **Automatic fallback**: Uses standard heuristics when no field specified

### Filtering Strategies

```bash
# All filters must match (AND logic), each using partial matching
# Finds instances where ALL three terms appear somewhere in the data
awsquery ec2 describe-instances production web database

# Column filters use partial, case-insensitive matching
# Shows columns containing "Instance", "State", or "Private" in their names
awsquery ec2 describe-instances -- Instance State Private

# Combine value and column filters
# Finds buckets with "backup" in any field, shows Name and Creation columns
awsquery s3 list-buckets backup -- Name Creation

# Partial matching examples:
# "prod" matches "production", "prod-server", "myproduct"
# "PROD" matches "production" (case-insensitive)
# "i-123" matches "i-1234567890abcdef0"
```

### Performance Tips

- Use specific filters to reduce API calls
- Column filters (`--`) don't affect API calls, only display
- Use `--region` to avoid cross-region latency
- Keys mode (`-k`) adds overhead; use only for discovery

## Troubleshooting

### Common Issues

**"No matching resources found"**
- Check your filters are not too restrictive
- Use debug mode (`-d`) to see actual API responses
- Verify you have permissions in the target region/account

**"Access Denied" errors**
- Ensure your AWS credentials have ReadOnly permissions
- Check if using the correct profile with `--profile`
- Verify the operation is permitted

**"Parameter validation failed"**
- Some APIs require specific parameters
- The tool attempts automatic resolution but may need manual input
- Use debug mode to see the parameter resolution process

**Performance issues**
- Large result sets may take time to process
- Use more specific filters to reduce data volume
- Consider using `--region` to target specific regions

## Requirements

The package dependencies are:

- boto3>=1.35.0
- botocore>=1.35.0
- tabulate>=0.9.0
- argcomplete>=3.0.0
- PyYAML>=6.0.0

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please ensure tests pass and follow the existing code style.
