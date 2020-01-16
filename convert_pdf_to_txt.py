import os
import pytesseract
from pdf2image import convert_from_path

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for i, image in enumerate(images):
        text = text + pytesseract.image_to_string(image, lang='eng')
    return text


def image_to_txt():
    for i in os.listdir("./Datas/PDF"):
        nom_liste = i.split('.')
        nom = nom_liste[0]
        if nom+".txt" not in os.listdir("./Datas/TXT"):
            texte = pdf_to_image("./Datas/PDF/" + i)
            fichier = open("./Datas/TXT/" + nom + ".txt", "w")
            fichier.write(texte)
            fichier.close()



