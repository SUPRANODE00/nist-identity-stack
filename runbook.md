# Telemetry Stack Operational Runbook
## Configuration Overview
The telemetry stack components run via Docker Compose or manual GitHub Actions triggers. Secrets are dynamically fed into worker runtime environments.
### Environment Injection
Local secrets injection relies on `.env`:
cp .env.example .env
### Local Runtime Deployment
docker compose up --build -d
### CI Dispatch
Workflows are bound to `workflow_dispatch`. Ensure repository secrets `MQTT_USER` and `MQTT_PASS` are defined in the repository settings prior to running manual triggers.
