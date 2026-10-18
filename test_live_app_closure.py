# -*- coding: utf-8 -*-
"""
Automated unit verification for 06_LiveApp endpoint
"""

import threading
import time
import urllib.request
import json
from http.server import HTTPServer
try:
    from .live_app import VisionNexusHandler, HOST, PORT
except ImportError:
    from live_app import VisionNexusHandler, HOST, PORT

def test_live_app_healthz():
    server = HTTPServer((HOST, PORT + 10), VisionNexusHandler)
    t = threading.Thread(target=server.serve_forever, daemon=True)
    t.start()
    time.sleep(0.5)

    try:
        url = f"http://{HOST}:{PORT + 10}/healthz"
        with urllib.request.urlopen(url, timeout=3) as resp:
            assert resp.status == 200
            data = json.loads(resp.read().decode("utf-8"))
            assert data["status"] == "HEALTHY"
            assert "OpenCV" in data["service"]
            assert data["zdr_status"] == "CLEARED (0.000000 MB)"
    finally:
        server.shutdown()
