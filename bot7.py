#completando a função do código anterior, para remover as linhas que estao zeradas no arquivo normal dentro do _r

import os
import datetime

def compare_files(dir1, dir2):
    files1 = [f for f in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, f))]
    files2 = [f for f in os.listdir(dir2) if os.path.isfile(os.path.join(dir2, f))]
    
    twin_files = []
    for file1 in files1:
        if file1[:-2] + "_r" in files2:
            twin_files.append((file1, file1[:-2] + "_r"))
            
    dates_to_remove = []
    for twin in twin_files:
        file1 = os.path.join(dir1, twin[0])
        file2 = os.path.join(dir2, twin[1])
        
        with open(file1, "r") as f1, open(file2, "r") as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            
            for i, (line1, line2) in enumerate(zip(lines1, lines2)):
                if line1.strip() == "" or line2.strip() == "":
                    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    dates_to_remove.append((i, date_time))
            
    for file2 in files2:
        with open(os.path.join(dir2, file2), "r") as f2:
            lines = f2.readlines()
        
        with open(os.path.join(dir2, file2), "w") as f2:
            for i, line in enumerate(lines):
                if (i, line.strip()) not in dates_to_remove:
                    f2.write(line)

dir1 = "/caminho/para/o/primeiro/diretorio"#pasta sem o _r aqui
dir2 = "/caminho/para/o/segundo/diretorio" #pasta_r aqui
compare_files(dir1, dir2)
