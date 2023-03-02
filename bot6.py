#Bot para ler pastas gêmeas e excluir a linha em branco de todas pastas que tem "_r"

import os
import subprocess

pasta_ler = "" # pasta com arquivos zerados
pasta_corrigir = "" # pasta com arquivos corrigidos

def remove_linha_branco(arquivo):
    with open(arquivo, "r") as f:
        linhas = f.readlines()
    with open(arquivo, "w") as f:
        for linha in linhas:
            if linha.strip():
                f.write(linha)

for i in os.listdir(pasta_ler):
    pasta_ler_path = os.path.join(pasta_ler, i)
    pasta_corrigir_path = os.path.join(pasta_corrigir, i[:-2] + "_r")

    if os.path.isfile(pasta_corrigir_path):
        remove_linha_branco(pasta_ler_path)
        remove_linha_branco(pasta_corrigir_path)
        subprocess.run(["ncks", "-O", "-v", "VARIÁVEIS", pasta_corrigir_path, pasta_ler_path])
        print(f"Aplicando ncks {pasta_corrigir_path} em {pasta_ler_path}")
    else:
        print(f"Arquivo {pasta_corrigir_path} não encontrado")
