import requests

import json

def httpFetcher(url : str, params = None, headers = None ):
    with requests.Session() as session:
        res = session.get(url, params = params, headers = headers )
        return res
    
# Prend la reponse et donne le format
def formatResponse(res, format : str):
    if format == "json":
        return res.json()
    return res.text() 

def collectData(fileName, path, res) : 
    f = open(path + '\\' + fileName, "w")
    f.write(json.dumps(res))