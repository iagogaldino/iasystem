import requests
import json
import config

def sendPostFile(file):
    fileName = 'downloads/'+file
    try:
        with open(fileName, 'rb') as f:
            r = requests.post(config.URL + "?acao=upload_img_galeria&api=apiEstabelecimento&shownameondone", headers=config.headers, data={"nome_imagem_text": "guinho"}, files={"imagem": f})
            jsonResponse = json.loads(r.text)
            print(jsonResponse)
            return jsonResponse
    except:
        print('Imagem não encontrada ===> ' + fileName)
        return False
    

# sendPostFile('coca cola.png')
