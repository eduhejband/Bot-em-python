#completando ainda a ideia do bot6 listando os arquivos faltantes

import os

def comparar_arquivos(arquivo1, arquivo2, caminho_saida):
    with open(arquivo1, 'r') as f1, open(arquivo2, 'r') as f2:
        linhas1 = f1.readlines()
        linhas2 = f2.readlines()

        dados_faltantes = []
        for i in range(len(linhas1)):
            linha1 = linhas1[i].strip()
            linha2 = linhas2[i].strip()

            if linha2 == '':
                linha2 = linha1
            elif linha1 == '':
                dados_faltantes.append(linha2)
                linhas1[i] = ''
                linhas2[i] = ''
                continue
                

            if linha1 != linha2:
                print(f"Linha {i + 1} não corresponde.")
                print(f"Arquivo 1: {linha1}")
                print(f"Arquivo 2: {linha2}")

        with open(arquivo1, 'w') as f1, open(arquivo2, 'w') as f2:
            f1.write('\n'.join(linhas1))
            f2.write('\n'.join(linhas2))

        if dados_faltantes:
            with open(caminho_saida, 'w') as f:
                f.write('\n'.join(dados_faltantes))

if __name__ == '__main__':
    pasta1 = '/caminho/para/pasta1'
    pasta2 = '/caminho/para/pasta2'
    caminho_saida = '/caminho/para/dados_faltantes.txt'

    for nome_arquivo in os.listdir(pasta1):
        arquivo1 = os.path.join(pasta1, nome_arquivo)
        arquivo2 = os.path.join(pasta2, nome_arquivo + '_r')

        comparar_arquivos(arquivo1, arquivo2, caminho_saida)
