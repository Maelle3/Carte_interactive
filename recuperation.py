import os

def recup_adresse(texte):
    fichier = open(texte, "r", encoding = "latin-1")
    res = str(fichier.read()).partition("immeuble sis ")[2].partition("-")[0].partition("")[0]
    return res

def recup_pathologie(texte):
    fichier = open(texte, "r", encoding = "latin-1")
    res = str(fichier.read()).partition("pathologies suivantes :")[2].partition("Considérant")[0]
    return res

##Il reste à gérer les bas de page

for i in os.listdir("./Datas/TXT"):
    print(recup_pathologie("./Datas/TXT/" + i))


