import os
import shutil

pasta = ""  # diretório para leitura



arquivos = os.listdir(pasta)


dest_folder = os.path.join(pasta, "PastaVazia")
if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

for i in arquivos:
    file_path = os.path.join(pasta, i)
    if os.path.getsize(file_path) == 0:
        print(f"Moving {file_path} to {dest_folder}")
        shutil.move(file_path, dest_folder)
