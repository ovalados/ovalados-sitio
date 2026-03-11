#!/usr/bin/env python3
"""
Ovalados — Scraper automático v3
Torneos: Super Rugby Américas, URBA Top 14, Seis Naciones,
         Los Pumas, Primera A, Primera B, Primera C, Segunda, Tercera
"""
import requests, re, os, json
from datetime import datetime, timezone

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "es-AR,es;q=0.9",
}

URLS = {
    "superrugby":   "https://www.espn.com.ar/rugby/nota/_/id/14697755/super-rugby-americas-rugby-resultados-posiciones-fixture-pampas-dogos-xv-tarucas-cobras-selknam-penarol-yacare-capibaras",
    "urba":         "https://www.espn.com.ar/rugby/nota/_/id/6719883/urba-top-14-fixture-resultados-tablas",
    "seisNaciones": "https://www.espn.com.ar/rugby/nota/_/id/15203928/rugby-seis-naciones-fixture-resultados-tabla-posiciones-2026-francia-irlanda-gales-escocia-inglaterra-italia-partidos",
    "pumas":        "https://www.espn.com.ar/rugby/nota/_/id/15820133/rugby-los-pumas-calendario-2026-rugby-championship-agenda-nations-cup",
    "primeraA":     "https://www.espn.com.ar/rugby/nota/_/id/6720007/urba-primera-a-fixture-y-resultados",
    "primeraB":     "https://www.espn.com.ar/rugby/nota/_/id/6721712/primera-b-fixture-y-resultados",
    "primeraC":     "https://www.espn.com.ar/rugby/nota/_/id/6743726/urba-desarrollo-fixture-y-resultados",
    "segunda":      "https://www.espn.com.ar/rugby/nota/_/id/6720007/urba-primera-a-fixture-y-resultados",
    "tercera":      "https://www.espn.com.ar/rugby/nota/_/id/6720007/urba-primera-a-fixture-y-resultados",
}

