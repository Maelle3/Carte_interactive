import geocode as geo
import carte
import database

c = carte.creation_carte()

liste_adresses = carte.adresses("arretes.csv")
liste_messages = carte.message("arretes.csv")


for i in range(len(liste_adresses)):
    carte.creation_marker(c, geo.geocode(liste_adresses[i])[0], geo.geocode(liste_adresses[i])[1], liste_messages[i])


c.save('carte.html')


