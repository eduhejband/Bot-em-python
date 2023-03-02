#Bot para ler duas colunas de abas diferentes e criar uma terceira aba para colar essas duas colunas apagando as linhas que tiveram um espaço em branco

import pandas as pd
import numpy as np

# Lê a primeira planilha e armazena em um dataframe
df1 = pd.read_excel("arquivo.xlsx",sheet_name='bkp_observado',usecols=[1, 2],dtype={1: np.datetime64, 2: np.float64})

# Lê a segunda planilha e armazena em um outro dataframe
df2 = pd.read_excel("arquivo2.xlsx",sheet_name='bkp_modelado',usecols=[0, 6], dtype={0: np.datetime64, 6: np.float64})

# Remove as linhas vazias de ambos os dataframes
df1.dropna(inplace=True)
df2.dropna(inplace=True)

# Cria uma lista para armazenar os dados combinados
combined_data = []

# Realiza a comparação entre as colunas das duas planilhas
for index1, row1 in df1.iterrows():
    for index2, row2 in df2.iterrows():
        if row1[1] == row2[0]:
            combined_data.append([row1[1], row1[2], row2[6]])
            df_combined = pd.DataFrame(combined_data, columns=["Data", "Coluna Observada", "Coluna Modelada"])
            df_combined.to_excel("LAJEADO_2023 (1).xlsx", sheet_name='teste',index=False)
