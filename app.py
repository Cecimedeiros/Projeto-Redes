from flask import Flask, render_template, jsonify
import threading
import time
import random
from datetime import datetime
from datetime import timezone 

app = Flask(__name__)


SERVICES = {
    "web-api": {"uptime_pct": 100.0, "latency_ms": 20.0, "up": True, "last_checked": None},
    "database": {"uptime_pct": 100.0, "latency_ms": 8.0, "up": True, "last_checked": None},
    "cache": {"uptime_pct": 100.0, "latency_ms": 3.0, "up": True, "last_checked": None},
}

_lock = threading.Lock()
RUN_SIM = True

def simulate_once():
    
    now = datetime.now(timezone.utc).isoformat()
    with _lock:
        for name, s in SERVICES.items():
            
            base = s.get("latency_ms", 10.0)
            noise = random.uniform(-0.5, 50.0)  
            latency = max(1.0, base + noise)

           
            down_chance = 0.05  
            up = random.random() > down_chance

            
            prev_uptime = s.get("uptime_pct", 100.0)
            new_uptime = prev_uptime * 0.99 + (100.0 if up else 0.0) * 0.01

            s.update({
                "latency_ms": round(latency, 2),
                "up": bool(up),
                "uptime_pct": round(new_uptime, 2),
                "last_checked": now
            })

def simulator_loop(interval_seconds=5):
    while RUN_SIM:
        simulate_once()
        time.sleep(interval_seconds)


sim_thread = threading.Thread(target=simulator_loop, args=(5,), daemon=True)
sim_thread.start()

@app.route("/status")
def status_api():
    with _lock:
        
        data = {name: dict(values) for name, values in SERVICES.items()}
    return jsonify({"services": data, "timestamp": datetime.utcnow().isoformat() + "Z"})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        RUN_SIM = False
