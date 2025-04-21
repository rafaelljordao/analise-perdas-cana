```markdown
# 📊 Análise de Perdas na Colheita de Cana‑de‑Açúcar

Este projeto implementa um sistema em Python para **carregar**, **analisar**, **gerar relatórios** e **armazenar** dados de perdas na colheita de cana‑de‑açúcar. Além de calcular percentuais de perdas entre colheita manual e mecanizada, ele gera recomendações e ainda persiste os resultados em um banco (SQLite por padrão, ou Oracle se você tiver um XE configurado).

---

## 🚀 Funcionalidades

- **Leitura / escrita de JSON**  
  - Carrega dados de entrada em `data/input/sample_data.json`.  
  - Gera relatório em `data/output/report.json`.
- **Cálculo de perdas**  
  - Classe `Colheita` calcula produtividade e perda (em toneladas e percentual).  
  - Funções de estatística e gráfico de comparação.
- **Banco de dados**  
  - **SQLite** (fallback automático).  
  - **Oracle** (se você criar `config_oracle.json` e tiver serviço rodando).
- **Relatório e recomendações**  
  - Texto no console + JSON.  
  - Sugestões de ajustes com base nas perdas.
- **Estrutura modular**  
  - Subalgoritmos (funções/procedimentos), listas, dicionários, JSON, classes.

---

## 🗂️ Estrutura de pastas

```txt
analise-perdas-cana/
│
├─ .venv/                    # ambiente virtual Python  
├─ data/
│   ├─ input/
│   │   └─ sample_data.json  # dados de exemplo  
│   └─ output/
│       └─ report.json       # relatório gerado  
│
├─ src/
│   ├─ data_loader.py        # ler/gravar JSON  
│   ├─ loss_calculator.py    # classe Colheita, estatísticas e gráfico  
│   ├─ report_generator.py   # montar relatório + recomendações  
│   ├─ db_manager.py         # persistência SQL (SQLite/Oracle)  
│   └─ main.py               # script principal  
│
├─ config_oracle.json        # **(opcional)** credenciais Oracle  
├─ requirements.txt          # dependências  
└─ README.md
```

---

## ⚙️ Pré‑requisitos

- Python 3.10+  
- Git  
- (Opcional) Oracle XE + SQL Developer  
- (Opcional) [DB Browser for SQLite](https://sqlitebrowser.org/)  

---

## 📥 Instalação

1. Clone este repositório  
   ```bash
   git clone https://github.com/seu-usuario/analise-perdas-cana.git
   cd analise-perdas-cana
   ```
2. Crie e ative um *virtualenv*  
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # macOS / Linux
   .venv\Scripts\activate       # Windows
   ```
3. Instale as dependências  
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 Configuração do Oracle (opcional)

Se quiser testar conexão Oracle, crie um `config_oracle.json` na raiz:

```json
{
  "host":         "localhost",
  "port":         1521,
  "service_name": "XEPDB1",
  "username":     "SYSTEM",
  "password":     "sua_senha_sem_asterisco"
}
```

> **Nota**: se não houver Oracle ativo ou faltar credenciais, o projeto usará **automatically** um banco SQLite local em `data/local.db`.

---

## ▶️ Como rodar

```bash
python src/main.py
```

O fluxo será:

1. **Carregar** `data/input/sample_data.json`  
2. **Calcular** perdas e estatísticas  
3. **Gerar** recomendações e imprimir no console  
4. **Salvar** JSON em `data/output/report.json`  
5. **Persistir** resultados em `data/local.db`  

---

## 🔍 Visualizando o banco

1. Abra o **DB Browser for SQLite**  
2. **Open Database** → selecione `data/local.db`  
3. Aba **Browse Data** → tabela `perdas_colheita`  

Você verá colunas como:

| id | fazenda   | safra | toneladas_m | toneladas_man | loss_percent | strategy                            |
|----|-----------|-------|-------------|---------------|--------------|-------------------------------------|
| 1  | Fazenda A | 2024  | 1000.0      | 950.0         | 5.26         | Ajustar calibração da colhedora.    |
| 2  | Sítio B   | 2024  |  800.0      | 780.0         | 2.56         | Parâmetros OK — sem ação necessária.|

---

## 📈 Melhorias sugeridas

- **Timestamp** em cada registro (`measured_at`) para histórico completo.  
- Validação de dados de entrada (tipos e campos obrigatórios).  
- CLI com `argparse` para parâmetros de entrada/saída.  
- **Upsert** no banco ao invés de sempre deletar tudo.

---

## 📚 Referências

- [Totvs: O que é agronegócio](https://www.totvs.com/blog/gestao-agricola/o-que-e-agronegocio)  
- Socicana: Perdas na colheita de cana  
- Embrapa, FAO, Croplife, etc.

---

> **Autor:** Rafael Jordão  
> **Data:** 21/04/2025 
