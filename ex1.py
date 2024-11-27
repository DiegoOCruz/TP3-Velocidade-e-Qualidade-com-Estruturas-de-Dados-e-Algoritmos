import os

def listar_arquivos(diretorio):
    for nome in os.listdir(diretorio):
        caminho = os.path.join(diretorio, nome)
        if os.path.isdir(caminho):
            listar_arquivos(caminho)
        else:
            print(caminho)

diretorio = "C:\\Users\\diego\\OneDrive\\Documentos"
listar_arquivos(diretorio)