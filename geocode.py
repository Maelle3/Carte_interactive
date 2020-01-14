import requests
import os

url_geocode = "http://api-adresse.data.gouv.fr/search/"
adresse_test = "11 rue Moustier Marseille"


def geocode(adresse):
    reponse = requests.get(url_geocode, params = {"q": adresse})
    lon = reponse.json().get("features")[0].get("geometry").get("coordinates")[0]
    lat = reponse.json().get("features")[0].get("geometry").get("coordinates")[1]
    return lat, lon

def recup_adresse(texte):
    fichier = open(texte, "r", encoding = "latin-1")
    res = str(fichier.read()).partition("immeuble sis ")[2].partition("-")[0].partition("")[0]
    return res



