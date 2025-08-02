# Annexa Trading – Lokalt KI‑basert system for automatisert analyse

Dette prosjektet bygger et robust, modulbasert og 100 % lokalt KI/ML‑system for tradingbeslutninger.
Systemet kjører i containere (Docker) og er gratis og åpen kildekode. Kjernemodulene (de første vi bygger) er:

* **n8n** – orkestrerer datainnhenting, flyt og signalbehandling.
* **Jupyter + ML** – kjører tekniske indikatorer og maskinlæringsmodeller for å generere trading‑signaler.
* **GitHub** – lagrer kildekode, dokumentasjon og roadmap.

I senere faser kan vi også legge til valgfrie moduler som:

* **Whisper** – konverterer tale til tekst for stemmekommandoer.
* **Ollama / LLM** – lokal språkmodell som tolker signaler og svarer på spørsmål.

Systemet inneholder også en **simuleringsmotor** for trygg testkjøring før reell handel aktiveres.

## Kom i gang

1. Sørg for at Docker og Docker Compose er installert.
2. Klon dette repoet og gå inn i katalogen:

    ```bash
    git clone https://github.com/fasterstatue/annexa-trading.git
    cd annexa-trading
    ```

3. Start alle tjenestene med Docker Compose:

    ```bash
    docker-compose up -d
    ```

Dette vil starte n8n, Whisper, Jupyter og plassholdere for Ollama og OpenRouter. Jupyter vil være tilgjengelig på `http://localhost:8888` og n8n på `http://localhost:5678`.

## Struktur

Prosjektet er modulbasert. Se `docs/SYSTEM_OVERVIEW.md` for en fullstendig oversikt over arkitekturen og 
`docs/ROADMAP.md` for den fasevise utviklingsplanen.

## Lisens

Dette prosjektet distribueres under en åpen kildekode‑lisens. Se `LICENSE` (kommer senere) for detaljer.