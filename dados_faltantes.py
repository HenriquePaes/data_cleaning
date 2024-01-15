import pandas as np

# configura o numero de colunas que serão visualizados
np.set_option("display.max_columns", 42)
# obtem os dados
dados = np.read_csv("./recursos/athlete_events.csv")
# realiza a impressão dos dados
#print(dados.head(5))

### OPÇÕES DE AJUSTE DE DADOS FALTANTES ###
#dados2 = dados
#print(dados2.head(5))

# remove a linha inteira onde contém dados faltantes (NAN)
#dados2 = dados2.dropna()
#print(dados2)

# comparação do tamanho dos datasets
#print("\nBASE ORIGINAL")
#print("Número de linhas: {0}\nNúmero de colunas: {1}.".format(dados.shape[0], dados.shape[1]))
#print("\nBASE SEM DADOS FALTANTES")
#print("Número de linhas: {0}\nNúmero de colunas: {1}.".format(dados2.shape[0], dados2.shape[1]))
#print("--------------------------\nTotal de {} linhas excluidas.".format(dados.shape[0] - dados2.shape[0]))

### ANÁLISE DOS DADOS FALTANTES ###
enulo = dados.isnull()
#print(enulo.head(100))

faltantes = dados.isnull().sum()
#print(faltantes)

faltantes_percentual = (dados.isnull().sum() / len(dados['ID'])) * 100
#print(faltantes_percentual)

### SUBSTITUIÇÃO DE DADOS FALTANTES ###
dados['Medal'].fillna('Nenhuma', inplace=True)
dados['Age'].fillna(dados['Age'].mean(), inplace=True)
dados['Height'].fillna(dados['Height'].mean(), inplace=True)
dados['Weight'].fillna(dados['Weight'].mean(), inplace=True)

faltantes_percentual = (dados.isnull().sum() / len(dados['ID'])) * 100
print(dados.head(100))
print(faltantes_percentual)