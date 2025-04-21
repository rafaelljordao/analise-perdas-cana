from data_loader import load_data
from loss_calculator import calculate_loss
from report_generator import generate_report, save_to_json
from db_manager import DBManager


def main():
    recs = load_data('data/input/sample_data.json')
    recs = calculate_loss(recs)
    recs = generate_report(recs)
    save_to_json(recs, 'data/output/report.json')
    print('✅ JSON salvo em data/output/report.json')

    db = DBManager('config_db.json')
    db.insert(recs)
    db.close()
    print(f'✅ Dados gravados em banco [{db.engine}]')

if __name__ == '__main__':
    main()