# SYSTEM OVERVIEW

Dette dokumentet gir en oversikt over modulene i Annexa Trading‑systemet og hvordan de henger sammen.

## Moduler

| Modul           | Beskrivelse                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **n8n**         | Orkestrerer arbeidsflyten. Henter data, kaller andre moduler og styrer signalbehandling.                                                     |
| **Whisper**     | Konverterer tale til tekst for stemmekommandoer. Kjøres i en egen Docker‑container.                                                         |
| **Ollama**      | Lokal LLM for å tolke naturlig språk og generere forslag eller svar.                                                                        |
| **OpenRouter**  | Fallback‑tjeneste mot skybasert LLM i tilfelle lokal modell feiler.                                                                          |
| **Jupyter + ML**| Kjøring av ML‑notebooks og scripts for beregning av tekniske indikatorer og modeller.                                                        |
| **Datafeed/API**| Henter markedsdata. I offline‐miljøer leses data fra en lokal CSV (se `data/sample_stock.csv` og `scripts/data/fetch_sample.py`). Når nettaksess eller API‐nøkler er tilgjengelig kan modulen hente sanntidsdata fra eksterne kilder.                                                                    |
| **Simulering**  | Tester strategier på historiske eller live data uten å gjøre reelle handler.                                                                 |
| **Handelskanal**| Integrasjon mot en broker (f.eks. Nordnet) for å sende ordrer.                                                                               |
| **Dashbord**    | Visualiserer resultater og statuser (Streamlit, Grafana, etc.).                                                                              |
| **SQLite/VectorDB** | Lokal database for lagring av data, historikk og eventuelle embeddings.                                                                 |

## Flyt

1. **n8n** starter automatiske arbeidsflyter basert på tidsplan eller brukerinput.
2. Hvis input kommer som tale, sendes lydfilen til **Whisper** for transkripsjon.
3. Transkribert tekst blir analysert av **LLM** (Ollama) eller **OpenRouter** for tolkning av intensjon.
4. **n8n** henter markedsdata via Datafeed/APIs og kjører ML‑analyser i **Jupyter** eller scripts.
5. Basert på analyser genereres trading‑signaler. Disse sendes til **simuleringsmodulen** for evaluering.
6. Hvis simuleringsresultatene oppfyller kriterier, sendes ordrer til **handelskanalen**. Ellers logges resultatene.
7. **Dashbordet** oppdateres kontinuerlig med nye signaler, historikk og statistikk.