TEAMS = {
    "superrugby": {
        "list": ["Capibaras XV","Tarucas","Dogos XV","Pampas","Selknam","Yacare XV","Cobras BR","Peñarol"],
        "aliases": {
            "capibaras xv":"Capibaras XV","capibaras":"Capibaras XV","tarucas":"Tarucas",
            "dogos xv":"Dogos XV","dogos":"Dogos XV","pampas xv":"Pampas","pampas":"Pampas",
            "selknam":"Selknam","yacaré xv":"Yacare XV","yacare xv":"Yacare XV","yacare":"Yacare XV",
            "cobras br":"Cobras BR","cobras":"Cobras BR","os cobras":"Cobras BR",
            "peñarol":"Peñarol","peñarol rugby":"Peñarol",
        }
    },
    "urba": {
        "list": ["La Plata","Hindu","Champagnat","Alumni","Newman","SIC",
                 "Belgrano Athletic","Buenos Aires C&RC","CUBA","CASI",
                 "Los Tilos","Atlético del Rosario","Regatas Bella Vista","Los Matreros"],
        "aliases": {
            "la plata":"La Plata","hindu":"Hindu","champagnat":"Champagnat","alumni":"Alumni",
            "newman":"Newman","sic":"SIC","belgrano athletic":"Belgrano Athletic","belgrano":"Belgrano Athletic",
            "buenos aires c&rc":"Buenos Aires C&RC","bacrc":"Buenos Aires C&RC","cuba":"CUBA","casi":"CASI",
            "los tilos":"Los Tilos","atlético del rosario":"Atlético del Rosario",
            "atletico del rosario":"Atlético del Rosario","regatas bella vista":"Regatas Bella Vista",
            "regatas":"Regatas Bella Vista","los matreros":"Los Matreros","matreros":"Los Matreros",
        }
    },
    "seisNaciones": {
        "list": ["Francia","Escocia","Irlanda","Italia","Inglaterra","Gales"],
        "aliases": {
            "france":"Francia","scotland":"Escocia","ireland":"Irlanda","italy":"Italia",
            "england":"Inglaterra","wales":"Gales","francia":"Francia","escocia":"Escocia",
            "irlanda":"Irlanda","italia":"Italia","inglaterra":"Inglaterra","gales":"Gales",
        }
    },
    "pumas": {
        "list": ["Argentina","Escocia","Gales","Inglaterra","Australia","Sudáfrica","Italia","Irlanda","Francia"],
        "aliases": {
            "argentina":"Argentina","los pumas":"Argentina","pumas":"Argentina",
            "scotland":"Escocia","escocia":"Escocia","wales":"Gales","gales":"Gales",
            "england":"Inglaterra","inglaterra":"Inglaterra","australia":"Australia","wallabies":"Australia",
            "south africa":"Sudáfrica","sudáfrica":"Sudáfrica","sudafrica":"Sudáfrica","springboks":"Sudáfrica",
            "italy":"Italia","italia":"Italia","ireland":"Irlanda","irlanda":"Irlanda",
            "france":"Francia","francia":"Francia",
        }
    },
    "primeraA": {
        "list": ["Hurling","Lomas Athletic","Curupayti","San Luis","Olivos","Gimnasia y Esgrima",
                 "San Albano","San Cirano","Deportiva Francesa","San Fernando","Pueyrredon",
                 "Universitario de la Plata","San Andres","Pucara"],
        "aliases": {
            "hurling":"Hurling","lomas athletic":"Lomas Athletic","lomas":"Lomas Athletic",
            "curupayti":"Curupayti","san luis":"San Luis","olivos":"Olivos",
            "gimnasia y esgrima":"Gimnasia y Esgrima","gimnasia":"Gimnasia y Esgrima",
            "san albano":"San Albano","san cirano":"San Cirano",
            "deportiva francesa":"Deportiva Francesa","francesa":"Deportiva Francesa",
            "san fernando":"San Fernando","pueyrredon":"Pueyrredon",
            "universitario de la plata":"Universitario de la Plata","universitario":"Universitario de la Plata",
            "san andres":"San Andres","san andrés":"San Andres","pucara":"Pucara","pucará":"Pucara",
        }
    },
    "primeraB": {
        "list": ["Liceo Naval","C.U. de Quilmes","Argentino","Don Bosco","San Martin",
                 "Monte Grande","Mariano Moreno","Manuel Belgrano","Delta","Vicentinos",
                 "Liceo Militar","San Patricio","Italiano","Banco Nacion"],
        "aliases": {
            "liceo naval":"Liceo Naval","cu de quilmes":"C.U. de Quilmes","quilmes":"C.U. de Quilmes",
            "argentino":"Argentino","don bosco":"Don Bosco","san martin":"San Martin",
            "monte grande":"Monte Grande","mariano moreno":"Mariano Moreno",
            "manuel belgrano":"Manuel Belgrano","delta":"Delta","vicentinos":"Vicentinos",
            "liceo militar":"Liceo Militar","san patricio":"San Patricio","italiano":"Italiano",
            "banco nacion":"Banco Nacion","banco nación":"Banco Nacion",
        }
    },
    "primeraC": {
        "list": ["Areco","SITAS","San Miguel","St Brendan","Lanus","Virreyes","San Carlos",
                 "Daom","Del Sur","CASA de Padua","Centro Naval","Los Molinos","Lujan","Ciudad de Bs.As."],
        "aliases": {
            "areco":"Areco","sitas":"SITAS","san miguel":"San Miguel","st brendan":"St Brendan",
            "lanus":"Lanus","lanús":"Lanus","virreyes":"Virreyes","san carlos":"San Carlos",
            "daom":"Daom","del sur":"Del Sur","casa de padua":"CASA de Padua",
            "centro naval":"Centro Naval","los molinos":"Los Molinos","lujan":"Lujan","luján":"Lujan",
            "ciudad de bs.as.":"Ciudad de Bs.As.",
        }
    },
    "segunda": {
        "list": ["Mercedes","Varela Jr.","Albatros","Tigre","Atletico Chascomus","Los Pinos",
                 "La Salle","El Retiro","San Marcos","Tiro F de San Pedro",
                 "Atletico y Progreso","Vicente Lopez","Old Georgian","Las Cañas"],
        "aliases": {
            "mercedes":"Mercedes","varela jr.":"Varela Jr.","varela":"Varela Jr.",
            "albatros":"Albatros","tigre":"Tigre","atletico chascomus":"Atletico Chascomus",
            "los pinos":"Los Pinos","la salle":"La Salle","el retiro":"El Retiro",
            "san marcos":"San Marcos","tiro f de san pedro":"Tiro F de San Pedro",
            "atletico y progreso":"Atletico y Progreso","vicente lopez":"Vicente Lopez",
            "vicente lópez":"Vicente Lopez","old georgian":"Old Georgian","las cañas":"Las Cañas",
        }
    },
    "tercera": {
        "list": ["Almafuerte","Tiro F de Baradero","Los Cedros","Arsenal Zarate","Banco Hipotecario",
                 "Pac General Rodriguez","G y E de Ituzaingo","Beromama","Porteño","Berisso","Ciudad de Campana"],
        "aliases": {
            "almafuerte":"Almafuerte","tiro f de baradero":"Tiro F de Baradero","los cedros":"Los Cedros",
            "arsenal zarate":"Arsenal Zarate","arsenal zárate":"Arsenal Zarate",
            "banco hipotecario":"Banco Hipotecario","pac general rodriguez":"Pac General Rodriguez",
            "g y e de ituzaingo":"G y E de Ituzaingo","beromama":"Beromama",
            "porteño":"Porteño","berisso":"Berisso","ciudad de campana":"Ciudad de Campana",
        }
    },
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
        print(f"  ✗ Error: {e}")
        return ""

def scrape_results(tournament):
    url = URLS.get(tournament)
    if not url:
        return []
    html = fetch_html(url)
    if not html:
        return []

    teams_list = TEAMS[tournament]["list"]
    results, seen = [], set()

    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.DOTALL | re.IGNORECASE)
    for row in rows:
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', row, re.DOTALL | re.IGNORECASE)
        cells = [re.sub(r'<[^>]+>', '', c).strip() for c in cells]
        cells = [re.sub(r'\s+', ' ', c).strip() for c in cells]
        cells = [c for c in cells if c]
        if len(cells) != 4:
            continue
        _, home_cell, score_cell, away_cell = cells
        score_match = re.match(r'^(\d{1,3})[-–](\d{1,3})$', score_cell.strip())
        if not score_match:
            continue
        hs, as_ = int(score_match.group(1)), int(score_match.group(2))
        home = normalize(home_cell, tournament)
        away = normalize(away_cell, tournament)
        if home not in teams_list or away not in teams_list or home == away:
            continue
        key = f"{home}_vs_{away}"
        if key in seen:
            continue
        seen.add(key)
        results.append({"home": home, "away": away, "hs": hs, "as": as_})
        print(f"  ✓ {home} {hs}–{as_} {away}")

    return results

