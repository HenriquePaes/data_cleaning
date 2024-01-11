import pandas as pd

# configura o pandas para mostrar todas as colunas
pd.set_option('display.max_columns', 42)
# efetua a leitura da base de dados
dados = pd.read_csv('./recursos/2015-building-energy-benchmarking.csv')
# mostra os 10 primeiros registros
print(dados.head(10))
# efetua a leiura dos tipos de dados de todas as colunas
print(dados.dtypes)

# vamos forçar a alteração do tipo da coluna 'DataYear' para object, simulando uma base com tipo errado
dados['DataYear'] = dados['DataYear'].astype('object')

# efetua a leiura dos tipos de dados de todas as colunas
print('----------------------------------------------------------\n{}'.format(dados.dtypes))