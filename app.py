from flask import Flask, render_template, jsonify
import threading
import time
import random
from datetime import datetime
from datetime import timezone 

app = Flask(__name__)

# ----------------------------
# SIMULADOR DOS SERVIÇOS
# ----------------------------

SERVICES = {
    "web-api":  {"uptime_pct": 100.0, "latency_ms": 20.0, "up": True, "last_checked": None},
    "database": {"uptime_pct": 100.0, "latency_ms": 8.0,  "up": True, "last_checked": None},
    "cache":    {"uptime_pct": 100.0, "latency_ms": 3.0,  "up": True, "last_checked": None},
}

_lock = threading.Lock()
RUN_SIM = True


def simulate_once():
    """Atualiza uma vez o estado dos serviços."""
    now = datetime.now(timezone.utc).isoformat()
    with _lock:
        for name, s in SERVICES.items():
            base = s.get("latency_ms", 10.0)

            # ruído na latência
            noise = random.uniform(-0.5, 50.0)
            latency = max(1.0, base + noise)

            # 5% de chance de ficar DOWN
            down_chance = 0.05
            up = random.random() > down_chance

            # atualiza uptime
            prev_uptime = s.get("uptime_pct", 100.0)
            new_uptime = prev_uptime * 0.99 + (100.0 if up else 0.0) * 0.01

            s.update({
                "latency_ms": round(latency, 2),
                "up": bool(up),
                "uptime_pct": round(new_uptime, 2),
                "last_checked": now
            })


def simulator_loop(interval_seconds=5):
    """Loop em background atualizando os serviços."""
    while RUN_SIM:
        simulate_once()
        time.sleep(interval_seconds)


# thread de simulação
sim_thread = threading.Thread(target=simulator_loop, args=(5,), daemon=True)
sim_thread.start()

# ----------------------------
# ROTAS HTTP
# ----------------------------

@app.route("/status")
def status_api():
    """Retorna o estado atual dos serviços em JSON."""
    with _lock:
        data = {name: dict(values) for name, values in SERVICES.items()}
    return jsonify({
        "services": data,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/")
def index():
    """Página principal com o painel estilo simulador."""
    return render_template("index.html")


if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        RUN_SIM = False
