# ROADMAP

Dette dokumentet beskriver den fasevise utviklingsplanen for Annexa Trading. 

## Fase 1: Infrastruktur og n8n‑grunnsystem

* Sett opp mappestruktur, `.gitignore` og basale dokumenter (`README`, `SYSTEM_OVERVIEW`, `CHANGELOG`).
* Lag `docker-compose.yaml` som starter n8n og Jupyter.
* Start n8n via Docker og bekreft at du kan logge inn og opprette en enkel workflow.

## Fase 2: Datainnhenting

* Utvikle en modul i `scripts/` eller direkte i n8n som henter markedsdata fra en valgt kilde (f.eks. Yahoo Finance eller Finnhub).
* Lagre dataene lokalt (CSV/SQLite) og verifiser at oppdateringer hentes riktig.
* Før du går videre, sørg for at datainnhentingen fungerer stabilt og automatisk via n8n.

## Fase 3: Grunnleggende analyse

* Lag notebooks eller Python‑skript som beregner enkle tekniske indikatorer som RSI og SMA.
* Integrer disse beregningene i n8n‑flyten, slik at dataene analyseres kontinuerlig.
* Verifiser at indikatorene beregnes korrekt før du fortsetter.

## Fase 4: Simuleringsmotor

* Implementer et skript i `scripts/simulation` som tar signaler (for eksempel basert på RSI) og simulerer handler over historiske data.
* Lag en strategi‑loop med logging til SQLite i `db/history.sqlite`.
* Evaluer ytelsen (profit/loss, drawdown) og generer rapporter. Ikke gå videre før simuleringen gir mening.

## Fase 5: Handelsintegrasjon (Nordnet eller alternativ)

* Utforsk API for Nordnet eller annen broker og sett opp en demokonto.
* Implementer modul i `scripts/trading_api` som kan sende ordre til demokontoen.
* Integrer ordresendingen i n8n‑flyten basert på signalene fra simuleringen.

## Fase 6: Dashbord og overvåkning

* Lag et dashbord (for eksempel med Streamlit eller Grafana) i `dashboards/` for å visualisere signaler, historikk og kapitalutvikling.
* Oppdater n8n til å sende løpende statuser til dashbordet.

## Fase 7: Avanserte funksjoner (LLM/tale – valgfritt)

* Hvis ønskelig, implementer en LLM‑modul (Ollama/OpenRouter) som kan tolke naturlig språk og generere forslag eller rapporter.
* Eventuelle tale‑til‑tekst‑funksjoner (Whisper) legges til her som en valgfri modul, etter at kjernesystemet fungerer.

## Fase 8: Automatisert vurdering og beslutning

* Definer regler for automatisert beslutning (f.eks. terskler for indikatorer eller ML‑modeller).
* Implementer en modul som vurderer om handler skal utføres automatisk, krever bekreftelse eller kun logges.

## Fase 9: GitHub‑kobling og versjonskontroll

* Opprett GitHub‑actions for automatiske tester (T1–T10), CI og deployment av containere.
* Oppdater `CHANGELOG` for hver milepæl.
* Dokumenter alle moduler og oppdater `SYSTEM_OVERVIEW` etter behov.