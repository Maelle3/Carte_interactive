import os
import pytesseract
from pdf2image import convert_from_path
import pandas
import requests

# À adapter en fonction de l'ordinateur utilisé
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for i, image in enumerate(images):
        text = text + pytesseract.image_to_string(image, lang='fra')
    return text


def pdf_to_txt():
    db_csv = pandas.read_csv("arretes.csv", encoding='utf-8')
    # for i in range(len(db)):
    for i in range(30):
        url = db_csv.loc[i].url
        url_split = url.split("/")
        nom = url_split[-1].split(".")[0]
        if nom + ".txt" not in os.listdir("./Datas/TXT") and not db_csv.loc[i].erreurs:
            if url_split[2] == 'logement-urbanisme.marseille.fr':
                url_split[2] = "marseille.fr"
                url = "/".join(url_split)
                db_csv.loc[i, "url"] = url
            try:
                myfile = requests.get(url)
                open('./Datas/PDF/' + nom+".pdf", 'wb').write(myfile.content)
                texte = pdf_to_image("./Datas/PDF/"+nom+".pdf")
                fichier = open("./Datas/TXT/" + nom + ".txt", "w", encoding="utf-8")
                fichier.write(texte)
                fichier.close()
            except:
                db_csv.loc[i, 'erreurs'] = True
                error = pandas.read_csv("Datas/erreurs.csv")
                error.loc[len(error)] = ["Problème URL"] + list(db_csv.loc[i])
                error.to_csv("Datas/erreurs.csv", encoding='utf-8', index=False)

            try:
                os.remove("./Datas/PDF/" + nom + ".pdf")
            except:
                pass
        db_csv.loc[i, "nom_txt"] = nom + ".txt"
    db_csv.to_csv("arretes.csv", index=False, encoding='utf-8')
    return db_csv
