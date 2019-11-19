import folium
import database

lat_marseille = 43.2969500
lon_marseille = 5.3810700


def creation_carte():
    return folium.Map(location=[lat_marseille, lon_marseille], zoom_start=12, min_zoom=11)


def creation_marker(carte, x , y, message):
    return folium.Marker([x, y], popup=message, icon=folium.Icon(icon='info-sign')).add_to(carte)

def adresses(bdd):
    db = database.ouverture_bdd(bdd)
    l = len(db)
    liste = []
    for i in range(l):
        adresse = db.loc[i].adresse
        if adresse not in liste:
            liste.append(adresse)
    return liste


def message(bdd):
    liste_adresse = adresses(bdd)
    db = database.ouverture_bdd(bdd)
    liste = []
    for i in liste_adresse:
        db2 = db.loc[db.adresse==i, :]
        char = ""+ i + "\n"
        liste_url = []
        l = len(db2)
        for j in range(l):
             u = db2.iloc[j].url
             if u not in liste_url:
                liste_url.append(u)
                char+= u + "\n"
             char+= db2.iloc[j].classification_pathologies + " " + db2.iloc[j].classification_lieux + "\n"

        liste.append(char)
    return liste

