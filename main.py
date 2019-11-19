import geocode as geo
import carte
import database

c = carte.creation_carte()

liste_adresses = carte.adresses("arretes.csv")
liste_messages = carte.message("arretes.csv")

for i in range(len(liste_adresses)):
    carte.creation_marker(c,geo.geocode(liste_adresses[i])[0], geo.geocode(liste_adresses[i])[1], liste_messages[i])


#adresse1=geo.geocode("11 rue Moustier Marseille")
#carte.creation_marker(c, adresse1[0], adresse1[1], "ca a marché")


c.save('carte.html')

##df[["lieux","pathologies"]]
##df.loc[df['adresse']='truc', :])

