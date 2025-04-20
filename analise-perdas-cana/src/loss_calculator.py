from typing import Dict

def calculate_loss(record: Dict) -> float:
    """
    Recebe um registro com as chaves:
      - toneladas_mecanica
      - toneladas_manual
    Retorna o percentual de perda:
      (mecânica - manual) / mecânica * 100
    """
    m = record['toneladas_mecanica']
    manual = record['toneladas_manual']
    if m == 0:
        return 0.0
    return (m - manual) / m * 100
