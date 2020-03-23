# Carte_interactive

Ce Read me a pour but de vous présenter globalement ce que fait le programme et de vous montrer également sur quels paramètres vous pouvez influer.
<br><br> /!\  Nous vous mettrons également en évidence quels paramètres sont à modifier en fonction de votre système d'exploitation et de votre configuration d'installation.

<br>Tout d'abord toutes les bibliothèques Python nécessaires pour le programme ont été mises dans le fichier *`requirements.txt`*.
<br>
<br>
## Changement en fonction de votre configuration

Plusieurs changements sont à effectuer :
<br> 
#### Dans le fichier *`convert_pdf_to_txt.py`* :
Il faut ajouter tesseract ainsi que poppler aux variables d'environnement de l'ordinateur.
<br> Il faut ajouter les dépendances relatives à l'installation tesseract aux lignes 12 à 18. Les lignes spnt différentes suivant le système d'exploitation. 
<br> **Sur Windows**, `pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`suffit pour l'utilisation de la langue française.
<br> **Sur Mac**, il faut donner le lien vers le fichier de langues : `tessdata_dir_config = r'--tessdata-dir "/Users/nomdutilisateur/Downloads/tesseract-ocr-setup-3.05.01/tessdata/"'`.
<br><br> Il faut également ajuster la fonction *`pdf_to_image`* en commantant la ligne correspondant au bon système d'exploitation.
<br>
## Changement de représentation des données : marqueurs ou points
Deux représentations sont possibles pour les différentes addresses présentant des arrêtés.
<br>
#### Dans le fichier *`carte.py`* :

Dans la fonction *`creation_carte`* aux lignes 27 à 34, il faut commenter et décommenter la représentation voulue.
<br>
Dans la fonction *`creation_marker`* aux lignes 42 à 47, il faut commenter et décommenter la représentation voulue.
<br>
#### Dans le fichier *`main.py`*  : 
Aux lignes 69 à 74, dans la boucle, il faut commenter et décommenter la représentation voulue.
<br>
Pour la représentation avec des **marqueurs**, il faut **décommenter** les lignes 57 à 61. 
<br>
Pour la représentation avec des **points**, il faut **commenter** ces lignes.
<br>
## Personnalisation des marqueurs 
Avec la représentation par des marqueurs, il est possible de personnaliser les icones (type et couleur). Par défaut, ce sont des maisons blanches.
<br>
### Dans le fichier *`carte.py`* : 
Dans la fonction *`creation_marker`* à la ligne 44 :
<br>
Pour le type d'icone, il faut changer `icon='home'` en remplaçant "home" par un des icones présent sur https://fontawesome.com/icons?d=gallery . 
<br>
Pour la couleur de l'icone, il faut changer `icon_color='white'` en remplaçant "white" par une des couleurs listées dans la documentation  : `'red', 'darkred',  'lightred', 'orange', 'beige', 'green', 'darkgreen', 'lightgreen', 'blue', 'darkblue', 'cadetblue', 'lightblue', 'purple', 'darkpurple', 'pink', 'white', 'gray', 'lightgray', 'black'`.
