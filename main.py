#######
### 2 endroits à modifier en fonction de MARKER ou POINT
######

import geocode as geo
import carte
import database
import os
import convert_pdf_to_txt as conv
import recuperation as rec
import webbrowser
import folium
from folium.plugins import MarkerCluster
from gestion_erreurs import ajout_erreur


db_csv = conv.pdf_to_txt()
json2 = database.ouverture_bdd()

for i in range(len(db_csv)):
    if not db_csv.loc[i].erreurs:
        path = "./Datas/TXT/" + db_csv.loc[i]["nom_txt"]
        id = rec.recup_id(path)
        if id not in json2:
            cat = database.calcul_categorie(i, db_csv)
            date = rec.recup_date(path, db_csv, i)
            if cat == "Arrêtés de péril":
                pathologies = rec.recup_pathologie(path, db_csv, i)

                if not db_csv.loc[i].erreurs:
                    conv.changement_url(i, db_csv.loc[i].url, db_csv)
                    try:
                        database.ajout_ligne_peril(id, db_csv.loc[i].url, db_csv.loc[i].adresse + ", Marseille",
                                               pathologies, date)
                    except:
                        ajout_erreur(db_csv, i, "Problème adresse")
            else:
                try:
                    database.ajout_ligne_autre(cat, id, db_csv.loc[i].url, db_csv.loc[i].adresse + ", Marseille",
                                           date)
                except:
                    ajout_erreur(db_csv, i, "Problème adresse")

db_csv.to_csv("arretes.csv", index=False, encoding='utf-8')

c = carte.creation_carte()


icon_create_function = """ 
    function(cluster) {
    var childCount = cluster.getChildCount(); 
    var c = ' marker-cluster-medium';
    return new L.DivIcon({ html: '<link rel="stylesheet" href="./cluster.css"/><div><span> ' + childCount + '</span></div>', className: 'marker-cluster' + c, iconSize: new L.Point(40, 40) });
    }
    """

#########
###Il faut que ce soit décommenté pour Markers et commenté pour Points
#mcg = folium.plugins.MarkerCluster(control=False, icon_create_function=icon_create_function)
#c.add_child(mcg)
########

liste_adresses = carte.adresses()

liste_messages = carte.message(liste_adresses, db_csv)


for i in range(len(liste_adresses)):
    ##########
    ### Pour Marker:
    #carte.creation_marker(mcg, geo.geocode(liste_adresses[i])[0], geo.geocode(liste_adresses[i])[1], liste_messages[i])
    ### Pour Points:
    carte.creation_marker(c, geo.geocode(liste_adresses[i])[0], geo.geocode(liste_adresses[i])[1], liste_messages[i])
    #########

legend = carte.ajout_legend()

c.get_root().add_child(legend)


c.save('carte.html')


webbrowser.open("file://" + os.getcwd() + '/carte.html')

