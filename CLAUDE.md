# CLAUDE.md – gym-tracker-analysis

> Projektspezifische Anweisungen für Claude Code.
> Ergänzt die globale CLAUDE.md aus dem Workspace.

---

## Projekt

| Feld | Inhalt |
| :--- | :--- |
| Slug | `gym-tracker-analysis` |
| Typ | DA (Data Analysis) |
| Stack | Polars · Plotly · Jupyter · uv · pytest · ruff |
| Python | >=3.11 |

## Kontext-Einstieg

1. `PROCESS_LOG.md` lesen — aktueller Projektstand
2. `ROADMAP.md` lesen — offene Phasen und Tasks
3. `BACKLOG.md` lesen — offene Einzelpunkte
4. Globale `CLAUDE.md` aus `/Users/kaywiegand/Workspace/` gilt weiterhin

## Beziehung zu gym-tracker-app

Ein Portfolio-Case, zwei Repos (Muster wie `zh-tram-data` / `zh-tram-flow`):

- **`gym-tracker-analysis`** (dieses Repo) — Analyse-Hälfte: Trainingslogs, BIA-Scans, Tabelle der Trainingspausen.
- **`gym-tracker-app`** (lokal `/Users/kaywiegand/Workspace/kw-gym-tracker`, GitHub `kaywiegand/gym-tracker-app`) — Produkt-Hälfte: Self-hosted Tracking-App, setzt die Findings als Regeln um und ist künftig die Datenquelle.

Übergabe-Eingänge: `data/raw/tracker-export/` (Exporte aus der App) und `data/raw/breaks.xlsx`.
Gemeinsame Definitionen (e1RM, gewichtete Sätze, Volumen-Schwellen, Farben) müssen in beiden Repos identisch sein.

## Konventionen (verbindlich)

- **Anonymität in jeder Datei** (README, Meta-Files, Code, Kommentare, Notebooks): Der Datensatz wird beschrieben als "training data of one person" / "a single trainee", dritte Person. Nie angeben oder andeuten, dass die Daten dem Autor gehören. Nie Geschlecht, Körpergrösse, Alter oder BMI nennen. Kein Vorname in Dateien.
- **Privacy:** Alles unter `data/` ist Gesundheitsdaten und darf nie getrackt werden (`.gitignore`). Das Repo wird später öffentlich.
- Code, Identifier, Kommentare, README: Englisch. Andere Meta-Files: Deutsch möglich. Keine Emojis.
- Meta-Files enthalten keine Zahlen/Findings aus Notebooks.
- `notebooks/archive/` = alter, unstrukturierter Versuch; lokal behalten, nicht in Git.

## Hinweise

- Der lokale Ordnername `kw-gym-performance` ist **temporär** und wird am Ende in `gym-tracker-analysis` umbenannt (bis dahin nicht ändern).
- Env: `uv sync`, Tests: `uv run pytest`, Lint: `uv run ruff check .`
