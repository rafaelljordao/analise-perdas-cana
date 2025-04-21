import json
from typing import List, Dict

from strategy_recommender import recommend_strategy


def generate_report(records: List[Dict]) -> List[Dict]:
    for r in records:
        r['strategy'] = recommend_strategy(r)
    return records


def save_to_json(records: List[Dict], path: str):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)