import geocode as geo
import carte

adresse1 = geo.geocode(geo.adresse_test)
c = carte.creation_carte()
carte.creation_marker(c, adresse1[0], adresse1[1], "ca a marché")

c.save('carte.html')