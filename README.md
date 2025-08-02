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

### Datainnhenting (Fase 2)

Det er ikke alltid mulig å hente data over nett i denne test‑miljøet. For å komme i gang
har vi inkludert et lite eksempelsett med aksjekurser i katalogen `data/`. Du finner en
CSV‑fil `sample_stock.csv` med én måneds daglig bar‐data for en fiktiv aksje. Tilhørende
`scripts/data/fetch_sample.py` inneholder funksjonen `load_sample_data()` som leser
CSV‑filen inn i et Pandas DataFrame. Eksempel:

```python
from scripts.data import load_sample_data

df = load_sample_data()
print(df.head())
```

Dette gir deg et konsistent datagrunnlag til å utvikle og teste indikatorskript
og simuleringslogikk. Når nettaksess eller API‐nøkler er tilgjengelig, kan du
utvide `fetch_sample.py` med funksjoner som henter data fra eksterne tjenester.

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