import folium
import database


lat_marseille = 43.2969500
lon_marseille = 5.3810700


def creation_carte():
    return folium.Map(location = [lat_marseille, lon_marseille], zoom_start = 12, min_zoom = 11)


def creation_marker(carte, x, y, message):
    popup = folium.Popup(message, max_width=600,  min_width=600)
    return folium.Marker([x, y], popup=popup, icon=folium.Icon(icon='info-sign')).add_to(carte)


def adresses(bdd):
    db = database.ouverture_bdd(bdd)
    l = len(db)
    liste = []
    for key, value in db.items():
        adresse = value[0]["adresse"]
        if adresse not in liste:
            liste.append(adresse)
    return liste


def message(bdd):
    liste_adresse = adresses(bdd)
    db = database.ouverture_bdd(bdd)
    liste = []
    for adresse in liste_adresse:
        char = '<font size="+1"><B>'+ adresse + "</B><br>"
        liste_url = []
        for key, value in db.items():
            if  value[0]["adresse"] == adresse :
                 u = value[0]["url"]
                 if u not in liste_url:
                    liste_url.append(u)
                    char += '<i>'+u + '</i><br>'
                 char += str(value[0]["classification_pathologies"]) + " <br> " + str(value[0]["classification_lieux"])+ "<br>"
        char += '</font>'
        liste.append(char)
    return liste

