import os
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="DeliveryPulse", version=os.getenv("APP_VERSION", "dev"))
started_at = datetime.now(timezone.utc).isoformat()

@app.get("/healthz")
def health():
    return {"status": "ok", "version": app.version, "started_at": started_at}

@app.get("/", response_class=HTMLResponse)
def home():
    return f'''<!doctype html><html><head><title>DeliveryPulse</title><style>body{{font:16px system-ui;background:#09121f;color:#edf5ff;display:grid;place-items:center;height:90vh}}main{{max-width:620px;padding:38px;border:1px solid #254567;border-radius:18px;background:#0e1d30}}.ok{{color:#55e6a5}}code{{background:#152b45;padding:3px 6px;border-radius:5px}}</style></head><body><main><p class="ok">● release healthy</p><h1>DeliveryPulse</h1><p>Azure delivery telemetry, made visible.</p><p>Running <code>{app.version}</code></p><p>Started {started_at}</p><p><a href="/healthz" style="color:#8fc7ff">Inspect health JSON →</a></p></main></body></html>'''
