```markdown
# 📊 Análise de Perdas na Colheita de Cana‑de‑Açúcar

Este projeto implementa um pipeline em Python para **carregar**, **analisar**, **gerar relatórios** e **armazenar** dados de perdas na colheita de cana‑de‑açúcar. Ele calcula percentuais de perdas entre colheita manual e mecanizada, gera recomendações, adiciona um carimbo de data/hora (`measured_at`) em cada registro e persiste tudo em um banco de dados (SQLite por padrão, ou Oracle se você tiver um XE configurado).

---

## 🚀 Funcionalidades

- **Leitura / escrita de JSON**  
  - Carrega dados brutos em `data/input/sample_data.json`.  
  - Gera relatório final em `data/output/report.json`, já com o campo `measured_at` (timestamp ISO).

- **Cálculo de perdas**  
  - Classe `Colheita` calcula produtividade (t/ha) e perdas (t e %).  
  - Funções auxiliares para estatísticas agregadas e geração de gráficos.

- **Recomendações inteligentes**  
  - Baseadas na comparação entre colheitas manuais e mecanizadas.  
  - Estratégias textuais (ex.: calibrar colhedora, revisar velocidade).

- **Timestamp**  
  - Cada registro recebe `measured_at` em `main.py` usando `datetime.now().isoformat()`.

- **Banco de dados**  
  - **SQLite** (`data/local.db`) como fallback automático.  
  - **Oracle** (opcional) via `config_oracle.json` + `cx_Oracle`.

- **Estrutura modular**  
  - Uso de subalgoritmos (funções e classes), listas, dicionários, JSON e POO.

---

## 🗂️ Estrutura de pastas

```text
analise-perdas-cana/
│
├─ .venv/                       # ambiente virtual Python  
├─ data/
│   ├─ input/
│   │   └─ sample_data.json     # dados de exemplo  
│   ├─ output/
│   │   └─ report.json          # relatório gerado (inclui `measured_at`)  
│   └─ local.db                 # banco SQLite (não versionado)  
│
├─ src/
│   ├─ data_loader.py           # carregamento/salvamento de JSON  
│   ├─ loss_calculator.py       # classe Colheita, estatísticas e cálculo de perdas  
│   ├─ report_generator.py      # adiciona recomendações e monta JSON final  
│   ├─ db_manager.py            # persistência SQLite/Oracle (insere `measured_at`)  
│   └─ main.py                  # script principal (gera timestamp)  
│
├─ config_db.json               # configuração SQLite padrão  
├─ config_oracle.json           # **(opcional)** credenciais Oracle  
├─ requirements.txt             # dependências Python  
└─ README.md                    # este arquivo
```

---

## ⚙️ Pré‑requisitos

- **Python 3.10+**  
- **Git**  
- (Opcional) **Oracle XE** + **SQL Developer**  
- (Opcional) **DB Browser for SQLite** ([sqlitebrowser.org](https://sqlitebrowser.org/))

---

## 📥 Instalação

1. **Clone** este repositório  
   ```bash
   git clone https://github.com/seu-usuario/analise-perdas-cana.git
   cd analise-perdas-cana
   ```

2. **Crie** e **ative** o virtualenv  
   ```bash
   python -m venv .venv
   # macOS / Linux
   source .venv/bin/activate
   # Windows
   .venv\Scripts\activate
   ```

3. **Instale** as dependências  
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configuração

### SQLite (padrão)

O `config_db.json` já aponta para:

```json
{
  "engine": "sqlite",
  "sqlite_file": "data/local.db"
}
```

### Oracle (opcional)

Se quiser usar Oracle, crie `config_oracle.json`:

```json
{
  "host":         "localhost",
  "port":         1521,
  "service_name": "XEPDB1",
  "username":     "SYSTEM",
  "password":     "sua_senha_sem_asterisco"
}
```

> Sem Oracle ativo, tudo rodará no SQLite automaticamente.

---

## ▶️ Como executar

```bash
python src/main.py
```

O script irá:

1. Carregar dados de `data/input/sample_data.json`  
2. Calcular perdas, estatísticas e recomendações  
3. Anexar `measured_at` (timestamp) a cada registro  
4. Salvar JSON em `data/output/report.json`  
5. Gravar registros (incluindo `measured_at`) na tabela `perdas_colheita` de `data/local.db`

---

## 🔍 Verificando o banco

1. Abra **DB Browser for SQLite**  
2. Clique em **Open Database**, selecione `data/local.db`  
3. Na aba **Browse Data**, escolha a tabela **perdas_colheita**

Você verá colunas como:

| id | fazenda   | safra | toneladas_m | toneladas_man | loss_percent | strategy                          | measured_at                 |
|----|-----------|-------|-------------|---------------|--------------|-----------------------------------|-----------------------------|
| 1  | Fazenda A | 2024  | 1000.0      | 950.0         | 5.26         | Ajustar calibração da colhedora.  | 2025-04-21T17:08:08.426346  |
| 2  | Sítio B   | 2024  |  800.0      | 780.0         | 2.56         | Parâmetros OK — sem ação necessária. | 2025-04-21T17:08:08.426349  |

---

## 📈 Possíveis melhorias

- Validação de entrada (tipos, valores obrigatórios).  
- CLI com `argparse` para configurar caminhos e engines.  
- **Upsert** em vez de truncar/inserir toda vez.  
- Exportar relatórios em CSV, Excel ou PDF.  

---

## 📚 Referências

- [Totvs: O que é agronegócio](https://www.totvs.com/blog/gestao-agricola/o-que-e-agronegocio)  
- Artigos Socicana, Embrapa, FAO, Croplife, etc.

---

> **Autor:** Rafael Jordão  
> **Data:** 21/04/2025  
