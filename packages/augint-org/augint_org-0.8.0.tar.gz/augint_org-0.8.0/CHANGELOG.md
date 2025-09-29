# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- version list -->

## v0.8.0 (2025-09-28)

### Features

- Disable CLI account creation; add DNS delegation StackSet
  ([`4e9ac54`](https://github.com/Augmenting-Integrations/aillc-org/commit/4e9ac544b786759ae90d4c7f3092770838665d9c))


## v0.7.1 (2025-09-23)

### Refactoring

- Replace SSO email references with username-based logic and enhance identity store integration
  ([`5bee09e`](https://github.com/Augmenting-Integrations/aillc-org/commit/5bee09e12aeb81dff7e5cc27becdb22dee614a58))


## v0.7.0 (2025-09-23)


## v0.6.0 (2025-09-23)


## v0.5.0 (2025-09-23)

### Features

- Add SSO user listing script and enhance identity filter logic
  ([`02b8e36`](https://github.com/Augmenting-Integrations/aillc-org/commit/02b8e368572966ac1b5d4914b0aed9b32802eb2a))


## v0.4.0 (2025-09-23)


## v0.3.0 (2025-09-23)

### Features

- Add StackSet operations and improve deployment workflow
  ([`d61059d`](https://github.com/Augmenting-Integrations/aillc-org/commit/d61059d22dd4c3227543594660a677a82d65da5e))


## v0.2.2 (2025-09-21)

### Bug Fixes

- Add test paths to workflow triggers and fix mock patch location
  ([`ad37cb1`](https://github.com/Augmenting-Integrations/aillc-org/commit/ad37cb1a5f212ffe6de75b9f9fb09873fb1aeb3f))

- Fix test_config_list_permission_sets mock to prevent real AWS calls
  ([`208b44a`](https://github.com/Augmenting-Integrations/aillc-org/commit/208b44aa2b41e396e94cbd9901a912f0f7b498e5))

### Documentation

- Rewrite README with focus on ai-org CLI usage
  ([`f3db038`](https://github.com/Augmenting-Integrations/aillc-org/commit/f3db038e893791758bf242b7a88cbd4d558deac7))


## v0.2.1 (2025-09-20)


## v0.2.0 (2025-09-20)


## v0.1.2 (2025-09-20)


## v0.1.1 (2025-09-20)


## v0.1.0 (2025-09-20)

- Initial Release

## [Unreleased]

### Added
- Initial implementation of augint-org CLI tool
- Account management commands (create, list, get)
- SSO permission management commands
- StackSet deployment commands
- Configuration management commands
- Comprehensive CI/CD pipeline with GitHub Actions
- Unit and integration test suite
- Semantic versioning with Python Semantic Release
- Documentation generation with pdoc
- Pre-commit hooks for code quality
