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

def recup_pathologie(texte):
    fichier = open(texte, "r", encoding = "latin-1")
    res = str(fichier.read()).partition("pathologies suivantes :")[2].partition("Considérant")[0]
    return res

##Il reste à gérer les bas de page

for i in os.listdir("./Datas/TXT"):
    print(recup_pathologie("./Datas/TXT/" + i))