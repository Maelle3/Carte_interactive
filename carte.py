import folium
import database

lat_marseille = 43.2969500
lon_marseille = 5.3810700


def creation_carte():
    return folium.Map(location=[lat_marseille, lon_marseille], zoom_start=12, min_zoom=11)


def creation_marker(carte, x, y, message):
    popup = folium.Popup(message, max_width=600, min_width=600)
    return folium.Marker([x, y], popup=popup, icon=folium.Icon(icon='home', icon_color='white')).add_to(carte)


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
        char = '<font size="+1"><B>' + adresse + "</B><br><br>"
        liste_key = []
        liste_key_date = []
        liste_date = []
        for key, value in db.items():
            if value[0]["adresse"] == adresse:
                if key not in liste_key:
                    liste_key.append(key)
                    liste_key_date.append([key, value[0]["date"]])
                    liste_date.append(value[0]["date"])
        liste_date.sort(reverse=True)
        sorted_list = []
        for i in liste_date:
            for k in liste_key_date:
                if k[1] == i:
                    sorted_list.append(k)
        for couple in sorted_list:
            char += '<i>' + '<a href=./Datas/PDF/' + db[couple[0]][0][
                "pdf"] + ' Target="_blank">Lien vers le pdf</a>' + '</i> ' + db[couple[0]][0]["date"] + '<br>'
            char += return_string(db[couple[0]][0]["classification_pathologies"]) + " <br> " \
                + return_string(db[couple[0]][0]["classification_lieux"]) + "<br><br>"

        char += '</font>'
        liste.append(char)

    return liste
