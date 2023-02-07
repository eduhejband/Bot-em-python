import os
import subprocess

pasta_ler = "" # pasta com arquivos zerados
pasta_corrigir = "" # pasta com arquivos corrigidos

for i in os.listdir(pasta_ler):
    pasta_ler_path = os.path.join(pasta_ler, i)
    if os.path.getsize(pasta_ler_path) == 0:
        pasta_corrigir_path = os.path.join(pasta_corrigir, i[:-2])
        if os.path.isfile(pasta_corrigir_path):
            subprocess.run(["ncks", "-O", "-v", "VARIÁVEIS", pasta_corrigir_path, pasta_ler_path])
            print(f"Aplicando ncks {pasta_corrigir_path} em {pasta_ler_path}")
        else:
            print(f"Arquivo {pasta_corrigir_path} não encontrado")
