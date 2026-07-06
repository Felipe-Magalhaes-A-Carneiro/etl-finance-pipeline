import sys
from extract import extrair_dados
from transform import transformar_dados
from load import carregar_dados

def executar_pipeline():
    print("Iniciando PIPELINE")

    try:
        # 1. Fase de Extração
        print("ETL - Extraindo dados da API externa")
        dados_brutos = extrair_dados()
        print("ETL - Extração concluída")

        # 2. Fase de Transformação
        print("ETL - Aplicando regras de negócio e limpando dados via Pandas")
        df_tratado = transformar_dados(dados_brutos)
        print("ETL - Dados transformados")

        # 3. Fase de Carga
        print("ETL - Conectando ao banco de dados e pesistindo as informações...")
        carregar_dados(df_tratado)


        print("Finalizando PIPELINE com sucesso de PONTA A PONTA")

    except Exception as erro:
        print(f"[ERRO CRITÍCO] Falha durante a execução do pipeline: {erro}", file=sys.stderr)
        print("=== PIPELINE INTERROMPIDO ===", file=sys.stderr)

if __name__ == "__main__":
    executar_pipeline()