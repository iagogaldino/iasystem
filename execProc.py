import datetime
from time import sleep
import json
from flask import Flask, request
import downloadImage
import sendFile
import sendRequest
import os


rangeLoop = 999999999

def loopFunc():
    for i in range(rangeLoop):
        print(i)
        try:
            listFiles()
        except:
            pass
        sleep(3)    #in seconds


def listFiles():
    pasta = './allProcess'
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            # print(os.path.join(arquivo))
            openFile(diretorio +"/"+ arquivo)

def openFile(fileName):
    with open(fileName, "r") as file:
        data = json.loads(file.read())
        # print(fileName)
        file.close()
        getImageProduct(data['id'], data['name'], fileName)


def getImageProduct(idItemDB, name, fileNameDelete):
    print('getImageProduct')
    if not idItemDB:
        print('not id')
        return
    if not name:
        print('not name')
        return

    fileName = name

    # ----- Faz download da imagem pelo Google
    downloadImage.downloadimages(fileName)
    # ----- Envia imagem para o repositorio do sistema e rescebe os dados da img pela resposta
   
    rapi = sendFile.sendPostFile(fileName + '.png')
   
    urlImage = rapi["urlImage"]
    fname = rapi["filename"]
  
  
    rs = sendRequest.sendRequest('updateImageProduct', 'apiEstabelecimento', {"id": idItemDB, "url": urlImage})
    deleteFile(fileNameDelete)
    res = {
        "imageResquest": fileName,
        "fileName": fname,
        "urlImage": urlImage,
        "rs": rs
    }

    print(res)


def deleteFile(fileName):
    print('deleteFile:::' + fileName)
    if os.path.exists(fileName):
        for i in range(1):
            print('Arquivo encontrado == remover ===>' + fileName)
            os.remove(fileName)
            sleep(5)    #in seconds
             
    else:
        print("The file does not exist")


# listFiles()
# loopFunc() 
# openFile() 
# deleteFile('./allProcess/287 copy.txt') 
