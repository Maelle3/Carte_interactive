import folium
import database

lat_marseille = 43.2969500
lon_marseille = 5.3810700


def creation_carte():
    return folium.Map(location=[lat_marseille, lon_marseille], zoom_start=12, min_zoom=11)


def creation_marker(carte, x, y, message):
    popup = folium.Popup(message, max_width=600, min_width=600)
    return folium.Marker([x, y], popup=popup, icon=folium.Icon(icon='info-sign')).add_to(carte)


def adresses():
    db = database.ouverture_bdd()
    liste = []
    for key, value in db.items():
        adresse = value[0]["adresse"]
        if adresse not in liste:
            liste.append(adresse)
    return liste


def return_string(liste):
    str = "- " + liste[0]
    for i in range(1, len(liste)):
        str += ", " + liste[i]
    return str


def message():
    liste_adresse = adresses()
    db = database.ouverture_bdd()
    liste = []
    for adresse in liste_adresse:
        char = '<font size="+1"><B>' + adresse + "</B><br>"
        liste_key = []
        for key, value in db.items():
            if value[0]["adresse"] == adresse:
                if key not in liste_key:
                    liste_key.append(key)
                    char += '<i>' + '<a href=./Datas/PDF/' + value[0]["pdf"] + ' Target="_blank">Lien vers le pdf</a>' \
                            + '</i><br>'
                    char += return_string(value[0]["classification_pathologies"]) + " <br> " \
                            + return_string(value[0]["classification_lieux"]) + "<br>"
        char += '</font>'
        liste.append(char)
    return liste
