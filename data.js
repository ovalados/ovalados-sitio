// ============================================================
//  OVALADOS — DATOS DE PORTADA
//  Editá solo este archivo cada fecha para actualizar el home.
// ============================================================
// ── ÚLTIMOS RESULTADOS ───────────────────────────────────────
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

// ── FORMACIONES TOP 14 ────────────────────────────────────────
const PARTIDOS = {
  sic_belgrano_athletic: {
    local: {
      nombre: "SIC",
      jugadores: [
        “1. Calandra, F”,
        “2. Rocha, L”,
        “3. Chiappe, B”,
        “4. Curuchaga, M”,
        “5. Plorutti, C”,
        “6. Panzarini, A”,
        “7. F De Oliveira, S”,
        “8. Meyrelles, T”,
        “9. Albanese, M”,
        “10. Sascaro, A”,
        “11. L. Fleming, B”,
        “12. Piran, C”,
        “13. Acosta, N”,
        “14. Silva, T”,
        “15. G Capdevilla, F”,
      ]
    },
    visitante: {
      nombre: "Belgrano Athletic",
      jugadores: [
        “1. Ferronato, Francisco”,
“2. García Dragui, Lisandro”,
“3. Morales, Franco”,
“4. Tecca, Luciano”,
“5. Bloom Quesada, Mikael”,
“6. Vaccarino, Augusto”,
“7. Rebussone, Julián”,
“8. Vega, Franco”,
“9. Blacksley, Theo”,
“10. Aparicio, Juan”,
“11. Bernabé, Tobias”,
“12. Arana, Martin”,
“13. Etchepare, Tomás”,
“14. Arana, Pedro”,
“15. Landó, Juan”,
      ]
    }
  },
};
