import json
import yaml
import requests
from pathlib import Path

def load_spec(path_or_url: str) -> dict:
    if path_or_url.startswith("http://") or path_or_url.startswith("https://"):
        response = requests.get(path_or_url)
        response.raise_for_status()
        return _parse_spec(response.text)
    else:
        path = Path(path_or_url)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        with open(path, "r") as f:
            return _parse_spec(f.read())

def _parse_spec(text: str) -> dict:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return yaml.safe_load(text)