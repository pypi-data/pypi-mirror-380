## v0.5.0 (2025-09-27)

### Feat

- add list databases command to show available PostgreSQL databases

## v0.4.0 (2025-09-28)

### Feat

- update Docker image dependency from lafayettegabe/wald to jstet/wald
- initial release of duplicaid CLI tool

### Fix

- simplify release workflow condition
- resolve black/ruff formatting conflict
- **workflow**: handle existing tags in release process
- **executor**: resolve container name mapping in LocalExecutor methods
- **executor**: resolve container name mapping in LocalExecutor methods (#2)
- update uv version in workflow
- resolve all test failures for CI pipeline
- resolve test failures in CI workflow
- configure Git identity for automated releases
- add --yes flag to commitizen commands for CI
- add OIDC permissions and fix build step logic
- workflow dependency issue preventing releases

### Refactor

- remove redundant container name mapping method (#3)
