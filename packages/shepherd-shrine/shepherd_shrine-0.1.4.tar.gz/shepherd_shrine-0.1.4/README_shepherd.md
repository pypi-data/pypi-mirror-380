Shepherd's Shrine — README

This repository includes `shepherd_launch.py`, a small utility that generates a stylized HTML "Shepherd’s Shrine" dashboard showing seven canonical phases, their scores, and a chronicle of recent runs.

Quick usage

Install locally (editable) and use the console script:

```bash
pip install -e .
shepherd --help
shepherd --no-open --outdir my_artifacts
```

Run with defaults (will attempt to open the generated dashboard on Windows):

```bash
python shepherd_launch.py
```

Run without opening and write artifacts to a custom directory:

```bash
python shepherd_launch.py --no-open --outdir my_artifacts --shepherd-image "C:\\path\\to\\Shepherd.jpg"
```

Files created

- `artifacts/dashboard_<stamp>.html` — generated dashboard per run
- `artifacts/dashboard_latest.html` — copy of the most recent dashboard
- `artifacts/reports/run_<stamp>.json` — run metadata
- `artifacts/reports/chronicle.json` — last 5 runs

Notes

- The script uses a placeholder scoring function; replace with real metrics as needed.
- On non-Windows systems the script falls back to `webbrowser.open` if automatic open is enabled.
 - In CI or headless environments, pass `--no-open`.
 - You can embed a logo or image via `--shepherd-image` or keep the minimal default styling.
