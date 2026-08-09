# RemoteMesh | Secure Jenkins Remoting Lab

> A self-contained Jenkins controller/agent topology that demonstrates labeled remote execution, ephemeral build agents, isolated Docker networks, and a reproducible verification job.

## What a reviewer can see

Instead of a single Jenkins container, RemoteMesh models a tiny build fleet. The controller only exposes the UI; the agent runs builds under the `linux-amd64` label. The pipeline proves where it executed and publishes a small build attestation.

```
Browser -> Jenkins controller :8080
                    | private `jenkins_mesh` network
                    +-> inbound Linux agent (label: linux-amd64)
```

## Start the lab

```bash
docker compose up --build -d
docker compose logs -f jenkins
```

Open `http://localhost:8080`. Retrieve the first-run unlock key with:

```bash
docker compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

In Jenkins: create an **inbound agent** named `mesh-agent`, set remote root to `/home/jenkins/agent`, label it `linux-amd64`, and copy its secret into a local `.env` file from `.env.example`. Then run `docker compose up -d agent`.

## Pipeline behavior

`Jenkinsfile` deliberately requests `linux-amd64`, checks the runtime, produces `build-attestation.json`, and archives it. A scheduler can be added safely through Jenkins UI after the first successful manual run.

## Operational hardening demonstrated

- Controller/agent traffic stays on a dedicated internal network.
- Agent runs as non-root and has no Docker socket mounted.
- Secrets stay in Jenkins credentials or ignored `.env`, never in the Git history.
- Workspaces are cleaned after every run.
- Controller persistence is isolated in a named Docker volume.

## Submission evidence

Capture the Jenkins node page showing `mesh-agent` online, a completed pipeline log showing its node label, and the archived attestation. These three images make the remoting design easy to defend in an interview.
