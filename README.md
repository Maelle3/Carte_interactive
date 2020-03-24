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
Il est nécessaire d'installer `tesseract-ocr` et `poppler`sur son ordinateur et **PAS UNIQUEMENT** les bibliothèques python ! <br>
`tesseract-ocr` peut être installé en suivant ces instructions : https://github.com/tesseract-ocr/tesseract/wiki#Installation
<br> Il faut également ajouter le fichier `fra.traineddata`dans le répertoire *`tessdata`* afin d'avoir l'analyse des PDF en français. On peut le trouver ici : https://github.com/tesseract-ocr/tessdata/blob/3.04.00/fra.traineddata .
<br>
<br> Il faut également ajouter tesseract ainsi que poppler aux variables d'environnement de l'ordinateur
<br>
<br> Il faut ajouter les dépendances relatives à l'installation tesseract aux lignes 12 à 18. Les lignes sont différentes suivant le système d'exploitation. 
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
Pour le type d'icone, il faut changer `icon='home'` en remplaçant "home" par un des icones présent sur https://glyphicons.com/sets/basic/ . 
<br>
Pour la couleur de l'icone, il faut changer `icon_color='white'` en remplaçant "white" par une des couleurs listées dans la documentation  : `'red', 'darkred',  'lightred', 'orange', 'beige', 'green', 'darkgreen', 'lightgreen', 'blue', 'darkblue', 'cadetblue', 'lightblue', 'purple', 'darkpurple', 'pink', 'white', 'gray', 'lightgray', 'black'`.
<br>
## Gestion manuelle des erreurs
Lorsqu'une erreur est détectée par le programme (problème d'url, d'adresse, de date ou d'annonce de pathologies), elle est ajoutée au fichier `erreurs.csv`. Certaines peuvent être traitées manuellement.
<br>
#### Problème de date :
1- Aller dans le fichier `.txt`corresondant à l'adresse que l'on souhaite traiter <br>
2- Ajouter au début du fichier : `Envoyé en préfecture le <dd/mm/yyyy>` <br>
3- Supprimer toutes les lignes de `erreurs.csv` sauf la première <br>
4- Supprimer le contenu du fichier `data.json` et ne laisser que `{}` comme contenu <br>
5- Dans le fichier `arretes.csv` placer la colonne `erreurs` de l'arrêté traité sur `False` <br>
6- Faire `run` sur le fichier `main.py` <br>
7- Vérifier que l'arrêté n'apparaît plus dans `erreurs.csv` et que l'erreur a été correctement traité <br>
#### Problème d'adresse : 
1- Aller dans le fichier `arretes.csv` <br>
2- Ajouter l'adresse dans la colonne `adresse` <br>
3- Placer la colonne `erreurs` de l'arrêté traité sur `False` <br>
4- Supprimer toutes les lignes de `erreurs.csv` sauf la première <br>
5- Supprimer le contenu du fichier `data.json` et ne laisser que `{}` comme contenu <br>
6- Faire `run` sur le fichier `main.py` <br>
7- Vérifier que l'arrêté n'apparaît plus dans `erreurs.csv` et que l'erreur a été correctement traitée <br>
#### Problème d'URL :
Si c'est cette catégorie de problème qui est listée dans le fichier `erreurs.csv`, il faut vérifier que le lien vers le PDF de l'arrêté est fonctionnel. Si c'est le cas et que l'arrêté n'avait pa pu être traité à cause d'un problème de connexion, relancer le programme suffira à traiter l'erreur. Sinon, il est possible que le PDF ne soit plus disponible sur le site de la mairie.
