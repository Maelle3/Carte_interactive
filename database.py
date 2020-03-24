import geocode as geo
import json
import recuperation as rec


def ouverture_bdd():
    with open('data.json', encoding='utf-8') as json_data:
        data_dict = json.load(json_data)
    return data_dict


def calcul_categorie(i, db):
    if db.loc[i].classe != 'Arrêtés de péril imminent, de Main Levée et de Réintégration partielle de la ville de Marseille':
        categorie = db.loc[i].classe
    else:
        url_split = db.loc[i].url.split("/")
        cat_partielle = url_split[-2]
        if cat_partielle == "Arretes-peril":
            if "odificatif" in db.loc[i]['nom_doc']:
                categorie = "Arrêtés de péril modificatif"
            else:
                categorie = "Arrêtés de péril"
        else:
            if "artiel" in db.loc[i]['nom_doc']:
                categorie = "Arrêtés de main levée partielle"
            else:
                categorie = "Arrêtés de main levée"
    return categorie


def ajout_ligne_peril(id, url, adresse, pathologies, date):
    db = ouverture_bdd()
    db[id] = [{"categorie": "Arrêtés de péril", "adresse": adresse, "longitude": geo.geocode(adresse)[0],
               "lattitude": geo.geocode(adresse)[1], "pathologies": pathologies,
               "classification_pathologies": rec.classification_pathologie(pathologies),
               "classification_lieux": rec.classification_lieu(pathologies), "url":  url, "date": date}]
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False)
    return None


def ajout_ligne_autre(categorie, id, url, adresse, date):
    db = ouverture_bdd()
    db[id] = [{"categorie": categorie, "adresse": adresse, "longitude": geo.geocode(adresse)[0],
               "lattitude": geo.geocode(adresse)[1], "url":  url, "date": date}]
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(db, f, ensure_ascii=False)
    return None

