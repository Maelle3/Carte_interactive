import requests

url_geocode = "http://api-adresse.data.gouv.fr/search/"
adresse_test = "11 rue Moustier Marseille"


def geocode(adresse):
    reponse = requests.get(url_geocode, params = {"q": adresse})
    lon = reponse.json().get("features")[0].get("geometry").get("coordinates")[0]
    lat = reponse.json().get("features")[0].get("geometry").get("coordinates")[1]
    return lat, lon


