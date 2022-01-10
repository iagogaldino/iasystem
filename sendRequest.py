import requests
import json
import config



def sendRequest(action, apiName, params):  # "?acao=updateImageProduct&api=apiEstabelecimento"
       
        url = config.URL + "?acao=" + action + "&api=" + apiName
        print(url, params)
        r = requests.post(url, data=params, headers=config.headers)
        return json.loads(r.text)

# print(sendRequest('updateImageProduct', 'apiEstabelecimento', {"id": "287", "url": "teste"}))
