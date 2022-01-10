from flask import Flask, request
import downloadImage
import os
import sendFile
import sendRequest
import threading

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello"


fileName = "" # Nome da imagem que vai ser pesquisada no GOOGLE
extesion = ".png"
idItemDB = 0; # id do item na base do sistema

@app.route("/addProcess", methods=["GET"])
def addProcess():
    threading.Thread(target=getImageProduct())
    return "<h1> Save process </h1>"

@app.route("/getImageProduct", methods=["GET"])
def getImageProduct():
    
    if not request.args.get("id"): 
        return('Erro id item')
    
    idItemDB = request.args.get("id")

    try:
        fileName = request.args.get("image") + " imagem"
    except:
        return 'Falta parametro < image >'
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
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
