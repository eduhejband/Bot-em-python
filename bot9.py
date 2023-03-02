import pandas as pd
import matplotlib.pyplot as plt

# Ler arquivo com as duas colunas separadas por tabulação
df = pd.read_csv("CAMINHO_ARQUIVO.csv", delimiter="\t")

# Definir os dados para o eixo x (datas e horas)
x = df.iloc[:, 1].values

# Definir os dados para as duas colunas
y1 = df.iloc[:, 2].values
y2 = df.iloc[:, 3].values
y3 = df.iloc[:, 4].values
y4 = df.iloc[:, 5].values
y5 = df.iloc[:, 6].values
y6 = df.iloc[:, 7].values

# Criar o primeiro gráfico comparando as colunas 1 e 2
plt.figure(figsize=(40, 16))
plt.subplot(2, 2, 1)
plt.plot(x, y1, color='blue', label='A')
plt.plot(x, y2, color='green', label='B')
plt.xlabel('Data')
plt.ylabel('Valores')
plt.title('Comparação entre A e B')
plt.legend()

# Criar o segundo gráfico comparando as colunas 2 e 3
plt.figure(figsize=(40, 16))
plt.subplot(2, 2, 2)
plt.plot(x, y1, color='blue', label='B')
plt.plot(x, y3, color='green', label='C')
plt.xlabel('Data')
plt.ylabel('Valores')
plt.title('Comparação entre B e C')
plt.legend()

# Criar o terceiro gráfico comparando as colunas 4 e 5
plt.figure(figsize=(40, 16))
plt.subplot(2, 2, 3)
plt.plot(x, y4, color='blue', label='C')
plt.plot(x, y5, color='green', label='D')
plt.xlabel('Data')
plt.ylabel('Valores')
plt.title('Comparação entre C e D')
plt.legend()

# Criar o quarto gráfico comparando as colunas 5 e 6
plt.figure(figsize=(40, 16))
plt.subplot(2, 2, 4)
plt.plot(x, y5, color='blue', label='D')
plt.plot(x, y6, color='green', label='E')
plt.xlabel('Data')
plt.ylabel('Valores')
plt.title('Comparação entre D e E')
plt.legend()

# Definir intervalo do eixo Y
plt.yticks([i/5 for i in range(11)])

# Ajustar layout e espaçamento entre os subplots
plt.tight_layout()

# Mostrar os gráficos
plt.show()
