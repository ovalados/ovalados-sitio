# Ovalados — Guía de actualización automática

## Cómo funciona

```
GitHub Actions (cada 6hs)
    → corre scraper/fetch.py
    → actualiza data/superrugby.json, data/urba.json, data/seisNaciones.json
    → hace commit automático
    → Netlify detecta el cambio → rebuild del sitio
```

---

## PASO 1 — Subir estos archivos a tu repo ovalados-sitio

Subir a GitHub (repo `ovalados-sitio`) con esta estructura exacta:

```
ovalados-sitio/
├── index.html
├── top14.html
├── super-rugby.html
├── seis-naciones.html
├── pumas.html
├── ... (resto de HTMLs)
├── css/styles.css
├── img/
├── data/                        ← NUEVA carpeta
│   ├── superrugby.json          ← NUEVO
│   ├── urba.json                ← NUEVO
│   └── seisNaciones.json        ← NUEVO
├── scraper/                     ← NUEVA carpeta
│   ├── fetch.py                 ← NUEVO
│   └── requirements.txt         ← NUEVO
└── .github/
    └── workflows/
        └── scraper.yml          ← NUEVO
```

---

## PASO 2 — Crear los JSONs base en GitHub

Ve a tu repo en GitHub → Add file → Create new file

### Archivo: `data/superrugby.json`
Copiá el contenido del archivo `data/superrugby.json` que te di.

### Archivo: `data/urba.json`
Copiá el contenido del archivo `data/urba.json` que te di.

### Archivo: `data/seisNaciones.json`
Copiá el contenido del archivo `data/seisNaciones.json` que te di.

---

## PASO 3 — Conectar Netlify al repo

1. Andá a netlify.com → tu sitio
2. Site configuration → Build & deploy
3. Buscá "Link to Git repository"
4. Elegí GitHub → seleccioná `ovalados-sitio`
5. Build settings:
   - Build command: (vacío, sitio estático)
   - Publish directory: `.`
6. Deploy

---

## PASO 4 — Verificar que Actions funciona

1. Andá a tu repo en GitHub → pestaña "Actions"
2. Click en "Actualizar resultados"
3. Click en "Run workflow" (botón verde)
4. Esperá ~1 minuto
5. Si ves ✓ verde, funciona

---

## Frecuencia de actualización

El scraper corre automáticamente:
- 00:00 UTC (21:00 Argentina)
- 06:00 UTC (03:00 Argentina)
- 12:00 UTC (09:00 Argentina)
- 18:00 UTC (15:00 Argentina)

También podés correrlo a mano desde GitHub → Actions → Run workflow.

---

## Si algo falla

Los logs de cada corrida se ven en GitHub → Actions → click en el run.
Los errores más comunes son:
- ESPN cambió el formato de la nota → hay que actualizar el scraper
- El JSON base no existe → hay que crearlo manualmente una vez
