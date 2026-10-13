# PROCESS_LOG – gym-tracker-analysis

## 2026-10-13 — Foundation

**Was passiert ist**
- Projektstruktur nach Workspace-Standard angelegt (`data/`, `notebooks/`, `public/`, `scripts/`, `src/gym_tracker_analysis/`, `tests/`), uv-Umgebung, `PATHS`-Config, Smoke-Test.
- Alter, unstrukturierter Versuch: fünf Notebooks und PNGs nach `notebooks/archive/` verschoben (nichts gelöscht).
- Git-Repo initialisiert, Remote gesetzt; nichts gestaged oder committet.

**Entscheidungen**
- Ein Case über zwei Repos: `gym-tracker-analysis` (Analyse) und `gym-tracker-app` (Produkt als Ergebnis der Analyse und künftige Datenquelle).
- Alte Notebooks bleiben lokal archiviert und aus Git heraus (`.gitignore`); `data/` ist komplett ausgeschlossen (Gesundheitsdaten, Repo wird öffentlich).
- BIA wird später nur als Veränderung seit dem ersten Scan gezeigt, nicht in absoluten Werten.
- Durchgängig dritte Person: "training data of one person" / "a single trainee".

**Nächster Schritt**
- Export-Vertrag mit der App definieren (Phase 1).
