import pandas as pd
import geocode as geo


#liste des classifications de pathologies
##'classification_pathologies'=["affaissemnt", "altération", "risque de chutes", "fissures", "fissures", "débris", "affaissement", "basculement d'escalier", "risque d'effondrement"]


def ouverture_bdd(bdd):
    return pd.read_csv(bdd)


def ajout_ligne(bdd, url, adresse, pathologies, lieu):
    db = ouverture_bdd(bdd)
    longeur = len(db)
    print(geo.geocode(adresse))
    db.loc[longeur] = [adresse, geo.geocode(adresse)[0], geo.geocode(adresse)[1], pathologies, lieu, url]
    db.to_csv(bdd, index=False)
    return None


def affiche_bdd(bdd):
    return ouverture_bdd(bdd)


def get_coordonnees_url(bdd, url):
    db = ouverture_bdd(bdd)
    i = 0
    url_found = False
    while not url_found:
        if db.loc[i].lien_artété != url:
            i += 1
        else:
            return db.loc[i].lon, db.loc[i].lat


def get_coordonnées_adresse(bdd, adresse):
    db = ouverture_bdd(bdd)
    i = 0
    adresse_found = False
    while not adresse_found:
        if db.loc[i].adresse != adresse:
            i += 1
        else:
            return db.loc[i].lon, db.loc[i].lat


def get_url_adresse(bdd, adresse):
    db = ouverture_bdd(bdd)
    i = 0
    adresse_found = False
    while not adresse_found:
        if db.loc[i].adresse != adresse:
            i += 1
        else:
            return db.loc[i].url