#!/usr/bin/env python3
"""
Ovalados — Scraper automático v2
Scrapea ESPN y genera JSONs en data/ para el sitio estático.
"""
import requests, re, os, json
from datetime import datetime, timezone

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "es-AR,es;q=0.9",
}

# ── URLs ESPN ──────────────────────────────────────────────
URLS = {
    "superrugby":  "https://www.espn.com.ar/rugby/nota/_/id/14697755/super-rugby-americas-rugby-resultados-posiciones-fixture-pampas-dogos-xv-tarucas-cobras-selknam-penarol-yacare-capibaras",
    "urba":        "https://www.espn.com.ar/rugby/nota/_/id/6719883/urba-top-14-fixture-resultados-tablas",
    "seisNaciones":"https://www.espn.com.ar/rugby/nota/_/id/15203928/rugby-seis-naciones-fixture-resultados-tabla-posiciones-2026-francia-irlanda-gales-escocia-inglaterra-italia-partidos",
}

# ── Equipos y aliases ──────────────────────────────────────
TEAMS = {
    "superrugby": {
        "list": ["Capibaras XV","Tarucas","Dogos XV","Pampas","Selknam","Yacare XV","Cobras BR","Peñarol"],
        "aliases": {
            "capibaras xv":"Capibaras XV","capibaras":"Capibaras XV",
            "tarucas":"Tarucas","los tarucas":"Tarucas",
            "dogos xv":"Dogos XV","dogos":"Dogos XV",
            "pampas xv":"Pampas","pampas":"Pampas",
            "selknam":"Selknam",
            "yacaré xv":"Yacare XV","yacare xv":"Yacare XV","yacare":"Yacare XV",
            "cobras br":"Cobras BR","cobras":"Cobras BR","os cobras":"Cobras BR",
            "peñarol":"Peñarol","peñarol rugby":"Peñarol",
        }
    },
    "urba": {
        "list": ["La Plata","Hindu","Champagnat","Alumni","Newman","SIC",
                 "Belgrano Athletic","Buenos Aires C&RC","CUBA","CASI",
                 "Los Tilos","Atlético del Rosario","Regatas Bella Vista","Los Matreros"],
        "aliases": {
            "la plata":"La Plata","hindu":"Hindu","champagnat":"Champagnat",
            "alumni":"Alumni","newman":"Newman","sic":"SIC",
            "belgrano athletic":"Belgrano Athletic","belgrano":"Belgrano Athletic",
            "buenos aires c&rc":"Buenos Aires C&RC","bacrc":"Buenos Aires C&RC",
            "cuba":"CUBA","casi":"CASI","los tilos":"Los Tilos",
            "atlético del rosario":"Atlético del Rosario","atletico del rosario":"Atlético del Rosario",
            "regatas bella vista":"Regatas Bella Vista","regatas":"Regatas Bella Vista",
            "los matreros":"Los Matreros","matreros":"Los Matreros",
        }
    },
    "seisNaciones": {
        "list": ["Francia","Escocia","Irlanda","Italia","Inglaterra","Gales"],
        "aliases": {
            "france":"Francia","scotland":"Escocia","ireland":"Irlanda",
            "italy":"Italia","england":"Inglaterra","wales":"Gales",
            "francia":"Francia","escocia":"Escocia","irlanda":"Irlanda",
            "italia":"Italia","inglaterra":"Inglaterra","gales":"Gales",
        }
    }
}

def normalize(name, tournament):
    aliases = TEAMS[tournament]["aliases"]
    return aliases.get(name.lower().strip(), name.strip())

def fetch_html(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        r.raise_for_status()
        return r.text
    except Exception as e:
        print(f"  ✗ Error fetching: {e}")
        return ""

def scrape_results(tournament):
    """
    Scrapea la nota ESPN y devuelve lista de resultados jugados.
    Formato: [{ home, away, hs, as }]
    """
    url = URLS[tournament]
    html = fetch_html(url)
    if not html:
        return []

    teams_list = TEAMS[tournament]["list"]
    results = []
    seen = set()

    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.DOTALL | re.IGNORECASE)
    for row in rows:
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.DOTALL | re.IGNORECASE)
        cells = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]
        cells = [re.sub(r'\s+', ' ', c).strip() for c in cells]
        cells = [c for c in cells if c]

        if len(cells) != 4:
            continue

        date_cell, home_cell, score_cell, away_cell = cells
        score_match = re.match(r'^(\d{1,3})[-–](\d{1,3})$', score_cell.strip())
        if not score_match:
            continue

        hs  = int(score_match.group(1))
        as_ = int(score_match.group(2))
        home = normalize(home_cell, tournament)
        away = normalize(away_cell, tournament)

        if home not in teams_list or away not in teams_list:
            continue
        if home == away:
            continue

        key = f"{home}_vs_{away}"
        if key in seen:
            continue
        seen.add(key)

        results.append({"home": home, "away": away, "hs": hs, "as": as_})
        print(f"  ✓ {home} {hs}–{as_} {away}")

    return results

