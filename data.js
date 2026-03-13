// ============================================================
//  OVALADOS — DATOS DE PORTADA
//  Edita solo este archivo cada fecha para actualizar el home.
// ============================================================
// ── ULTIMOS RESULTADOS ───────────────────────────────────────
const SR_ULTIMA_FECHA = {
  label: "Super Rugby Americas - Fecha 3",
  partidos: [
    { home:"Tarucas",     hs:29, away:"Dogos XV",     as:26, fecha:"08/03/2026" },
    { home:"Pampas",      hs:25, away:"Capibaras XV", as:20, fecha:"08/03/2026" },
    { home:"Penarol",     hs:40, away:"Selknam",      as:27, fecha:"07/03/2026" },
    { home:"Cobras BR",   hs:21, away:"Yacare XV",    as:19, fecha:"07/03/2026" },
  ]
};
// ── PROXIMA FECHA ────────────────────────────────────────────
const SR_PROXIMA_FECHA = {
  label: "Super Rugby Americas - Fecha 4 - 14-15 mar",
  partidos: [
    { home:"Penarol",   away:"Tarucas",      fecha:"14/03" },
    { home:"Dogos XV",  away:"Capibaras XV", fecha:"15/03" },
    { home:"Yacare XV", away:"Pampas",       fecha:"15/03" },
    { home:"Selknam",   away:"Cobras BR",    fecha:"15/03" },
  ]
};
// ── RENDER AUTOMATICO ────────────────────────────────────────
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
      <div class="result-score gold">${p.hs} - ${p.as}</div>
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
        "1. Calandra, F",
        "2. Rocha, L",
        "3. Chiappe, B",
        "4. Curuchaga, M",
        "5. Plorutti, C",
        "6. Panzarini, A",
        "7. De Oliveira, S",
        "8. Meyrelles, T",
        "9. Albanese, M",
        "10. Sascaro, A",
        "11. Fleming, B",
        "12. Piran, C",
        "13. Acosta, N",
        "14. Silva, T",
        "15. Capdevilla, F",
      ]
    },
    visitante: {
      nombre: "Belgrano Athletic",
      jugadores: [
        "1. Ferronato, Francisco",
        "2. Garcia Dragui, Lisandro",
        "3. Morales, Franco",
        "4. Tecca, Luciano",
        "5. Bloom, Mikael",
        "6. Vaccarino, Augusto",
        "7. Rebussone, Julian",
        "8. Vega, Franco",
        "9. Blacksley, Theo",
        "10. Aparicio, Juan",
        "11. Bernabe, Tobias",
        "12. Arana, Martin",
        "13. Etchepare, Tomas",
        "14. Arana, Pedro",
        "15. Lando, Juan",
      ]
    }
  },
  const PARTIDOS = {
  la_plata_atletico_del_rosario: {
    local: {
      nombre: "La Plata",
      jugadores: [
        "1. Del Cerro, Ariel",
        "2. Nunez, Joaquin",
        "3. Patat, Martin",
        "4. Ozog, Bautista",
        "5. Kucic, Ivan",
        "6. Pineda, Segundo",
        "7. Chiappani, Nicolas",
        "8. Bernasconi, Tomas",
        "9. De la Fuente, Manuel",
        "10. Di Lucca, Santino",
        "11. Addiechi, Pedro",
        "12. Paz Rizzoli, Francisco",
        "13. Cejas, Francisco",
        "14. Panigatti, Facundo",
        "15. Sica Manuele, Federico",
      ]
    },
    visitante: {
      nombre: "Atletico del Rosario",
      jugadores: [
        "1. Reyes, Ezequiel",
        "2. Rubio, Ramiro",
        "3. Montenegro, Bruno",
        "4. Caceres, Jose",
        "5. Capella, Octavio",
        "6. Sapino, Ignacio",
        "7. Echenique, Francisco",
        "8. Malanos, Lucas",
        "9. Nogues, Felipe",
        "10. Nogues, Manuel",
        "11. Casals, Nicolas",
        "12. Malanos, Tomas",
        "13. Musio, Ramiro",
        "14. Bertero, Juan Cruz",
        "15. Elias, Martin",
      ]
    }
  },
};
