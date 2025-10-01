# AI LLS Library

Core business logic library and CLI tools for Landline Scrubber - phone verification and DNC checking.

## Version 2.1.0 - Streaming & Provider Architecture

New features:
- **Streaming support** for large CSV files to reduce memory usage
- **Provider architecture** for clean separation of verification logic
- **Contract tests** ensuring all providers behave consistently

## Version 2.0.0 - Breaking Changes

This is a greenfield rewrite with no backwards compatibility:
- All file-based CSV processing replaced with text-based methods
- Removed `_sync` suffix from all methods (everything is sync)
- `process_csv_sync(file_path)` → `process_csv(csv_text)`
- `generate_results_csv(...)` now returns CSV string instead of writing to file

## Features

- Phone number normalization (E.164 format)
- Line type detection (mobile/landline/voip)
- DNC (Do Not Call) list checking
- DynamoDB caching with 30-day TTL
- Bulk CSV processing
- Infrastructure-aware CLI for admin operations
- AWS Lambda PowerTools integration

## Installation

```bash
# Install library with Poetry
poetry install

# Install CLI globally
pip install -e .
```

## Library Usage

### Single Phone Verification

```python
from ai_lls_lib import PhoneVerifier, DynamoDBCache

cache = DynamoDBCache(table_name="phone-cache")
verifier = PhoneVerifier(cache)

result = verifier.verify("+15551234567")
print(f"Line type: {result.line_type}")
print(f"DNC: {result.dnc}")
print(f"From cache: {result.cached}")
```

### Bulk Processing

```python
from ai_lls_lib import BulkProcessor, PhoneVerifier, DynamoDBCache

cache = DynamoDBCache(table_name="phone-cache")
verifier = PhoneVerifier(cache)
processor = BulkProcessor(verifier)

# Process CSV text content
csv_text = "name,phone\nJohn,+15551234567\nJane,+15551234568"
results = processor.process_csv(csv_text)

# Generate results CSV
results_csv = processor.generate_results_csv(csv_text, results)
print(results_csv)  # CSV string with added line_type, dnc, cached columns
```

### Streaming Large Files

For memory-efficient processing of large CSV files:

```python
from ai_lls_lib import BulkProcessor, PhoneVerifier, DynamoDBCache

cache = DynamoDBCache(table_name="phone-cache")
verifier = PhoneVerifier(cache)
processor = BulkProcessor(verifier)

# Process CSV as a stream, yielding batches
csv_lines = open('large_file.csv').readlines()
for batch in processor.process_csv_stream(csv_lines, batch_size=100):
    print(f"Processed batch of {len(batch)} phones")
    # Each batch is a list of PhoneVerification objects
```

### Custom Verification Providers

Use different verification providers based on your needs:

```python
from ai_lls_lib import PhoneVerifier, DynamoDBCache
from ai_lls_lib.providers import StubProvider

# Use stub provider for testing
cache = DynamoDBCache(table_name="phone-cache")
provider = StubProvider()  # Deterministic testing provider
verifier = PhoneVerifier(cache, provider=provider)

# When external APIs are ready, switch to:
# from ai_lls_lib.providers.external import ExternalAPIProvider
# provider = ExternalAPIProvider(phone_api_key="...", dnc_api_key="...")
```

## CLI Usage

The `ai-lls` CLI provides infrastructure-aware administrative tools:

### Verification Commands
```bash
# Verify single phone
ai-lls verify phone +15551234567 --stack landline-api

# Bulk verify CSV
ai-lls verify bulk input.csv -o output.csv --stack landline-api
```

### Cache Management
```bash
# Show cache statistics
ai-lls cache stats --stack landline-api

# Get cached entry
ai-lls cache get +15551234567 --stack landline-api

# Invalidate cache entry
ai-lls cache invalidate +15551234567 --stack landline-api

# Clear old entries
ai-lls cache clear --older-than 20 --stack landline-api
```

### Administrative Commands
```bash
# Manage user credits
ai-lls admin user-credits user123 --add 100
ai-lls admin user-credits user123 --set 500

# List API keys
ai-lls admin api-keys --user user123

# Check queue status
ai-lls admin queue-stats

# View secrets (masked)
ai-lls admin secrets --stack landline-api
```

### Test Stack Management
```bash
# Deploy test stack
ai-lls test-stack deploy

# Check status
ai-lls test-stack status

# Run integration tests
ai-lls test-stack test

# Delete test stack
ai-lls test-stack delete
```

## Project Structure

```
ai-lls-lib/
├── src/ai_lls_lib/
│   ├── core/           # Business logic (infrastructure-agnostic)
│   │   ├── models.py   # Pydantic models
│   │   ├── verifier.py # Phone verification
│   │   ├── processor.py # Bulk processing
│   │   └── cache.py    # DynamoDB cache
│   ├── cli/            # Infrastructure-aware CLI
│   │   ├── __main__.py # Entry point
│   │   ├── commands/   # Command modules
│   │   └── aws_client.py # AWS operations
│   └── testing/        # Test utilities
│       └── fixtures.py # Test data
├── tests/
│   ├── unit/          # Mocked tests
│   └── integration/   # AWS integration tests
└── test-stack.yaml    # Test infrastructure
```

## Testing

```bash
# Run unit tests (mocked AWS)
poetry run pytest tests/unit -v

# Deploy test stack for integration tests
ai-lls test-stack deploy

# Run integration tests (requires test stack)
TEST_STACK_NAME=ai-lls-lib-test poetry run pytest tests/integration -v

# All tests with coverage
poetry run pytest --cov=src --cov-report=html

# Clean up
ai-lls test-stack delete
```

## Development

### Current Stub Implementation

For demo purposes, verification uses stub logic based on last digit:
- Ends in 3: mobile, not on DNC
- Ends in 2: landline, not on DNC
- Ends in 1: mobile, on DNC
- Ends in 0: landline, on DNC
- Otherwise: mobile, not on DNC

TODO markers indicate where real API integration will be added.

### Code Quality

```bash
# Format code
poetry run black src/ tests/
poetry run isort src/ tests/

# Type checking
poetry run mypy src/

# Run pre-commit hooks
pre-commit run --all-files
```

## Environment Variables

- `DNC_API_KEY` - DNC verification API key
- `DNC_CHECK_API_KEY` - Alternative DNC service
- `PHONE_VERIFY_API_KEY` - Line type verification
- `AWS_REGION` - AWS region (default: us-east-1)
- `AWS_PROFILE` - AWS profile for CLI operations

## License

Proprietary - All rights reserved

## Release Process

This library uses semantic versioning and publishes to:
- TestPyPI on dev branch pushes (pre-release versions)
- PyPI on main branch pushes (stable releases)
