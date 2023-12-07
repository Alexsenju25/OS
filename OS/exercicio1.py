#Crie uma função que peça para o usuario criar o caminho de uma pasta/diretorio e que liste aquivos e que, liste os arquivos de um deretorio utilizando a biblioteca
import os

def listar_arquivos():
    caminho_diretorio = input("Informe o caminho do diretório")
    #Listar os arquivos do diretório passado

    arquivos = os.listdir(caminho_diretorio)

    print("Os arquivos do diretório passado são: ")

    for arquivo in arquivos:
        print(arquivo)
    else:
        print("Diretório inválido")


listar_arquivos ()
