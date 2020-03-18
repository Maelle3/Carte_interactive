########
### 2 endroits à modifier pour tesseract
#######

import os
import pytesseract
from pdf2image import convert_from_path
import pandas
import requests
from gestion_erreurs import enlever_erreur, ajout_erreur

#########
### À adapter en fonction de l'ordinateur utilisé
### Pour PC: (?)
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
### Pour Mac: (?)
tessdata_dir_config = r'--tessdata-dir "/Users/maelle/Downloads/tesseract-ocr-setup-3.05.01/tessdata/"'
#########


def pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for i, image in enumerate(images):
        #########
        ### À adapter en fonction de l'ordinateur utilisé
        ### Pour PC: (?)
        # text = text + pytesseract.image_to_string(image, lang='fra')
        ### Pour Mac: (?)
        text = text + pytesseract.image_to_string(image, lang='fra', config=tessdata_dir_config)
        #########
    return text


def pdf_to_txt():
    db_csv = pandas.read_csv("arretes.csv", encoding='utf-8')
    for i in range(len(db_csv)):
        url = db_csv.loc[i].url
        url_split = url.split("/")
        nom = url_split[-1].split(".")[0]
        if nom + ".txt" not in os.listdir("./Datas/TXT"):
            try:
                changement_url(i, url, db_csv)
                myfile = requests.get(url)
                open('./Datas/PDF/' + nom+".pdf", 'wb').write(myfile.content)
                texte = pdf_to_image("./Datas/PDF/"+nom+".pdf")
                fichier = open("./Datas/TXT/" + nom + ".txt", "w", encoding="utf-8")
                fichier.write(texte)
                fichier.close()
                if db_csv.loc[i].erreurs:
                    enlever_erreur(db_csv, i, url)
            except:
                ajout_erreur(db_csv, i, "Problème URL")

            try:
                os.remove("./Datas/PDF/" + nom + ".pdf")
            except:
                pass
        db_csv.loc[i, "nom_txt"] = nom + ".txt"
    db_csv.to_csv("arretes.csv", index=False, encoding='utf-8')
    return db_csv


def changement_url(i, url, db):
    url_split = url.split("/")
    if url_split[2] == 'logement-urbanisme.marseille.fr':
        url_split[2] = "marseille.fr"
        url = "/".join(url_split)
        db.loc[i, "url"] = url
    elif url_split[4] == 'logement-urbanisme':
        url_split.pop(3)
        url = "/".join(url_split)
        db.loc[i, "url"] = url
    return None
