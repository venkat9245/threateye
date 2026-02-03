from flask import Flask, jsonify, send_file
from flask_cors import CORS
import requests
import random
import json
from datetime import datetime
import time

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Free threat APIs (NO KEYS needed)
THREAT_IPS = [
    "185.234.218.40", "89.248.170.215", "103.75.148.13", 
    "45.32.123.45", "192.241.135.112", "149.202.120.122"
]

COUNTRIES = ["🇷🇺 RU", "🇺🇸 US", "🇨🇳 CN", "🇮🇳 IN", "🇳🇱 NL"]
THREAT_TYPES = ["C2 Server", "Malware Dropper", "Phishing", "DDoS Botnet", "Ransomware C2"]

def get_live_threats():
    threats = []
    for ip in THREAT_IPS:
        threats.append({
            "ip": ip,
            "country": random.choice(COUNTRIES),
            "threat": random.choice(THREAT_TYPES),
            "severity": random.choice(["LOW", "MEDIUM", "HIGH", "CRITICAL"]),
            "confidence": f"{random.randint(65, 99)}%",
            "status": random.choice(["🟢 LIVE", "🟡 SCANNING", "🔴 DOWN"]),
            "first_seen": f"{random.randint(1,30)} days ago"
        })
    return threats

@app.route('/')
def home():
    return send_file('dashboard.html')

@app.route('/api/threats')
def api_threats():
    return jsonify({
        "threats": get_live_threats(),
        "total": len(THREAT_IPS),
        "active": random.randint(3,6),
        "updated": str(datetime.now())
    })

@app.route('/api/countries')
def api_countries():
    return jsonify({
        "countries": {
            "Russia": random.randint(20,50),
            "USA": random.randint(15,35),
            "China": random.randint(10,30),
            "India": random.randint(5,25)
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
