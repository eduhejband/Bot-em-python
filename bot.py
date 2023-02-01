import pandas as pd

#Carrega arquivo
df = pd.read_excel("Arquivo.xlsx")

# Converte a primeira coluna da esquerda
df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0])

# Filtro das linahs
df = df[df.iloc[:, 0].dt.strftime('%M:%S') == '00:00']

#Salva o as alterações
df.to_excel("Arquivo.xlsx", index=False, engine='openpyxl')

