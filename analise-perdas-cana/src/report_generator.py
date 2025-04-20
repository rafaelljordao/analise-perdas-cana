import json
from typing import List, Dict

def generate_report(records: List[Dict]) -> List[Dict]:
    """
    Recebe uma lista de registros e retorna uma nova lista
    onde cada dicionário ganhou a chave 'loss' (percentual).
    """
    report = []
    for rec in records:
        rec_with_loss = rec.copy()
        m = rec['toneladas_mecanica']
        manual = rec['toneladas_manual']
        rec_with_loss['loss'] = ((m - manual) / m * 100) if m else 0.0
        report.append(rec_with_loss)
    return report

def save_to_json(records: List[Dict], path: str):
    """
    Salva a lista de registros em um arquivo JSON.
    """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
