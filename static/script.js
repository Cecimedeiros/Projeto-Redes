async function fetchStatus() {
  try {
    const res = await fetch('/status');
    const data = await res.json();

    const services    = Object.entries(data.services || {});
    const listEl      = document.getElementById('service-list');
    const leftTime    = document.getElementById('left-time');
    const centerTime  = document.getElementById('center-time');
    const lastUpdate  = document.getElementById('last-update');

    listEl.innerHTML = '';

    // lista de serviços
    services.forEach(([name, s]) => {
      const li = document.createElement('li');
      li.className = 'service-item';

      const upText = s.up ? 'UP' : 'DOWN';

      li.innerHTML = `
        <div class="svc-name-line">
          <span class="name">${name}</span>
          <span class="state ${s.up ? 'state-up' : 'state-down'}">${upText}</span>
        </div>
        <div class="svc-meta-line">
          <span><span class="label">Latency:</span> ${s.latency_ms}ms</span>
          <span><span class="label">Uptime:</span> ${s.uptime_pct}%</span>
          <span><span class="label">Última checagem:</span> ${s.last_checked || '-'}</span>
        </div>
      `;

      listEl.appendChild(li);
    });

    // métricas agregadas
    const uptimeSpan  = document.getElementById('uptime-value');
    const latencySpan = document.getElementById('latency-value');
    const statusSpan  = document.getElementById('status-value');

    if (services.length) {
      let sumUptime  = 0;
      let sumLatency = 0;
      let allUp      = true;

      services.forEach(([_, s]) => {
        sumUptime  += Number(s.uptime_pct  || 0);
        sumLatency += Number(s.latency_ms || 0);
        if (!s.up) allUp = false;
      });

      const avgUptime  = (sumUptime / services.length).toFixed(2);
      const avgLatency = Math.round(sumLatency / services.length);

      uptimeSpan.textContent  = `${avgUptime}%`;
      latencySpan.textContent = `${avgLatency}ms`;
      statusSpan.textContent  = allUp ? 'OK' : 'ISSUES';

      statusSpan.className = 'value ' + (allUp ? 'metric-ok' : 'metric-error');
    } else {
      uptimeSpan.textContent  = '--';
      latencySpan.textContent = '--';
      statusSpan.textContent  = 'NO DATA';
    }

    const ts = data.timestamp || '-';
    leftTime.textContent   = ts;
    centerTime.textContent = ts;
    lastUpdate.textContent = ts;

  } catch (err) {
    console.error('Erro buscando /status', err);
  }
}

// atualiza ao abrir e a cada 5s
fetchStatus();
setInterval(fetchStatus, 5000);
