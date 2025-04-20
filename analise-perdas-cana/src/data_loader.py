import json
from typing import List, Dict

def load_data(path: str) -> List[Dict]:
    """
    Lê um arquivo JSON de registros de colheita e retorna uma lista de dicionários.
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
