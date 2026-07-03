# Pipeline de Ingestão e ETL de Dados Financeiros (End-to-End)

## 📌 Contexto do Projeto
No cenário corporativo moderno, a tomada de decisões estratégicas depende da agilidade e da confiabilidade no acesso a indicadores de mercado. 

Este projeto simula um cenário real de Engenharia de Dados: a automação do processo de extração, transformação e carga (ETL) de dados macroeconômicos (cotações de moedas) para alimentar data warehouses ou ferramentas de Business Intelligence (BI).

O objetivo principal é garantir que dados brutos vindos de uma API externa sejam capturados de forma segura, higienizados contra inconsistências e persistidos de maneira estruturada em um banco de dados relacional local, preparando a infraestrutura para futuras análises preditivas.

---

## 🏗️ Arquitetura da Solução
O pipeline foi desenvolvido seguindo a arquitetura tradicional de ETL:

1. **Extração (Extract):** Consumo automatizado de dados em tempo real (JSON) via API pública de economia.
2. **Transformação (Transform):** Limpeza, filtragem de atributos irrelevantes, conversão de tipos de dados (tipagem numérica correta) e enriquecimento com data/hora da ingestão utilizando a biblioteca Pandas.
3. **Carga (Load):** Persistência dos dados estruturados em tabelas SQL usando engenharia de mapeamento objeto-relacional (ORM).

[ API AwesomeAPI ] ➔ [ Script Python / Requests ] ➔ [ Tratamento / Pandas ] ➔ [ Banco de Dados SQL ]

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Linguagem Principal:** Python 3
* **Manipulação de Dados:** Pandas (DataFrames)
* **Conexão HTTP:** Requests
* **Mapeamento e Banco de Dados:** SQLAlchemy / SQLite
* **Controle de Versão:** Git & GitHub

---

## 📁 Estrutura do Repositório
* `extract.py`: Módulo responsável pelas requisições HTTP e validação do status da API.
* `transform.py`: Módulo que processa a estrutura de dados bruta e aplica as regras de negócio.
* `load.py`: Módulo responsável pela conexão com o banco e append das novas linhas.
* `main.py`: Orquestrador central que executa os três passos do pipeline em ordem.
* `requirements.txt`: Arquivo de gerenciamento de dependências com versionamento congelado.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3** instalado em sua máquina.

### 1. Clonar o Repositório
```bash
git clone https://github.com/Felipe-Magalhaes-A-Carneiro/etl-finance-pipeline
cd etl-finance-pipeline
```

### 2. Instalar as Dependências
Utilize o gerenciador de pacotes para instalar as versões exatas de produção:
```bash
pip install -r requirements.txt
```

### 3. Rodar o Pipeline
Execute o script principal para rodar o processo de ponta a ponta:
```bash
python main.py
```
*Observação: Após a execução, um arquivo de banco de dados chamado `mercado_dados.db` será gerado automaticamente na raiz do projeto com a tabela `cotacoes_diarias` preenchida.*

---

## 🎯 Próximos Passos (Evolução da Arquitetura)
Como parte do meu plano de especialização contínua em Engenharia de Dados, as próximas etapas planejadas para este repositório incluem:
* Migrar a infraestrutura local para a Nuvem (**AWS Lambda** para computação serverless).
* Substituir o armazenamento local por um Data Lake (**AWS S3**).
* Implementar ferramentas de orquestração de fluxo como **Apache Airflow**.

---