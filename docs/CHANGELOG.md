# CHANGELOG

Alle vesentlige endringer i dette prosjektet dokumenteres i dette dokumentet.

## [0.1.0] – 2025‑08‑02

### Added

* Initial repository structure basert på utviklingsplanen.
* Konfigurasjonsfiler: `docker-compose.yaml`, `README`, `ROADMAP`, `SYSTEM_OVERVIEW`, `CHANGELOG`.
* Opprettet mappehierarki for moduler: whisper, jupyter, scripts, ollama, openrouter, db, dashboards med mer.

## [0.1.1] – 2025‑08‑02

### Added

* Lagt til en prøvefil med aksjekurser (`data/sample_stock.csv`) som gir et grunnlag for utvikling uten nettaksess.
* Implementert `scripts/data/fetch_sample.py` med funksjonen `load_sample_data()` for å lese prøvedata til en Pandas DataFrame.
* Oppdatert `README.md`, `docs/ROADMAP.md` og `docs/SYSTEM_OVERVIEW.md` med informasjon om den nye datamodulen og offline datainnhenting.