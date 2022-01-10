from flask import Flask, request
import downloadImage
import os
import sendFile
import sendRequest
import threading
import execProc
import execProc


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello"


fileName = "" # Nome da imagem que vai ser pesquisada no GOOGLE
extesion = ".png"
idItemDB = 0 # id do item na base do sistema

@app.route("/addProcess", methods=["POST"])
def addProcess():

    id = request.get_json()["id"]
    name = request.get_json()["name"]
    fileData = '{"id": '+id+', "name": "'+name+'"}'
    arquivo = open('allProcess/'+id+".txt", "a")
    arquivo.write(fileData)

    return fileData



def getImageProduct():
    print('getImageProduct')
    print(request.get_json())
    try:
        idItemDB = request.get_json()["id"]
    except:
        print('Erro id')

    try:
        fileName = request.get_json()["name"] + " imagem"
    except:
        print('Erro nome')




    # Faz download da imagem pelo Google
    downloadImage.downloadimages(fileName)
    # Envia imagem para o repositorio do sistema e rescebe os dados da img pela resposta
    rapi = sendFile.sendPostFile(fileName + extesion)
    urlImage = rapi["urlImage"];
    rs = sendRequest.sendRequest('updateImageProduct', 'apiEstabelecimento', {"id": idItemDB, "url": urlImage})
    return {
        "imageResquest": fileName,
        "fileName": rapi["filename"],
        "urlImage": rapi["urlImage"],
        "rs": rs,
    }


def main():
    port = int(os.environ.get("PORT", 5000))
    threading.Thread(target=execProc.loopFunc, args=()).start()
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
