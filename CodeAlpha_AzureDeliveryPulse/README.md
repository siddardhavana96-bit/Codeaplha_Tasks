# DeliveryPulse | Azure CI/CD Reference Platform

> A production-minded delivery pipeline for a small FastAPI service. It builds a trusted container image, publishes it to Azure Container Registry, deploys to Azure App Service, and verifies the live release.

## Why this stands out

DeliveryPulse turns a basic "push to deploy" exercise into an observable release workflow: immutable image tags, a provenance label, endpoint tests, dependency scanning, a deployment gate, and a post-deploy smoke test. The app itself exposes a release card so a reviewer can see which commit is running.

```
GitHub push -> test + scan -> ACR -> App Service deployment -> /healthz smoke test
```

## Local run

```bash
docker compose up --build
# open http://localhost:8000 and http://localhost:8000/healthz
```

To run the release contract tests outside Docker, use `pip install -r requirements-dev.txt` followed by `python -m unittest discover -s tests -v`.

## Azure setup

1. Create an Azure Container Registry and a Linux Web App configured for containers.
2. In Azure DevOps, create an Azure Resource Manager service connection named `azure-production`.
3. Create a Docker Registry service connection named `acr-production` for your ACR.
4. Edit `azure-pipelines.yml` variables (`azureServiceConnection`, `acrName`, `webAppName`, `resourceGroup`).
5. Create a pipeline from this repository and run it from `main`.

The pipeline deploys a commit-SHA image tag, so rollback is a one-line variable change rather than a rebuild.

## Repository map

- `src/` - application and health endpoints
- `tests/` - release-health contract tests run by the pipeline
- `azure-pipelines.yml` - test, scan, build, publish, deploy, verify
- `infra/` - repeatable Azure CLI provisioning commands
- `docker-compose.yml` - zero-friction local demonstration

## Evidence to capture for a submission

- Azure Pipelines successful run with the Verify stage.
- ACR repository showing the commit-SHA tag.
- App Service URL showing the release card.
- `/healthz` response after deployment.

## Security notes

No cloud credentials live in this repository. Store service connections and registry credentials in Azure DevOps, use least-privilege RBAC, and replace the sample resource names before deploying.
