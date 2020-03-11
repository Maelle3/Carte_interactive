import pandas


def recup_id(texte):
    fichier = open(texte, "r", encoding="utf-8")
    res = str(fichier.read()).partition("ID : ")[2].partition("\n")[0]
    return res


def recup_adresse(texte):
    fichier = open(texte, "r", encoding="utf-8")
    res = str(fichier.read()).partition("immeuble sis ")[2].partition("-")[0].partition("")[0].partition("â")[0].partition("—")[0]
    return res


def recup_pathologie(texte, db_csv, i):
    fichier = open(texte, "r", encoding="utf-8")
    if "pathologies suivantes :" in fichier.read():
        fichier.seek(0)
        res = str(fichier.read()).partition("pathologies suivantes :")[2].partition("Considérant")[0]
        fichier.close()
        return res
    else:
        db_csv.loc[i, 'erreurs'] = True
        error = pandas.read_csv("Datas/erreurs.csv")
        error.loc[len(error)] = ["Problème pathologies"] + list(db_csv.loc[i])
        error.to_csv("Datas/erreurs.csv", encoding='utf-8', index=False)
        db_csv.to_csv('arretes.csv', encoding='utf-8', index=False)
        return None


def recup_date(texte):
    fichier = open(texte, "r", encoding="utf-8")
    res = str(fichier.read()).partition("le ")[2].partition("\n")[0]
    return res


def ajout_class(string1, string2, classification, pathologie):
    if string1 in pathologie:
        if string2 not in classification:
            classification.append(string2)
    return None


def classification_pathologie(pathologie):
    classification = []
    ajout_class("ffais", "affaissement", classification, pathologie)
    ajout_class("ltér", "altération", classification, pathologie)
    ajout_class("hute", "chutes", classification, pathologie)
    ajout_class("tomber", "chutes", classification, pathologie)
    ajout_class("porte à faux", "chutes", classification, pathologie)
    ajout_class("orro", "corrosion", classification, pathologie)
    ajout_class("ouill", "corrosion", classification, pathologie)
    ajout_class("lectr", "danger électrique", classification, pathologie)
    ajout_class("ébris", "débris", classification, pathologie)
    ajout_class("éform", "déformation", classification, pathologie)
    ajout_class("égrad", "dégradation", classification, pathologie)
    ajout_class("ésord", "désordre", classification, pathologie)
    ajout_class("éstructu", "déstructuration", classification, pathologie)
    ajout_class("estructi", "déstruction", classification, pathologie)
    ajout_class("étérior", "détérioration", classification, pathologie)
    ajout_class("ffondr", "effondrement", classification, pathologie)
    ajout_class("stabl", "effondrement", classification, pathologie)
    ajout_class("tanch", "étanchéité", classification, pathologie)
    ajout_class("coulement", "étanchéité", classification, pathologie)
    ajout_class("issu", "fissures", classification, pathologie)
    ajout_class("ézarde", "fissures", classification, pathologie)
    ajout_class("ragil", "fragilité", classification, pathologie)
    ajout_class("aible", "fragilité", classification, pathologie)
    ajout_class("umid", "humidité", classification, pathologie)
    ajout_class("nstab", "instabilité", classification, pathologie)
    ajout_class("oisi", "moisissures", classification, pathologie)
    return classification


def classification_lieu(pathologie):
    classification = []
    ajout_class("alcon", "balcon", classification, pathologie)
    ajout_class("agade", "façade", classification, pathologie)
    ajout_class("açade", "façade", classification, pathologie)
    ajout_class("acade", "façade", classification, pathologie)
    ajout_class("oiture", "toiture", classification, pathologie)
    ajout_class("scalier", "escalier", classification, pathologie)
    ajout_class("loison", "cloison", classification, pathologie)
    ajout_class("lafond", "plafond", classification, pathologie)
    ajout_class("sol", "plancher", classification, pathologie)
    ajout_class("lancher", "plancher", classification, pathologie)
    ajout_class("enêtre", "fenêtre", classification, pathologie)
    ajout_class("enetre", "fenêtre", classification, pathologie)
    ajout_class("outre", "poutre", classification, pathologie)
    ajout_class("arrelage", "plancher", classification, pathologie)
    ajout_class("harpente", "charpente", classification, pathologie)
    ajout_class("mur", "mur", classification, pathologie)
    ajout_class("arche", "escalier", classification, pathologie)
    ajout_class("orniche", "corniche", classification, pathologie)
    ajout_class("lafond", "plafond", classification, pathologie)
    ajout_class("errass", "balcon", classification, pathologie)
    return classification
