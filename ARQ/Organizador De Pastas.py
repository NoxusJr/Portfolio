#FEITO PARA PORTFÓLIO E ESTUDO S2

import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione Uma Pasta")

lista_arquivos = os.listdir(caminho)

#DICIONÁRIO

locais = {
    "imagens": [".png", ".jpg", ".gif", ".bmp", ".webp", ".tiff", ".raw"],
    "textos": [".txt", ".pdf", ".doc", ".docx"],
    "musicas": [".mp3", ".wav", ".aac"],
    "videos": [".mp4", ".mov", ".wmv", ".avi", ".avchd", ".mkv"],
    "planilhas":[ ".xls", ".xlsx", ".csv"],
    "scripts":[".js",".py",".html", ".css", ".php",".java"]
}

for arquivo in lista_arquivos:

# EXTRAINDO O NOME E A EXTENSÃO DO ARQUIVO

    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:

# SE NÃO TIVER A PASTA, CRIA A PASTA

            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")

# MOVE OS ARQUIVOS PARA A PASTA CRIADA  

#                     CAMINHO ANTIGO                 CAMINHO NOVO
#                           |                              |
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")