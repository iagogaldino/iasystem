from flask import Flask, request
import downloadImage
import os
import sendFile
import sendRequest

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello"


fileName = "Guarana lata 350 ml icon"
extesion = ".png"


@app.route("/getImageProduct", methods=["GET"])
def getImageProduct():
    # fileName = request.args.get("image") + " icon"
    # r = downloadImage.downloadimages(fileName)
    # rapi = sendFile.sendPostFile(fileName + extesion)
    rs = sendRequest.sendPostFile({"id": "287", "url": "teste"})
    return rs
    # return {
    #     "imageResquest": fileName,
    #     "fileName": rapi["filename"],
    #     "urlImage": rapi["urlImage"],
    # }


def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
