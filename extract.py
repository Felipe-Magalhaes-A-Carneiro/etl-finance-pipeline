import requests

def extrair_dados():
    url = "https://awesomeapi.com.br"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        return dados
    else:
        raise Exception(f"Erro ao acessar API: {response.status_code}")