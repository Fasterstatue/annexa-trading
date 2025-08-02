# ROADMAP

Dette dokumentet beskriver den fasevise utviklingsplanen for Annexa Trading. 

## Fase 1: Infrastruktur og grunnsystem

* Sett opp mappe‑ og modulstrukturen i repoet.
* Skriv `docker-compose.yaml` med tjenester for n8n, Whisper, Jupyter og plassholdere for Ollama og OpenRouter.
* Lag `.gitignore` og initial dokumentasjon (`README`, `SYSTEM_OVERVIEW`, `CHANGELOG`).
* Konfigurer n8n til å kjøre lokalt med volum for persistent data.

## Fase 2: Input og taleanalyse

* Implementer Whisper‑modulen som Docker‑container med OpenAI Whisper eller annen åpen kildekode‑modell.
* Lag en n8n‑flyt som tar lydfiler fra en monitorert mappe, sender dem til Whisper for transkripsjon og returnerer tekst.

## Fase 3: LLM‑integrasjon (Ollama + OpenRouter)

* Installer og konfigurer Ollama for lokal kjøring av LLM (LLaMA, Mistral eller lignende).
* Bygg Dockerfil for Ollama.
* Implementer n8n‑flyt som sender transkribert tekst til LLM for tolkning.
* Legg til fallback mot OpenRouter med gratis API‑nøkkel i tilfelle lokal modell ikke svarer.

## Fase 4: ML‑modell og analyse

* Lag notebooks i `jupyter/notebooks` for beregning av tekniske indikatorer som RSI og SMA.
* Implementer Python‑skript i `scripts/ml` for å trene en enkel modell (f.eks. XGBoost) for å predikere retning basert på historiske data.
* Integrer disse analysene i n8n‑flyten via API‑kall eller scripts.

## Fase 5: Simuleringsmotor

* Implementer et skript i `scripts/simulation` som tar signaler fra ML‑modellen og simulerer handler over historiske data.
* Lag en strategi‑loop med logging til SQLite i `db/history.sqlite`.
* Evaluer ytelsen (profit/loss, drawdown) og generer rapporter.

## Fase 6: Handelsintegrasjon (Nordnet eller alternativ)

* Utforsk API for Nordnet eller annen broker.
* Implementer modul i `scripts/trading_api` som sender ordre til demokonto.
* Integrer ordresending i n8n‑flyten basert på signaler og konfigurasjon.

## Fase 7: Dashbord og logg

* Lag et dashbord med f.eks. Streamlit eller Grafana i `dashboards/` for å visualisere signaler, historikk og kapitalutvikling.
* Oppdater n8n til å sende løpende statuser til dashbordet.

## Fase 8: Automatisk vurdering og beslutning

* Definer regler for automatisert beslutning (eks. terskel for modell‑prediksjon).
* Implementer modul som vurderer om handler skal utføres automatisk, krever bekreftelse eller kun logges.

## Fase 9: GitHub‑kobling og versjonskontroll

* Opprett GitHub‑actions for automatiske tester (T1–T10), CI og deployment av containere.
* Oppdater `CHANGELOG` for hver milepæl.
* Dokumenter alle moduler og oppdater `SYSTEM_OVERVIEW` etter behov.