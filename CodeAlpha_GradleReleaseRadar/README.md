# ReleaseRadar | Gradle Quality-Gated Java Service

> A small Java 21 HTTP service that turns build and release metadata into a human-readable status endpoint. Its Gradle workflow demonstrates dependency locking, tests, code-quality reporting, container packaging, and CI publication.

## Design choices that matter

This is intentionally not a generated Spring project. The service uses JDK `HttpServer`, keeping the application understandable while the delivery system shows modern Gradle practice: a reproducible toolchain, locked dependencies, JUnit tests, JaCoCo coverage, and a GitHub Actions release gate.

## Run it

```bash
./gradlew test jacocoTestReport run
# Windows: .\\gradlew.bat test jacocoTestReport run
curl http://localhost:8080/healthz
```

## CI/CD lifecycle

```
push -> Gradle test -> coverage report -> build JAR -> build/push container on main
```

The workflow only pushes if repository secrets `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` are configured. Without them, validation still runs on every pull request.

## Interview-ready talking points

- Dependency versions are centralised in `gradle/libs.versions.toml`.
- Java 21 toolchain removes "works on my machine" differences.
- Unit tests cover the response policy without needing a running server.
- The container is non-root and has a health check.
- GitHub Actions separates validation from the release-only image push.
