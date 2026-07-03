from sqlalchemy import create_engine

def carregar_dados(df):
    # Realiza conexao com o banco de dados e criará o arquivo SQLite
    engine = create_engine("sqlite:///mercado_dados.db")

    # Salva o DataFrame como uma tabela SQL
    df.to_sql("cotacoes_diarias", con = engine, if_exists = "append", index = False)
    print("Dados foram carregados com sucesso!")

