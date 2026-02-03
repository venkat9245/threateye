#!/bin/bash
cd ~/ThreatEye

# Activate venv
source venv/bin/activate

# Direct Python (bypasses Flask CLI issues)
echo "🚀 Starting ThreatEye..."
python3 api.py
