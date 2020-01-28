import geocode as geo
import carte
import database
import os
import convert_pdf_to_txt as conv
import recuperation as rec
import webbrowser
import folium
from folium.plugins import MarkerCluster
from folium.plugins import FeatureGroupSubGroup
from folium import plugins

"""Ce qu'il reste à faire:
- ajouter un système de filtre
- gérer le problèmes de footer
- gérer les exceptions (2 adresses, mains levées etc)
"""


conv.image_to_txt()
json2 = database.ouverture_bdd()

for i in os.listdir("./Datas/TXT"):
    path = "./Datas/TXT/" + i
    id = rec.recup_id(path)
    if id not in json2:
        database.ajout_ligne(id, i.partition(".txt")[0] + ".pdf", rec.recup_adresse(path) + ", Marseille",
                             rec.recup_pathologie(path), rec.recup_date(path))

c = carte.creation_carte()



Liste_des_classifications = ["affaissement", "altération","chutes", "corrosion", "danger électrique","débris",
                             "déformation", "dégradation", "déstructuration", "détérioration", "effondrement",
                             "étanchéité", "fissures", "fragilité", "humidité", "moisissures"]

Liste_des_lieux = ["balcon", "cloison", "charpente", "corniche", "escalier", "façade", "fenêtre", "mur", "plafond",
                "plancher", "poutre", "toiture"]

fg = folium.FeatureGroup(name='groups', control = False)
c.add_child(fg)

Liste_groupe = []
for i in Liste_des_classifications:
    g = plugins.FeatureGroupSubGroup(fg, i)
    c.add_child(g)
    Liste_groupe.append(g)

# for j in Liste_des_lieux:
#     g = plugins.FeatureGroupSubGroup(fg, j)
#     c.add_child(g)
#     Liste_groupe.append(g)



liste_adresses = carte.adresses()
liste_messages = carte.message()

for i in range(len(liste_adresses)):
    for j in liste_messages[1][i]:
        ind = Liste_des_classifications.index(j)
        groupe = Liste_groupe[ind]
        carte.creation_marker(groupe , geo.geocode(liste_adresses[i])[0], geo.geocode(liste_adresses[i])[1], liste_messages[0][i])
    # for k in liste_messages[2][i]:
    #     print(k)
    #     ind = Liste_des_lieux.index(k)
    #     groupe = Liste_groupe[len(Liste_des_classifications) + ind]
    #     carte.creation_marker(groupe , geo.geocode(liste_adresses[i])[0], geo.geocode(liste_adresses[i])[1], liste_messages[0][i])


folium.LayerControl(collapsed=False).add_to(c)



c.save('carte.html')


webbrowser.open("file://"+os.getcwd()+'/carte.html')

