import json
from typing import List, Dict
from datetime import datetime            # <<< novo import

from strategy_recommender import recommend_strategy


def generate_report(records: List[Dict]) -> List[Dict]:
    """
    Para cada registro:
      1) calcula a strategy
      2) acrescenta o timestamp de medição
    """
    for r in records:
        # 1) estratégia existente
        r['strategy'] = recommend_strategy(r)
        # 2) timestamp de quando rodou o relatório
        r['measured_at'] = datetime.now().isoformat(sep=' ')
    return records


def save_to_json(records: List[Dict], path: str):
    """
    Salva a lista de dicts (já com strategy + measured_at) em JSON.
    """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
