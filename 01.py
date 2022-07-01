# Ecrire une fonction qui permet de recuperer les données de l'API et les stocke dans un fichier csv
# utiliser les fonctions precedentes pour collecter la donnée, réajuster si necessaire la fonction qui permet de fetcher la donnée en prenant en compte le type de fichier

import requests

import json
import csv


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


if __name__ == "__main__" :
    url = "https://api.datamuse.com/words" 
    params, headers = {"rel_jjb" : "ocean"} , {}
    res = httpFetcher(url, params = params)
    rep = formatResponse(res, 'json')
    #print(type(rep))
    #print(type(json.dumps(rep)))
    collectData("ocean.csv", "files", rep )
    
    