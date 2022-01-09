import requests
import json
import config

def sendPostFile(params):
        url = config.URL + "?acao=updateImageProduct&api=apiEstabelecimento"
        print(url, params)
        r = requests.get(url, data=params)
        return r.text



# sendPostFile({"id": "287", "url": "teste"})
