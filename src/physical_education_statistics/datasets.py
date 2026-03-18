from __future__ import annotations

from pathlib import Path

import pandas as pd

DATA_FILES = {
    "tgmd": "tgmd_dataset.csv",
    "motor_competence": "motor_competence_dataset.csv",
    "growth": "growth_dataset.csv",
    "longitudinal_activity": "longitudinal_activity_dataset.csv",
    "motor_learning": "motor_learning_experiment.csv",
}


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def data_dir() -> Path:
    return project_root() / "data"


def load_dataset(name: str) -> pd.DataFrame:
    try:
        filename = DATA_FILES[name]
    except KeyError as exc:
        raise ValueError(f"Dataset desconhecido: {name}. Opções: {sorted(DATA_FILES)}") from exc
    return pd.read_csv(data_dir() / filename)
