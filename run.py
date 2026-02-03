#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
os.chdir('/root/ThreatEye')  # Adjust path
print("🌐 Serving ThreatEye on http://0.0.0.0:8080")
HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler).serve_forever()
