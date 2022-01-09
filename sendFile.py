import requests
import json
import config

def sendPostFile(file):
    fileName = file

    with open('downloads/'+fileName, 'rb') as f:
        r = requests.post(config.URL + "?acao=upload_img_galeria&api=apiEstabelecimento&shownameondone", data={"nome_imagem_text": "guinho"}, files={"imagem": f})
        jsonResponse = json.loads(r.text)
        # print(jsonResponse['filename'])
        return jsonResponse

# sendPostFile('coca cola.png')
