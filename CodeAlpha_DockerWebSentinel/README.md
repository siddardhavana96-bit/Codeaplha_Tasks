# WebSentinel | Observable Docker Web Server

> A deliberately small static web server that shows the operational details recruiters expect: multi-stage image creation, a non-root Nginx runtime, health checks, structured access logs, a metrics endpoint, and a one-command smoke test.

## Run

```bash
docker compose up --build -d
curl http://localhost:8088/healthz
curl http://localhost:8088/metrics
./scripts/smoke-test.sh       # PowerShell: bash scripts/smoke-test.sh
```

The public landing page is at `http://localhost:8088`.

## The operational story

| Concern | Implementation |
| --- | --- |
| Small image | multi-stage build copies only static assets into Nginx |
| Runtime privilege | Nginx is configured to listen on 8080 as non-root |
| Health | Docker `HEALTHCHECK` calls `/healthz` |
| Observability | JSON access logs and an Nginx stub-status metrics endpoint |
| Troubleshooting | `make logs`, `make status`, and a deterministic smoke test |
| Safety | read-only filesystem, dropped Linux capabilities, no-new-privileges |

## Demonstrate lifecycle management

```bash
make up       # build and start
make status   # container health
make logs     # inspect JSON access logs
make smoke    # check page, health, and metrics
make down     # clean shutdown
```

## Screenshots worth adding to your GitHub README

1. Landing page in browser.
2. `docker compose ps` showing **healthy**.
3. `make smoke` output.
4. A single JSON access-log line.

That is stronger evidence than a Dockerfile alone: it shows you understand build, run, observe, and validate.
