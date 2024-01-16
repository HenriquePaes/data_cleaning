import pandas as np

# setando o numero de visualizacao de colunas
np.set_option('display.max_columns', 42)
# obtendo os dados
dados = np.read_csv('./recursos/2015-building-energy-benchmarking.csv')
# visualização dos 10 primeiros registros
#print(dados.head(10))

# substituição dos valores faltantes da coluna ENERGYSTARScore pela mediana
#print(dados.columns)
dados['ENERGYSTARScore'] = dados['ENERGYSTARScore'].fillna(dados['ENERGYSTARScore'].median())
print(dados['ENERGYSTARScore'])
# valida se existe alguma linha com dados faltantes
print('Percentual de dados faltantes: {:.2f}'.format((dados['ENERGYSTARScore'].isnull().sum() / len(dados['OSEBuildingID']) * 100)))