def load_existing(path):
    """Carga el JSON existente del sitio para preservar fixture y datos no scrapeables."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return None

def update_matches(existing_matches, scraped_results):
    """
    Combina el fixture existente con los resultados scrapeados.
    Solo actualiza partidos que el scraper encontró como jugados.
    Preserva todos los partidos pendientes del fixture.
    """
    if not existing_matches:
        return existing_matches

    # Índice de resultados scrapeados para búsqueda rápida
    results_index = {}
    for r in scraped_results:
        key = f"{r['home']}_vs_{r['away']}"
        key_rev = f"{r['away']}_vs_{r['home']}"
        results_index[key] = r
        results_index[key_rev] = {"home": r["away"], "away": r["home"], "hs": r["as"], "as": r["hs"]}

    updated = 0
    for round_key, round_data in existing_matches.items():
        for match in round_data.get("ms", []):
            key = f"{match['home']}_vs_{match['away']}"
            if key in results_index and not match.get("played"):
                r = results_index[key]
                match["hs"] = r["hs"]
                match["as"] = r["as"]
                match["played"] = True
                updated += 1

    print(f"  → {updated} partido(s) actualizado(s) en fixture")
    return existing_matches

def recalc_standings(teams, matches):
    """Recalcula la tabla de posiciones desde cero basándose en los matches jugados."""
    # Reset
    for t in teams:
        t.update({"pts":0,"pj":0,"g":0,"e":0,"p":0,"pf":0,"pc":0,"bp":0,"bf":0,"form":[]})

    team_index = {t["name"]: t for t in teams}

    for round_data in matches.values():
        for m in round_data.get("ms", []):
            if not m.get("played"):
                continue
            h = team_index.get(m["home"])
            a = team_index.get(m["away"])
            if not h or not a:
                continue

            hs, as_ = m["hs"], m["as"]
            h["pj"] += 1; a["pj"] += 1
            h["pf"] += hs; h["pc"] += as_
            a["pf"] += as_; a["pc"] += hs

            if hs > as_:
                h["pts"] += 4; h["g"] += 1; a["p"] += 1
                h["form"].append("w"); a["form"].append("l")
            elif hs < as_:
                a["pts"] += 4; a["g"] += 1; h["p"] += 1
                a["form"].append("w"); h["form"].append("l")
            else:
                h["pts"] += 2; h["e"] += 1
                a["pts"] += 2; a["e"] += 1
                h["form"].append("d"); a["form"].append("d")

            # Bonus ofensivo (BP): 4+ tries aproximado por score alto
            if m.get("bp_home"): h["pts"] += 1; h["bp"] += 1
            if m.get("bp_away"): a["pts"] += 1; a["bp"] += 1
            if m.get("bf_home"): h["pts"] += 1; h["bf"] += 1
            if m.get("bf_away"): a["pts"] += 1; a["bf"] += 1

            # Mantener solo últimas 5 fechas en form
            h["form"] = h["form"][-5:]
            a["form"] = a["form"][-5:]

    return teams

def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  💾 Guardado: {path}")

def process_tournament(tournament, data_dir):
    print(f"\n── {tournament.upper()} ─────────────────────────────────")

    json_path = os.path.join(data_dir, f"{tournament}.json")
    existing = load_existing(json_path)

    # Scrapear resultados nuevos
    scraped = scrape_results(tournament)
    print(f"  Resultados scrapeados: {len(scraped)}")

    if not scraped:
        print("  ⚠ Sin resultados nuevos, preservando datos existentes")
        return

    if existing:
        # Actualizar matches con resultados scrapeados
        updated_matches = update_matches(existing.get("matches", {}), scraped)
        # Recalcular standings
        updated_teams = recalc_standings(existing.get("teams", []), updated_matches)
        existing["matches"] = updated_matches
        existing["teams"] = updated_teams
        existing["lastUpdate"] = datetime.now(timezone.utc).isoformat()
        existing["matchesScraped"] = len(scraped)
        save_json(existing, json_path)
    else:
        # No hay JSON existente, guardar solo los resultados scrapeados
        data = {
            "lastUpdate": datetime.now(timezone.utc).isoformat(),
            "matchesScraped": len(scraped),
            "results": scraped
        }
        save_json(data, json_path)
        print("  ⚠ No había JSON base — guardados solo resultados crudos")

def main():
    # Detectar directorio data/ relativo al script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # El scraper está en scraper/, los datos en data/ (un nivel arriba)
    data_dir = os.path.join(script_dir, "..", "data")
    data_dir = os.path.normpath(data_dir)

    print(f"\n{'='*52}")
    print(f"Ovalados Scraper v2 — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Data dir: {data_dir}")
    print(f"{'='*52}")

    for tournament in ["superrugby", "urba", "seisNaciones"]:
        process_tournament(tournament, data_dir)

    print(f"\n✓ Listo\n")

if __name__ == "__main__":
    main()
