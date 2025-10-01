import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

from shepherd.shepherd_launch import main


def test_happy_path(tmp_path):
    outdir = tmp_path / "artifacts"
    rc = main(["--no-open", "--outdir", str(outdir)])
    assert rc == 0
    assert (outdir / "dashboard_latest.html").exists()
    reports = outdir / "reports"
    assert reports.exists()
    # there should be at least one run_*.json
    json_runs = list(reports.glob("run_*.json"))
    assert len(json_runs) >= 1
    assert (reports / "run_latest.json").exists()


def test_embed_missing_image(tmp_path):
    outdir = tmp_path / "artifacts2"
    rc = main(
        [
            "--no-open",
            "--outdir",
            str(outdir),
            "--embed-image",
            "--shepherd-image",
            "nonexistent.jpg",
        ]
    )
    assert rc == 0
    assert (outdir / "dashboard_latest.html").exists()
    reports = outdir / "reports"
    assert reports.exists()
