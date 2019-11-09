import geocode as geo
import carte

adresse1 = geo.geocode(geo.adresse_test)
adresse_centrale = geo.geocode("38 rue frédéric joliot curie marseille")
c = carte.creation_carte()
carte.creation_marker(c, adresse1[0], adresse1[1], "ca a marché")
carte.creation_marker(c, adresse_centrale[0], adresse_centrale[1], "Centrale Marseille")

c.save('carte.html')