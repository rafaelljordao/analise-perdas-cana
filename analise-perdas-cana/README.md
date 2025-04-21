```markdown
# 📊 Análise de Perdas na Colheita de Cana‑de‑Açúcar

Este projeto em Python **carrega**, **analisa**, **gera relatórios** e **persiste** dados de perdas na colheita de cana‑de‑açúcar.  
Ele mede as diferenças entre colheita manual e mecanizada, sugere ações corretivas e salva tudo num JSON e num banco (SQLite por padrão, ou Oracle se você tiver).

---

## 🚀 Funcionalidades

- **JSON I/O**  
  - Entrada em `data/input/sample_data.json`  
  - Saída em `data/output/report.json`, agora com carimbo `measured_at` (timestamp da análise)
- **Cálculo de perdas**  
  - `Colheita`: produtividade, perda (toneladas + percentual)  
  - Estatísticas gerais e por tipo, gráfico comparativo
- **Recomendações**  
  - Sugestões automáticas de ajustes conforme perda percentual
- **Persistência em BD**  
  - **SQLite** local: `data/local.db`  
  - **Oracle XE** (opcional), via `config_oracle.json`
- **Arquitetura modular**  
  - Funções e classes (data loader, cálculo, relatório, DB)  
  - Uso de listas, dicionários e JSON

---

## 🗂️ Estrutura de pastas

```
analise-perdas-cana/
│
├─ .venv/                    # virtualenv Python  
├─ data/
│   ├─ input/
│   │   └─ sample_data.json  
│   ├─ output/
│   │   └─ report.json       # JSON gerado  
│   └─ local.db              # SQLite gerado  
│
├─ src/
│   ├─ data_loader.py        # ler / gravar JSON  
│   ├─ loss_calculator.py    # classe Colheita + estatísticas + gráfico  
│   ├─ report_generator.py   # adiciona `strategy` + `measured_at`  
│   ├─ db_manager.py         # cria tabela com coluna `measured_at`, insere no SQLite/Oracle  
│   └─ main.py               # fluxo principal  
│
├─ config_oracle.json        # **(opcional)** credenciais Oracle  
├─ requirements.txt          # deps  
└─ README.md                 # este arquivo  
```

---

## ⚙️ Pré‑requisitos

- Python 3.10+  
- Git  
- (Opcional) Oracle XE + SQL Developer  
- (Opcional) [DB Browser for SQLite](https://sqlitebrowser.org/)  

---

## 📥 Instalação e setup

1. **Clone**  
   ```bash
   git clone https://github.com/seu-usuario/analise-perdas-cana.git
   cd analise-perdas-cana
   ```
2. **Virtualenv**  
   ```bash
   python -m venv .venv
   # macOS / Linux
   source .venv/bin/activate
   # Windows
   .venv\Scripts\activate
   ```
3. **Deps**  
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configuração do Oracle (opcional)

Se quiser usar Oracle em vez de SQLite, crie na raiz um `config_oracle.json`:

```json
{
  "host":         "localhost",
  "port":         1521,
  "service_name": "XEPDB1",
  "username":     "SYSTEM",
  "password":     "sua_senha_sem_asterisco"
}
```

Caso falhe a conexão Oracle, o código automaticamente cai no **SQLite**.

---

## ▶️ Como rodar

```bash
python src/main.py
```

O que acontece:

1. **Carrega** `data/input/sample_data.json`  
2. **Calcula** perdas e estatísticas  
3. **Gera** recomendações e imprime no console  
4. **Adiciona** campo `"measured_at": "YYYY‑MM‑DD HH:MM:SS.ssssss"` em cada registro  
5. **Salva** JSON em `data/output/report.json`  
6. **Persiste** tudo em `data/local.db` (tabela `perdas_colheita`)

---

## 🔍 Ver o banco (SQLite)

1. Abrir **DB Browser for SQLite**  
2. **Open Database** → `data/local.db`  
3. Aba **Browse Data**, selecione tabela `perdas_colheita`  

| id | fazenda   | safra | toneladas_m | toneladas_man | loss_percent | strategy                            | measured_at               |
|----|-----------|-------|-------------|---------------|--------------|-------------------------------------|---------------------------|
| 1  | Fazenda A | 2024  | 1000.0      | 950.0         | 5.26         | Ajustar calibração da colhedora.    | 2025-04-21 17:08:08.426346|
| 2  | Sítio B   | 2024  |  800.0      | 780.0         | 2.56         | Parâmetros OK — sem ação necessária.| 2025-04-21 17:08:08.426349|

---

## 💡 Próximas melhorias

- Validação de entrada (tipos, campos obrigatórios)  
- CLI com `argparse` para definir paths na linha de comando  
- **Upsert** ao invés de truncate+insert no BD  
- Dash/Web UI para visualização interativa  
- Suporte a PostgreSQL/MySQL  

---

## 📚 Referências

- [Totvs: O que é agronegócio](https://www.totvs.com/blog/gestao-agricola/o-que-e-agronegocio)  
- Socicana: Perdas na colheita de cana  
- Embrapa, FAO, Croplife, etc.

---

> **Autor:** Rafael Jordão  
> **Data:** 21/04/2025  
> **Versão:** 1.1 – adiciona `measured_at` no JSON e no BD  