def load_existing(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return None

def update_matches(existing_matches, scraped_results):
    if not existing_matches:
        return existing_matches
    idx = {}
    for r in scraped_results:
        idx[f"{r['home']}_vs_{r['away']}"] = r
        idx[f"{r['away']}_vs_{r['home']}"] = {"home":r["away"],"away":r["home"],"hs":r["as"],"as":r["hs"]}
    updated = 0
    for rd in existing_matches.values():
        ms_key = "ms" if "ms" in rd else "matches"
        for m in rd.get(ms_key, []):
            key = f"{m['home']}_vs_{m['away']}"
            if key in idx and not m.get("played"):
                r = idx[key]
                m.update({"hs":r["hs"],"as":r["as"],"played":True})
                updated += 1
    print(f"  → {updated} partido(s) actualizado(s)")
    return existing_matches

def recalc_standings(teams, matches):
    for t in teams:
        t.update({"pts":0,"pj":0,"g":0,"e":0,"p":0,"pf":0,"pc":0,"bp":0,"bf":0,"form":[]})
    ti = {t["name"]: t for t in teams}
    for rd in matches.values():
        ms_key = "ms" if "ms" in rd else "matches"
        for m in rd.get(ms_key, []):
            if not m.get("played"):
                continue
            h, a = ti.get(m["home"]), ti.get(m["away"])
            if not h or not a:
                continue
            hs, as_ = m["hs"], m["as"]
            h["pj"]+=1; a["pj"]+=1; h["pf"]+=hs; h["pc"]+=as_; a["pf"]+=as_; a["pc"]+=hs
            if hs > as_:
                h["pts"]+=4; h["g"]+=1; a["p"]+=1; h["form"].append("w"); a["form"].append("l")
            elif hs < as_:
                a["pts"]+=4; a["g"]+=1; h["p"]+=1; a["form"].append("w"); h["form"].append("l")
            else:
                h["pts"]+=2; h["e"]+=1; a["pts"]+=2; a["e"]+=1
                h["form"].append("d"); a["form"].append("d")
            if m.get("bp_home"): h["pts"]+=1; h["bp"]+=1
            if m.get("bp_away"): a["pts"]+=1; a["bp"]+=1
            if m.get("bf_home"): h["pts"]+=1; h["bf"]+=1
            if m.get("bf_away"): a["pts"]+=1; a["bf"]+=1
            h["form"]=h["form"][-5:]; a["form"]=a["form"][-5:]
    return teams

def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  💾 {path}")

def process_tournament(tournament, data_dir):
    print(f"\n── {tournament.upper()} {'─'*(40-len(tournament))}")
    json_path = os.path.join(data_dir, f"{tournament}.json")
    existing  = load_existing(json_path)
    scraped   = scrape_results(tournament)
    print(f"  Resultados scrapeados: {len(scraped)}")
    if not scraped:
        print("  ⚠ Sin resultados nuevos, preservando datos existentes")
        return
    if existing:
        existing["matches"]        = update_matches(existing.get("matches", {}), scraped)
        if existing.get("teams"):
            existing["teams"]      = recalc_standings(existing["teams"], existing["matches"])
        existing["lastUpdate"]     = datetime.now(timezone.utc).isoformat()
        existing["matchesScraped"] = len(scraped)
        save_json(existing, json_path)
    else:
        save_json({"lastUpdate": datetime.now(timezone.utc).isoformat(),
                   "matchesScraped": len(scraped), "results": scraped}, json_path)
        print("  ⚠ No había JSON base — guardados resultados crudos")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir   = os.path.normpath(os.path.join(script_dir, "..", "data"))
    print(f"\n{'='*52}")
    print(f"Ovalados Scraper v3 — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"Data dir: {data_dir}")
    print(f"{'='*52}")
    for t in ["superrugby","urba","seisNaciones","pumas","primeraA","primeraB","primeraC","segunda","tercera"]:
        process_tournament(t, data_dir)
    print(f"\n✓ Listo\n")

if __name__ == "__main__":
    main()
