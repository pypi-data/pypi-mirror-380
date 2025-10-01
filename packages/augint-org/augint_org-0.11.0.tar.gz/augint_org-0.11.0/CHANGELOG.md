# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- version list -->

## v0.11.0 (2025-09-30)

### Features

- Add API Gateway logging configuration and CloudWatch permissions
  ([`d9c85df`](https://github.com/Augmenting-Integrations/aillc-org/commit/d9c85df5d857a7564f7072c18a544c62f9ca2119))


## v0.10.0 (2025-09-30)

### Bug Fixes

- Add script to fix manual StackSets permission model
  ([`b9001b8`](https://github.com/Augmenting-Integrations/aillc-org/commit/b9001b8874054b9c55b92a0dfb12084fb5fe7b8f))

- Correct DeploymentTargets parameter in DNS delegation
  ([`17f5443`](https://github.com/Augmenting-Integrations/aillc-org/commit/17f5443b47fc08bf4cea2537589828c8e49cb9c2))

- Deploy SERVICE_MANAGED StackSets to parent OU with account filtering
  ([`f79c6c2`](https://github.com/Augmenting-Integrations/aillc-org/commit/f79c6c268c2616245b3c01c9955a43b32f39e436))

- DNS delegation deployment to work with SERVICE_MANAGED StackSets
  ([`45c65c5`](https://github.com/Augmenting-Integrations/aillc-org/commit/45c65c5197a8b5a6b67ecf11ee0dbc722de94538))

- Include integration tests in CI pipeline to meet coverage requirements
  ([`4636b81`](https://github.com/Augmenting-Integrations/aillc-org/commit/4636b81c53b61d9bfefbec4ef16bd1f59ae08733))

- Make version dynamic and fix ACM stackset example
  ([`bde217e`](https://github.com/Augmenting-Integrations/aillc-org/commit/bde217e920159a83661c855960994745a2410d9f))

- Set manual-deploy StackSets to SELF_MANAGED permission model
  ([`b8197f4`](https://github.com/Augmenting-Integrations/aillc-org/commit/b8197f44827a0663cc46783fd714ff90a52e1a62))

- Simplify ACM certificate template to avoid DNS validation conflicts
  ([`238a09e`](https://github.com/Augmenting-Integrations/aillc-org/commit/238a09e1acc5d03e6716071de2dffb49e4d64ebb))

- Simplify zone discovery to only search in target account
  ([`476ce70`](https://github.com/Augmenting-Integrations/aillc-org/commit/476ce705d1f844cceb4bcacd7892bb1b888af9f6))

- Use SERVICE_MANAGED for all org-* StackSets with proper OU filtering
  ([`34413ff`](https://github.com/Augmenting-Integrations/aillc-org/commit/34413ff71b638b7048b99dbb8ef30c2dafd4cef2))

- Use single DomainValidationOption for apex+wildcard certificate
  ([`89590f3`](https://github.com/Augmenting-Integrations/aillc-org/commit/89590f350ebd9192b32e9dd342a4212f231fed75))

- Zone discovery now searches in target account for ACM certificates
  ([`67438ce`](https://github.com/Augmenting-Integrations/aillc-org/commit/67438cee09d87c2bbf6ea2f1ad431f357559ffbf))

### Features

- Add ACM certificate automation and improve StackSet commands
  ([`7455717`](https://github.com/Augmenting-Integrations/aillc-org/commit/74557171a459d96b0721fffd2c9e93577af250ae))

- Add human-friendly static export names to StackSets
  ([`055db1a`](https://github.com/Augmenting-Integrations/aillc-org/commit/055db1abb84acad00bc6d807c95762630b491380))

- Smart region defaults for ACM certificate deployment
  ([`1a3ffc5`](https://github.com/Augmenting-Integrations/aillc-org/commit/1a3ffc52341cd7bce4577928cb59e48898366b19))

### Refactoring

- Simplify ACM certificate pattern to use base domain
  ([`fb1e4f1`](https://github.com/Augmenting-Integrations/aillc-org/commit/fb1e4f116329e5bc003cdadd861909110bc41ed8))


## v0.9.0 (2025-09-29)

### Bug Fixes

- Convert MonitorSpecification to JSON string format
  ([`75069ea`](https://github.com/Augmenting-Integrations/aillc-org/commit/75069eabb411e90c272e09053e0fe0b40c7121c0))

- Correct AWS::CE::AnomalyMonitor configuration for linked account monitoring
  ([`4a4912b`](https://github.com/Augmenting-Integrations/aillc-org/commit/4a4912b9dec5b41b6119e782ecb0d9282df30205))

- Remove AnomalyThreshold parameter from deployment script
  ([`0018812`](https://github.com/Augmenting-Integrations/aillc-org/commit/001881253b64b412f9a9b84790ce14f3c306049c))

- Remove MonitorSpecification from DIMENSIONAL ServiceAnomalyDetector
  ([`f258e88`](https://github.com/Augmenting-Integrations/aillc-org/commit/f258e885203e30a330c8fadf364200cc6cbaab7d))

- Separate SNS subscription from topic definition
  ([`b843df1`](https://github.com/Augmenting-Integrations/aillc-org/commit/b843df1b2967f3c504b165c7ebb400d7bc129978))

- Separate SNS Subscription from Topic resource
  ([`6febf99`](https://github.com/Augmenting-Integrations/aillc-org/commit/6febf9947aaa13e61c973c7f060544a3aef2888e))

- Simplify cost management template by removing broken anomaly detection
  ([`90eaf27`](https://github.com/Augmenting-Integrations/aillc-org/commit/90eaf27f9f7ad24e385c6bcda55130f14451c08f))

### Features

- Refactor StackSet deployment with registry-based architecture
  ([`68985e7`](https://github.com/Augmenting-Integrations/aillc-org/commit/68985e753e30be95394a4603f792b329f5d63954))

- Restore anomaly detection with fixes now that Cost Explorer is enabled
  ([`bde64d2`](https://github.com/Augmenting-Integrations/aillc-org/commit/bde64d22f55df3ab4bd389aef1ffd9e99e02d5fd))

### Breaking Changes

- Replaces hardcoded StackSet deployment with centralized registry pattern


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
