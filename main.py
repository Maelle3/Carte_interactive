import geocode as geo
import carte
import database
import os
import convert_pdf_to_txt as conv
import recuperation as rec

"""Ce qu'il reste à faire:
- ajouter des pdfs
- mieux afficher les classification (sans les [] et les ''), peut être aussi rendre l'affichage plus clair pour 
    différencier les pathologies des lieux
- ajouter un système de filtre
- gérer le problèmes de footer
- gérer les exceptions (2 adresses, mains levées etc)
"""


conv.image_to_txt()
json2 = database.ouverture_bdd("data.json")

for i in os.listdir("./Datas/TXT"):
    path = "./Datas/TXT/" + i
    id  = rec.recup_id(path)
    if id not in json2:
        database.ajout_ligne("data.json", id, i.partition(".txt")[0]+ ".pdf", rec.recup_adresse(path) + ", Marseille", rec.recup_pathologie(path))



c = carte.creation_carte()



liste_adresses = carte.adresses("data.json")
liste_messages = carte.message("data.json")


for i in range(len(liste_adresses)):
    carte.creation_marker(c, geo.geocode(liste_adresses[i])[0], geo.geocode(liste_adresses[i])[1], liste_messages[i])


c.save('carte.html')


