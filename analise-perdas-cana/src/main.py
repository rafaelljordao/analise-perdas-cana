from data_loader import load_data
from loss_calculator import calculate_loss
from report_generator import generate_report, save_to_json

def main():
    # 1) Carregar dados
    path_in = 'data/input/sample_data.json'
    registros = load_data(path_in)

    # 2) Calcular perdas e gerar relatório
    # (aqui usamos nossa função de report_generator)
    registros_completos = generate_report(registros)

    # 3) Exibir no console
    print("Relatório de perdas (%):")
    for r in registros_completos:
        print(f"{r['fazenda']} (safra {r['safra']}): {r['loss']:.2f}%")

    # 4) Salvar JSON de saída
    path_out = 'data/output/report.json'
    save_to_json(registros_completos, path_out)
    print(f"\nRelatório salvo em {path_out}")

if __name__ == '__main__':
    main()
