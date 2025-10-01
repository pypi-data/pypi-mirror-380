"""Shepherd launcher - minimal clean file.

This implementation is intentionally small and single-purpose:
- computes simple per-phase scores from backtest_results.csv (if present),
- writes JSON artifacts under <outdir>/reports/, keeps a 5-entry chronicle,
- writes a compact HTML dashboard, and optionally opens it on Windows.

This file is written atomically to avoid leftover duplicated fragments.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

VERSION = "0.1.4"
PHASES = [
    "Presence",
    "Awareness",
    "Guidance",
    "Decision",
    "Action",
    "Reflection",
    "Continuity",
]


def compute_scores(csv_path: Path) -> List[Dict]:
    """Parse CSV with numeric columns and return phase list."""
    if not csv_path.exists():
        raise FileNotFoundError(csv_path)

    breakout_vals: List[float] = []
    move_vals: List[float] = []
    with csv_path.open("r", encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            parts = [p.strip() for p in line.split(",") if p.strip()]
            if not parts:
                continue
            try:
                a = float(parts[0])
                b = float(parts[1]) if len(parts) > 1 else 0.0
            except Exception:
                continue
            breakout_vals.append(a)
            move_vals.append(abs(b))

    if not breakout_vals:
        raise ValueError("no numeric rows in CSV")

    avg_breakout = sum(breakout_vals) / len(breakout_vals)
    avg_move = sum(move_vals) / len(move_vals) if move_vals else 0.0
    norm_move = max(0.0, min(1.0, avg_move / 10.0))
    base_score = (max(0.0, min(1.0, avg_breakout)) + norm_move) / 2.0

    phases: List[Dict] = []
    for i, name in enumerate(PHASES):
        offset = (i - (len(PHASES) // 2)) * 0.02
        score = max(0.0, min(1.0, base_score + offset))
        phases.append({"name": name, "score": round(score, 3), "fix_sweep": True})

    return phases


def _embed_image_as_data_uri(image_path: Path) -> Optional[str]:
    try:
        raw = image_path.read_bytes()
        b64 = base64.b64encode(raw).decode("ascii")
        ext = image_path.suffix.lower()
        if ext in (".jpg", ".jpeg"):
            mime = "image/jpeg"
        elif ext == ".png":
            mime = "image/png"
        else:
            mime = "application/octet-stream"
        return f"data:{mime};base64,{b64}"
    except Exception:
        return None


def launch_dashboard(
    shepherd_img: str,
    run_data: Dict,
    chronicle: List[Dict],
    artifacts: Path,
    do_open: bool,
    embed_image: bool,
) -> None:
    stamp = run_data["run_id"]
    html_path = artifacts / f"dashboard_{stamp}.html"

    rows = "".join(
        f"<tr><td>{p['name']}</td><td>{p['score']:.3f}</td></tr>"
        for p in run_data["phases"]
    )
    chronicle_items = "".join(
        f"<li>{c['run_id']}: {c['overall_score']:.3f}</li>" for c in chronicle
    )

    img_url = ""
    if embed_image and shepherd_img:
        emb = _embed_image_as_data_uri(Path(shepherd_img))
        img_url = emb if emb else shepherd_img
    elif shepherd_img:
        img_url = shepherd_img

    html = (
        '<!doctype html><html><head><meta charset="utf-8"><title>Shepherd Shrine</title>'
        "<style>body{font-family:serif;background:#f5efe0;padding:18px}table{width:100%;}</style></head><body>"
    )
    html += f"<h1>Shepherd Shrine</h1><div>Run: {stamp}</div>"
    if img_url:
        html += f'<div><img src="{img_url}" style="max-width:200px"></div>'
    html += f"<table>{rows}</table><h3>Chronicle</h3><ul>{chronicle_items}</ul></body></html>"

    artifacts.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html, encoding="utf-8")
    latest = artifacts / "dashboard_latest.html"
    latest.write_text(html, encoding="utf-8")

    if do_open:
        try:
            if sys.platform.startswith("win"):
                os.startfile(str(latest))
            elif sys.platform.startswith("darwin"):
                os.system(f"open {str(latest)}")
            else:
                os.system(f"xdg-open {str(latest)}")
        except Exception:
            pass


def run_shepherd(
    shepherd_img: str = "",
    outdir: str = "artifacts",
    do_open: bool = True,
    embed_image: bool = False,
) -> int:
    artifacts = Path(outdir)
    reports = artifacts / "reports"
    artifacts.mkdir(parents=True, exist_ok=True)
    reports.mkdir(parents=True, exist_ok=True)

    csv_path = Path("backtest_results.csv")
    try:
        phases = (
            compute_scores(csv_path)
            if csv_path.exists()
            else [
                {"name": name, "score": round(0.3 + i * 0.02, 3), "fix_sweep": True}
                for i, name in enumerate(PHASES)
            ]
        )
    except Exception:
        phases = [
            {"name": name, "score": round(0.3 + i * 0.02, 3), "fix_sweep": True}
            for i, name in enumerate(PHASES)
        ]

    overall_score = sum(p["score"] for p in phases) / len(phases)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    run_data = {
        "run_id": stamp,
        "overall_score": overall_score,
        "phases": phases,
        "version": VERSION,
    }
    (reports / f"run_{stamp}.json").write_text(
        json.dumps(run_data, indent=2), encoding="utf-8"
    )
    (reports / "run_latest.json").write_text(
        json.dumps(run_data, indent=2), encoding="utf-8"
    )

    chronicle_path = reports / "chronicle.json"
    if chronicle_path.exists():
        try:
            chronicle = json.loads(chronicle_path.read_text(encoding="utf-8"))
        except Exception:
            chronicle = []
    else:
        chronicle = []

    if not any(entry.get("run_id") == stamp for entry in chronicle):
        chronicle.append({"run_id": stamp, "overall_score": overall_score})
    chronicle = chronicle[-5:]
    chronicle_path.write_text(json.dumps(chronicle, indent=2), encoding="utf-8")

    try:
        launch_dashboard(
            shepherd_img, run_data, chronicle, artifacts, do_open, embed_image
        )
    except Exception as e:
        print(f"Error generating dashboard: {e}")
        print(f"Reports available at: {reports}")
        return 2

    print(f"Artifacts written to: {reports}")
    return 0


def main(argv: List[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="shepherd_launch", description="Shepherd's Shrine dashboard generator")
    p.add_argument("--shepherd-image", default="", help="path to shepherd image")
    p.add_argument("--outdir", default="artifacts", help="output directory")
    p.add_argument("--no-open", action="store_true", help="do not open the dashboard")
    p.add_argument(
        "--embed-image", action="store_true", help="embed image as base64 in HTML"
    )
    p.add_argument("--version", action="store_true", help="print version and exit")
    args = p.parse_args(argv)

    if args.version:
        print(VERSION)
        return 0

    do_open = not args.no_open
    return run_shepherd(args.shepherd_image, args.outdir, do_open, args.embed_image)


if __name__ == "__main__":
    raise SystemExit(main())
