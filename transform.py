import pandas as pd
from datetime import datetime

def transformar_dados(dados_brutos):
    lista_moedas = []

    for chave, info in dados_brutos.items():
        lista_moedas.append({
            "moeda": info["code"],
            "nome": info["name"],
            "valor_compra": float(info["bid"]),
            "valor_venda": float(info["ask"]),
            "data_consulta": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    df = pd.DataFrame(lista_moedas)
    return df