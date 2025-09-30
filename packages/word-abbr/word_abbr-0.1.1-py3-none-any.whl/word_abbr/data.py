import json
from pathlib import Path
from typing import Dict

class DataManager:
    def __init__(self) -> None:
        self.data_file: Path = Path(__file__).parent / 'data' / "abbreviations.json"

    def load_abbreviations(self) -> Dict[str, str]:
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                data: dict = json.load(f)
                if isinstance(data, dict):
                    return {k.lower(): v for k, v in data.items()}
                return {}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
