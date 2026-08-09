#!/usr/bin/env sh
set -eu
base="${BASE_URL:-http://localhost:8088}"
curl --fail --silent "$base/" >/dev/null
health="$(curl --fail --silent "$base/healthz")"
echo "$health" | grep -q '"status":"ok"'
echo "PASS: page and health endpoint respond correctly"
