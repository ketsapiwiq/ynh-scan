# YunoScan

Contains:
- `apps.toml`: the amended list of apps, with CPEs added
    - this was built with `add_cpes.py`, `cpe.csv`, and `add_cpes.diff`. The diff unfortunately formats the TOML a bit (the arrays), but I couldn't fix `python.diff.invalid` to avoid this.
- `security.toml`: the ideal resulting file (example)
- `scan.py`: main script for fetch vulns for `apps.toml` from vuln db
- `vulns/`: folder with each app as subfolder, `results.json` inside with raw results from NVD

## Running `scan.py`
- `python3 -m venv venv`
- `source .env` (edit from `.env.example`, API key not really needed, it's just faster)
- `python scan.py`