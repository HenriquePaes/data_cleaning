import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# configuração do display de colunas
pd.set_option("display.max_columns", 320)

# obtenção dos dados
dados = pd.read_csv("./recursos/diabetes.csv")

# visualização dos 10 primeiros registros
#print(dados.head(10))

#print("Tabela de Correlação dos dados\n")
#print(dados.corr(method="pearson"))

# releitura dos dados
colunas = ['Preg', 'Gluc', 'Bloo', 'Skin', 'Insu', 'BMI', 'DPF', 'Age', 'Out']
dados2 = pd.read_csv("./recursos/diabetes.csv", names=colunas)

# visualizando dados faltantes
print((dados2.isnull().sum() / len(dados2['Preg'])) * 100)

# impressão do grafico mapa de calor
plt.figure(figsize=(10,10))
sns.heatmap(dados2.corr())
plt.show()