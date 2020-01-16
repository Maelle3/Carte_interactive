import pandas as pd
import geocode as geo
import json
import recuperation as rec


# liste des classifications de pathologies
##'classification_pathologies'=["affaissemnt", "altération", "risque de chutes", "fissures", "fissures", "débris", "affaissement", "basculement d'escalier", "risque d'effondrement"]


# def ouverture_bdd(bdd):
#     return pd.read_csv(bdd)

def ouverture_bdd(bdd):
    with open('data.json') as json_data:
        data_dict = json.load(json_data)
    return data_dict




def ajout_ligne(bdd,id, pdf, adresse, pathologies):
    db = ouverture_bdd(bdd)
    db[id] = [{"adresse" : adresse, "longitude" : geo.geocode(adresse)[0], "lattitude" : geo.geocode(adresse)[1],
               "pathologies" : pathologies, "classification_pathologies" : rec.classification_pathologie(pathologies),
               "classification_lieux" : rec.classification_lieu(pathologies) , "pdf" :  pdf}]
    with open('data.json', 'w') as f:
         json.dump(db, f, ensure_ascii=False)
    return None

# def affiche_bdd(bdd):
#     return ouverture_bdd(bdd)


def get_coordonnees_url(bdd, url):
    db = ouverture_bdd(bdd)
    i = 0
    url_found = False
    while not url_found:
        if db.loc[i].lien_artété != url:
            i += 1
        else:
            return db.loc[i].lon, db.loc[i].lat


# def get_coordonnées_adresse(bdd, adresse):
#     db = ouverture_bdd(bdd)
#     i = 0
#     adresse_found = False
#     while not adresse_found:
#         if db.loc[i].adresse != adresse:
#             i += 1
#         else:
#             return db.loc[i].lon, db.loc[i].lat


# def get_url_adresse(bdd, adresse):
#     db = ouverture_bdd(bdd)
#     i = 0
#     adresse_found = False
#     while not adresse_found:
#         if db.loc[i].adresse != adresse:
#             i += 1
#         else:
#             return db.loc[i].url







# data = {}
# data2 = {"addresse" : "adresse1", "longitude" : 1, "lattitude" : 1, "classification" : ["fissures", "effondrement"]}
# data["id1"] = [data2]
# data3 = {"addresse" : "bonjour", "longitude" : 2, "lattitude" : 2, "classification" : ["moisissures", "effondrement"]}
# data["id2"]  = [data3];
#
#
# with open('data.json', 'w') as f:
#     json.dump(data, f)
