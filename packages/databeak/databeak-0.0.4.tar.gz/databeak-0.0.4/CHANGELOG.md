# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.4] - 2025-09-30

### Added

- **Relaxed JSON Schema Validation**: Custom jsonschema validator that accepts
  integers as strings or floats, handling LLM-generated parameters that don't
  strictly conform to integer types (PR #115)
- **Integration Testing Framework**: Comprehensive integration testing with
  pytest configuration, isolated test environment, and coverage reporting (PR #110)
- **ReadTheDocs Configuration**: Official documentation site with MkDocs
  integration and automated deployment (PR #108)
- **Type Safety Enhancements**: MCP-specific type definitions including
  NonNegativeIntString and PositiveIntString with regex validation (PR #111)

### Changed

- **Header Type Architecture**: Refactored HeaderConfig to use Abstract Base
  Class with Pydantic discriminated union pattern for cleaner polymorphic
  behavior (PR #113)
- **FastMCP Dependency**: Updated to use released fastmcp version instead of
  development branch (PR #114)
- **Testing Configuration**: Enhanced pytest configuration with integration test
  markers, coverage settings, and proper test isolation
- **Project Structure**: Streamlined documentation and removed unmaintained
  agent files and Docker infrastructure (PR #116)

### Removed

- **Docker Support**: Removed Dockerfile and docker-compose.yml as Docker
  deployment is not officially supported
- **Agent Documentation**: Removed specialized agent documentation files that
  are no longer actively maintained

## [0.0.3] - 2025-01-24

### Fixed

- **Circular Import Resolution**: Resolved critical circular import between
  `session.py` and `session_service.py` using lazy imports and TYPE_CHECKING
  blocks
- **Import Architecture**: Converted all relative imports to absolute imports,
  eliminating 15 TID252 ruff violations
- **MyPy Configuration**: Added `mypy_path="src"` to enable type checking from
  project root and pre-commit compatibility
- **Documentation Consistency**: Updated all documentation to use standardized
  `uv run mypy src/databeak/` command syntax

### Changed

- **Agent Documentation**: Streamlined test-coverage-analyzer agent description
  to focus on prescriptive guidance rather than current state information
- **Quality Pipeline**: Pre-commit hooks now pass completely with proper MyPy
  integration

## [0.0.2] - 2025-01-19

### Added

- **Production Quality Standards**: Achieved zero ruff violations across all
  code quality categories
- **Enhanced Type Safety**: 100% mypy compliance with comprehensive type
  annotations
- **Context-Based Logging**: MCP-integrated logging for better traceability in
  tool functions
- **API Design Improvements**: Keyword-only boolean parameters to eliminate
  boolean traps
- **Data Validation**: Added proper validation constraints (e.g., negative value
  prevention)
- **Comprehensive Test Coverage**: 1100+ unit tests with excellent coverage
- **Logging Guidelines**: Clear documentation for Context vs standard logger
  usage

### Changed

- **Architecture Simplification**: Removed CorrelatedLogger, simplified to
  standard Python logging
- **Server Composition**: Enhanced modular FastMCP server architecture
- **Exception Handling**: Consistent exception message patterns with variable
  extraction
- **Parameter Naming**: Resolved variable shadowing (format → export_format)
- **Test Structure**: Improved pytest patterns with proper exception testing
- **Documentation**: Updated all docs to reflect current architecture and
  quality standards

### Fixed

- **Security**: Eliminated silent exception handling (try-except-pass patterns)
- **Code Consistency**: Fixed variable shadowing violations throughout codebase
- **Test Quality**: Proper pytest.raises usage with specific match parameters
- **Error Messages**: Extracted all exception messages to variables for
  maintainability
- **Import Organization**: Cleaned up unused imports and dependencies

### Removed

- **Code Violations**: Eliminated all ruff violations (G004, FBT, EM, PT, A,
  ARG, S110, N818)
- **Boolean Traps**: Removed confusing boolean positional parameters
- **Custom Logging Complexity**: Simplified logging architecture
- **Duplicate Code**: Consolidated AutoSaveConfig implementations
- **Outdated Documentation**: Updated all references to current architecture

## [0.0.1] - 2025-09-18

### Added

- Initial release of DataBeak MCP Server
- Core CSV operations: read, write, filter, transform
- Data validation and quality checks
- Statistical analysis and profiling capabilities
- Outlier detection and handling
- Support for multiple file formats (CSV, Excel, Parquet)
- Async operations for high performance
- Comprehensive error handling and logging
- FastMCP integration for seamless AI assistant integration
- Pandas-powered data manipulation
- Full test coverage with pytest
- Documentation with examples
- Type hints and mypy compatibility

[0.0.1]: https://github.com/jonpspri/databeak/releases/tag/v0.0.1
[0.0.2]: https://github.com/jonpspri/databeak/releases/tag/v0.0.2
[0.0.3]: https://github.com/jonpspri/databeak/releases/tag/v0.0.3
[0.0.4]: https://github.com/jonpspri/databeak/releases/tag/v0.0.4
