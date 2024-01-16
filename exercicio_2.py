import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns", 42)
pd.set_option("display.width", 320)
dados = pd.read_csv("./recursos/2015-building-energy-benchmarking.csv")
print(dados)

plt.figure(figsize=(10,30))
sns.heatmap(dados.corr())
plt.show()
