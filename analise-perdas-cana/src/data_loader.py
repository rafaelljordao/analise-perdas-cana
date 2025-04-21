import json


def load_data(path: str):
    """Lê JSON de entrada e retorna lista de dicts."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
