import pandas as pd
import requests

df = pd.read_excel('Pasta1.xlsx')

for i,cnpj in enumerate(df["cnpj"]):
    cnpj = str(cnpj).zfill(14).replace(".","").replace("-","").replace("/","") #para tratar os caracteres do cnpj, transformando para string, colocando zeros a esquerda caso necessário
    resposta = requests.get(f'https://brasilapi.com.br/api/cnpj/v1/{cnpj}')
    dados = resposta.json()
    situacao = dados["descricao_situacao_cadastral"]
    df.at[i, 'situacao'] = situacao #acessa a celula i da coluna >>situacao<< e salva a variavel situacao
    print(f'{cnpj} = {situacao}')
df.to_excel('Pasta1.xlsx', index=False) #salva a situação no arquivo original