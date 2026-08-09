#!/usr/bin/env bash
set -euo pipefail
# Set these before running. Azure DevOps service connections should use least privilege.
RG="${RG:?set RG}"; LOCATION="${LOCATION:-centralindia}"; ACR="${ACR:?set ACR}"; PLAN="${PLAN:?set PLAN}"; APP="${APP:?set APP}"
az group create -n "$RG" -l "$LOCATION"
az acr create -g "$RG" -n "$ACR" --sku Basic --admin-enabled false
az appservice plan create -g "$RG" -n "$PLAN" --is-linux --sku B1
az webapp create -g "$RG" -p "$PLAN" -n "$APP" --deployment-container-image-name "mcr.microsoft.com/azuredocs/aci-helloworld"
echo "Provisioned. Grant the web app managed identity AcrPull on the registry before deploying."
