
#Bot para ler duas colunas e apagar as linhas que tiverem um espaço em branco
import pandas as pd


df = pd.read_excel("LAJEADO_2023 (1).xlsx",sheet_name="teste")

df.dropna(how='any', inplace=True)

df.to_excel("LAJEADO_2023 (1).xlsx",sheet_name="teste", index=False)
