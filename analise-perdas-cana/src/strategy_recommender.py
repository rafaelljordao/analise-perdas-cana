from typing import Dict


def recommend_strategy(record: Dict) -> str:
    loss = record.get('loss', 0)
    if loss > 10:
        return 'Revisar programação de colheita manual.'
    if loss > 5:
        return 'Ajustar calibração da colhedora.'
    return 'Parâmetros OK — sem ação necessária.'