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
  hindu_los_tilos: {
    local: {
      nombre: "Hindu",
      jugadores: [
        "1. Diviesti, Franco",
        "2. Capurro, Agustin",
        "3. Leiva, Nicolas",
        "4. Scallan, Tomas",
        "5. Comolli, Juan",
        "6. Amaya, Santinl",
        "7. Bavaro, Lautaro",
        "8. Amaya, Nicolas",
        "9. Ezcurra, Felipe",
        "10. Ormaechea, Fermin",
        "11. Graglia, Facundo",
        "12. Fernandez Miranda, Ramon",
        "13. Rodriguez, Lisandro",
        "14. Amher, Tomas",
        "15. Aranoa, Juan",
      ]
    },
    visitante: {
      nombre: "Los Tilos",
      jugadores: [
        "1. Briozzo, Joaquin",
        "2. San Sebastian, Hipolito",
        "3. Laurin, Maximo",
        "4. Leiva, Martin",
        "5. Blaiotta Lago, Juan",
        "6. Torboli, Luciano",
        "7. Chiavassa, Eliseo",
        "8. Bares, Felipe",
        "9. Rodriguez Alcobendas, Pedro",
        "10. Tuculet, Joaquin",
        "11. Martinez, Gaston",
        "12. Fernandez Armendariz, Tomas",
        "13. Bassagaistegui, Tiago",
        "14. Guichon, Ignacio",
        "15. Santamarina, Bautista",
      ]
    }
  },
  champagnat_casi: {
    local: {
      nombre: "Champagnat",
      jugadores: [
        "1. Adissi, Alberto Natan",
        "2. Rodriguez Pascarella, Fernando",
        "3. Magaro, Marcos",
        "4. Escuti, Santiago",
        "5. Rivas Orozco, Tobias",
        "6. Alonso Boto, Matias Jesus",
        "7. Castelli Azpiroz, Francisco Migi",
        "8. Rojo, Nicolas",
        "9. Panelo, Juan Segundo",
        "10. Panelo, Santos",
        "11. Rodriguez Navarro, Bautista",
        "12. Bottazzi, Joaquin",
        "13. Cotter Daireaux, Tomas",
        "14. Rufino, Facundo",
        "15. Costaguta, Gonzalo",
      ]
    },
    visitante: {
      nombre: "CASI",
      jugadores: [
        "1. Scaiano, Facundo",
        "2. Torres Obeid, Juan Bautista",
        "3. Paolucci, Felix",
        "4. Torrado, Ignacio",
        "5. Mazzini, Leo",
        "6. Sartori, Eugenio",
        "7. Paolucci, Benito",
        "8. Rocca Rivarola, Benjamin",
        "9. Sanchez, Joaquin",
        "10. Hileman, Felipe",
        "11. Lescano, Francisco",
        "12. Solveyra, Jeronimo",
        "13. Belaga, Benjamin",
        "14. Tumbarello, Jeronimo",
        "15. Akemeier, Juan",
      ]
    }
  },
  alumni_cuba: {
    local: {
      nombre: "Alumni",
      jugadores: [
        "1. Bottoni, Juan Cruz",
        "2. Lamelas, Maximo",
        "3. Bottoni, Francisco",
        "4. Mora, Manuel",
        "5. Alduncin, Santiago",
        "6. Cubilla, Ignacio",
        "7. Anderson, Juan Patricio",
        "8. Neyra, Santiago",
        "9. Passerotti, Tomas",
        "10. Canzani, Bautista",
        "11. Vieyra, Aquiles",
        "12. Testoni, Filippo",
        "13. Sabato, Franco",
        "14. Fuentes, Ramon",
        "15. Del Franco, Matias",
      ]
    },
    visitante: {
      nombre: "CUBA",
      jugadores: [
        "1. Garoby, Francisco",
        "2. Anderlic, Tomas",
        "3. Iribarne, Esteban",
        "4. Loza, Marcos",
        "5. Uriarte, Santiago",
        "6. Campion, Lucas",
        "7. Pisani, Segundo",
        "8. Ortiz de Rozas, Benito",
        "9. Albani, Ignacio",
        "10. Mastroizzi, Valentin",
        "11. Castro Nevares, Pedro",
        "12. Benedit, Rafael",
        "13. de la Vega, Felipe",
        "14. Cardini, Ramiro",
        "15. Passaro, Tomas",
      ]
    }
  },
  los_matreros_regatas_bella_vista: {
    local: {
      nombre: "Los Matreros",
      jugadores: [
        "1. Salina, Matias",
        "2. Cec, Boris",
        "3. Zeiss, Juan Pablo",
        "4. Gahan, Tomas",
        "5. Villafane, Alejo",
        "6. McCormack, Colin",
        "7. Guevara, Juan Pablo",
        "8. Villarino, Santiago",
        "9. Amorisa, Marcos",
        "10. Morales, Juan Francisco",
        "11. Marelli, Santiago",
        "12. Del Busto, Pedro",
        "13. Santecchia, Nicolas",
        "14. Gallastegui, German",
        "15. Garcia Michero, Juan Pablo",
      ]
    },
    visitante: {
      nombre: "Regatas Bella Vista",
      jugadores: [
        "1. Barbaccia, Tomas",
        "2. Landivar, Beltran",
        "3. Gobet, Juan Manuel",
        "4. Sanguinetti, Valentin",
        "5. Sanguinetti, Tomas",
        "6. Garcia Campos, Agustin",
        "7. Gobet, Lucas",
        "8. Camerlinckx, Felipe",
        "9. Joseph, Marcos",
        "10. Camerlinkckx, Justo",
        "11. Camerlinckx, Enrique",
        "12. Camerlinckx, Mateo",
        "13. Klapenbach, Tobias",
        "14. Pisani, Francisco",
        "15. Rugolo, Felipe",
      ]
    }
  },
  newman_buenos_aires_c_rc: {
    local: {
      nombre: "Newman",
      jugadores: [
        "1. Prince, Miguel",
        "2. Perkins, Fermin",
        "3. Bosch, Bautista",
        "4. Cardinal, Pablo",
        "5. Urtubey, Alejandro",
        "6. Montoya, Mateo",
        "7. De la Vega, Joaquin",
        "8. Diaz de Vivar, Rodrigo",
        "9. Nava, Lucas",
        "10. Gutierrez Taboada, Gonzalo",
        "11. Ortiz Basualdo, Justo",
        "12. Lanfranco, Benjamin",
        "13. Prince, Simon",
        "14. Ulloa, Cruz",
        "15. Daireaux, Juan Bautista",
      ]
    },
    visitante: {
      nombre: "Buenos Aires C&RC",
      jugadores: [
        "1. Gallo, Tomas",
        "2. Ruiz, Tomas",
        "3. Zanella, Renzo",
        "4. Syriani, Francisco",
        "5. Saint Bonnet, Bautista",
        "6. Espina, Matias",
        "7. Bourdal, Pablo",
        "8. Etcheverry, Tomas",
        "9. Freire, Mateo",
        "10. Bunge, Tomas",
        "11. Bensadon, Ignacio",
        "12. Lamensa, Agustin",
        "13. Costa, Ramiro",
        "14. Ortiz, Segundo",
        "15. Novo, Alejo",
      ]
    }
  }
};
