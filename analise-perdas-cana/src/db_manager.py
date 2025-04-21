import json
import sqlite3
from typing import List, Dict

try:
    import oracledb
except ImportError:
    oracledb = None


class DBManager:
    def __init__(self, cfg_path='config_db.json'):
        # Carrega configuração (SQLite ou Oracle)
        cfg = json.load(open(cfg_path, 'r', encoding='utf-8'))
        self.engine = cfg['engine']
        if self.engine == 'sqlite':
            self.conn = sqlite3.connect(cfg['sqlite_file'])
        elif self.engine == 'oracle' and oracledb:
            o = cfg['oracle']
            self.conn = oracledb.connect(
                user=o['username'],
                password=o['password'],
                dsn=o['dsn']
            )
        else:
            raise RuntimeError(f'Engine inválida ou driver ausente: {self.engine}')
        self._ensure_table()

    def _ensure_table(self):
        # Cria tabela de perdas caso não exista
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS perdas_colheita (
              id            INTEGER PRIMARY KEY AUTOINCREMENT,
              fazenda       TEXT,
              safra         INTEGER,
              toneladas_m   REAL,
              toneladas_man REAL,
              loss_percent  REAL,
              strategy      TEXT
            )
        ''')
        self.conn.commit()

    def insert(self, recs: List[Dict]):
        # Insere as perdas no banco
        c = self.conn.cursor()
        for r in recs:
            c.execute('''
                INSERT INTO perdas_colheita
                  (fazenda, safra, toneladas_m, toneladas_man, loss_percent, strategy)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                r['fazenda'],
                r['safra'],
                r['toneladas_mecanica'],
                r['toneladas_manual'],
                r['loss'],
                r['strategy']
            ))
        self.conn.commit()

    def close(self):
        # Fecha a conexão
        self.conn.close()
