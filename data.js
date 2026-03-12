// ============================================================
//  OVALADOS — DATOS DE PORTADA
//  Editá solo este archivo cada fecha para actualizar el home.
// ============================================================

// ── ÚLTIMOS RESULTADOS ───────────────────────────────────────
// Cambiá el label y los 4 partidos después de cada fecha.
const SR_ULTIMA_FECHA = {
  label: "Super Rugby Américas · Fecha 3",
  partidos: [
    { home:"Tarucas",     hs:29, away:"Dogos XV",     as:26, fecha:"08/03/2026" },
    { home:"Pampas",      hs:25, away:"Capibaras XV", as:20, fecha:"08/03/2026" },
    { home:"Peñarol",     hs:40, away:"Selknam",      as:27, fecha:"07/03/2026" },
    { home:"Cobras BR",   hs:21, away:"Yacare XV",    as:19, fecha:"07/03/2026" },
  ]
};

// ── PRÓXIMA FECHA ────────────────────────────────────────────
// Cambiá el label y los 4 partidos cuando haya nueva fecha.
const SR_PROXIMA_FECHA = {
  label: "Super Rugby Américas · Fecha 4 · 14–15 mar",
  partidos: [
    { home:"Peñarol",   away:"Tarucas",      fecha:"14/03" },
    { home:"Dogos XV",  away:"Capibaras XV", fecha:"15/03" },
    { home:"Yacare XV", away:"Pampas",       fecha:"15/03" },
    { home:"Selknam",   away:"Cobras BR",    fecha:"15/03" },
  ]
};

// ── RENDER AUTOMÁTICO ────────────────────────────────────────
// No toques esto.
document.addEventListener('DOMContentLoaded', function() {
  const ul = document.getElementById('sr-ultimos');
  const px = document.getElementById('sr-proximos');
  const ulLabel = document.getElementById('sr-ultimos-label');
  const pxLabel = document.getElementById('sr-proximos-label');

  if (ulLabel) ulLabel.textContent = SR_ULTIMA_FECHA.label;
  if (pxLabel) pxLabel.textContent = SR_PROXIMA_FECHA.label;

  if (ul) ul.innerHTML = SR_ULTIMA_FECHA.partidos.map(p => `
    <div class="result-row gold-hover">
      <div class="result-home">${p.home}</div>
      <div class="result-score gold">${p.hs} — ${p.as}</div>
      <div class="result-away">${p.away}</div>
      <div class="result-date">${p.fecha}</div>
    </div>`).join('');

  if (px) px.innerHTML = SR_PROXIMA_FECHA.partidos.map(p => `
    <div class="result-row gold-hover">
      <div class="result-home">${p.home}</div>
      <div class="result-score upcoming">VS</div>
      <div class="result-away">${p.away}</div>
      <div class="result-date">${p.fecha}</div>
    </div>`).join('');
});
