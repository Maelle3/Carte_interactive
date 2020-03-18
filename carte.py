# -*- coding: utf-8 -*-
import folium
import database
from branca.element import Template, MacroElement
from gestion_erreurs import ajout_erreur

lat_marseille = 43.2969500
lon_marseille = 5.3810700


def creation_carte():
    return folium.Map(location=[lat_marseille, lon_marseille], zoom_start=12, min_zoom=11)


palette = dict()
palette["Arrêtés de déconstruction"] = "black"
palette["Arrêtés d'interdiction d'occuper"] = "darkred"
palette["Arrêtés de péril"] = "red"
palette["Arrêtés de péril modificatif"] = "red"
palette["Arrêtés d'insécurité imminente des équipements communs"] = "lightred"
palette["Arrêtés d'évacuation et de réintégration"] = "orange"
palette["Arrêtés de périmètres de sécurité sur voie publique"] = "beige"
palette["Arrêtés de police générale"] = "beige"
palette["Arrêtés de main levée partielle"] = "lightgreen"
palette["Arrêtés de main levée"] = "green"
palette["Diagnostics d'ouvrages"] = "purple"


def creation_marker(carte, x, y, message):
    popup = folium.Popup(message[0], max_width=600, min_width=600)
    return folium.Marker([x, y], popup=popup, icon=folium.Icon(icon='home', icon_color='white', color=palette[message[1]])).add_to(carte)


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


def message(liste_adresse, db_csv):
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
        # liste_date.sort(reverse=True)
        liste_date.reverse()
        sorted_list = []
        for i in liste_date:
            for k in liste_key_date:
                if k[1] == i:
                    sorted_list.append(k)
        cat_last = db[sorted_list[0][0]][0]["categorie"]
        for couple in sorted_list:
            cat = db[couple[0]][0]["categorie"]
            char += '<U>' + cat + '</U><br>'
            try:
                char += '<i>' + '<a href=' + db[couple[0]][0]["url"] + ' Target="_blank">Lien vers le pdf</a>' + '</i> '\
                            + db[couple[0]][0]["date"] + '<br>'
            except:
                indice = db_csv.loc[db_csv['url'] == db[couple[0]][0]["url"]].index.tolist()[0]
                ajout_erreur(db_csv, indice, "Problème date")
            if cat == 'Arrêtés de péril':
                try:
                    char += return_string(db[couple[0]][0]["classification_pathologies"]) + " <br> " + return_string(
                        db[couple[0]][0]["classification_lieux"]) + "<br>"
                except:
                    print(adresse, "problème de pathologie manquante")
            char += '<br>'
        char += '</font>'
        liste.append([char, cat_last] )

    return liste


def ajout_legend():
    template = """
    {% macro html(this, kwargs) %}

    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Carte des Arrêtés de Marseille</title>
      <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

      <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
      <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

      <script>
      $( function() {
        $( "#maplegend" ).draggable({
                        start: function (event, ui) {
                            $(this).css({
                                right: "auto",
                                top: "auto",
                                bottom: "auto"
                            });
                        }
                    });
    });

      </script>
    </head>
    <body>


    <div id='maplegend' class='maplegend' 
        style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
         border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>

    <div class='legend-title'>Type d'arrêtés (cliquez pour déplacer)</div>
    <div class='legend-scale'>
      <ul class='legend-labels'>
        <li><span style='background:black;opacity:0.7;'></span>Arrêtés de déconstruction</li>
        <li><span style='background:darkred;opacity:0.7;'></span>Arrêtés d'interdiction d'occuper</li>
        <li><span style='background:red;opacity:0.7;'></span>Arrêtés de péril</li>
        <li><span style='background:red;opacity:0.7;'></span>Arrêtés de péril modificatif</li>
        <li><span style='background:salmon;opacity:0.7;'></span>Arrêtés d'insécurité imminente des équipements communs</li>
        <li><span style='background:orange;opacity:0.7;'></span>Arrêtés d'évacuation et de réintégration</li>
        <li><span style='background:beige;opacity:0.7;'></span>Arrêtés de périmètres de sécurité sur voie publique</li>
        <li><span style='background:beige;opacity:0.7;'></span>Arrêtés de police générale </li>
        <li><span style='background:lightgreen;opacity:0.7;'></span>Arrêtés de main levée partielle </li>
        <li><span style='background:green;opacity:0.7;'></span>Arrêtés de main levée </li>
        <li><span style='background:purple;opacity:0.7;'></span>Diagnostics d'ouvrages </li>
      </ul>
    </div>
    </div>

    </body>
    </html>

    <style type='text/css'>
      .maplegend .legend-title {
        text-align: left;
        margin-bottom: 5px;
        font-weight: bold;
        font-size: 90%;
        }
      .maplegend .legend-scale ul {
        margin: 0;
        margin-bottom: 5px;
        padding: 0;
        float: left;
        list-style: none;
        }
      .maplegend .legend-scale ul li {
        font-size: 80%;
        list-style: none;
        margin-left: 0;
        line-height: 18px;
        margin-bottom: 2px;
        }
      .maplegend ul.legend-labels li span {
        display: block;
        float: left;
        height: 16px;
        width: 30px;
        margin-right: 5px;
        margin-left: 0;
        border: 1px solid #999;
        }
      .maplegend .legend-source {
        font-size: 80%;
        color: #777;
        clear: both;
        }
      .maplegend a {
        color: #777;
        }
    </style>
    {% endmacro %}"""
    macro = MacroElement()
    macro._template = Template(template)
    return macro

