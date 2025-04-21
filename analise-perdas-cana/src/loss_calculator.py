from typing import List, Dict


def calculate_loss(records: List[Dict]) -> List[Dict]:
    """Adiciona chave 'loss' com percentual de perda."""
    out = []
    for r in records:
        manual = r.get('toneladas_manual', 0)
        mecan = r.get('toneladas_mecanica', 0)
        loss = abs((manual - mecan) / manual * 100) if manual else 0
        r['loss'] = round(loss, 2)
        out.append(r)
    return out