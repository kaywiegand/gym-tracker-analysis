"""Central path configuration. All paths are relative to the project root."""

from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Paths:
    root: Path = ROOT
    data: Path = ROOT / "data"
    raw: Path = ROOT / "data" / "raw"
    interim: Path = ROOT / "data" / "interim"
    processed: Path = ROOT / "data" / "processed"
    models: Path = ROOT / "data" / "models"
    img: Path = ROOT / "public" / "img"
    # Hand-off inputs
    tracker_export: Path = ROOT / "data" / "raw" / "tracker-export"  # exports from the app
    breaks: Path = ROOT / "data" / "raw" / "breaks.xlsx"  # table of training breaks


PATHS = Paths()
