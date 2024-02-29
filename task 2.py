import PyPDF2
from docx import Document
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')


def extract_info_cv(fichier):
    # Déterminer le format du fichier
    if fichier.endswith(".pdf"):
        _format = "pdf"
    elif fichier.endswith(".docx"):
        _format = "docx"
    elif fichier.endswith(".txt"):
        _format = "txt"
    else:
        return "Format de fichier non supporté"

    # Lire le contenu du fichier selon son format
    if _format == "pdf":
        with open(fichier, "rb") as pdf:
            lecteur = PyPDF2.PdfReader(pdf)
            nb_pages = len(lecteur.pages)
            texte = ""
            for i in range(nb_pages):
                page = lecteur.pages[i]
                texte += page.extract_text()
    elif _format == "docx":
        doc = Document(fichier)
        texte = ""
        for para in doc.paragraphs:
            texte += para.text + "\n"
    elif _format == "txt":
        with open(fichier, "r", encoding="utf-8") as txt:
            texte = txt.read()
    else:
        return "Format of file not supported"

    texte = texte.lower()
    mots = word_tokenize(texte)
    mots = [mot for mot in mots if mot not in stopwords.words("english")]
    etiquettes = pos_tag(mots)
    entites = ne_chunk(etiquettes)

    # Initialise a dictionnary
    infos = {"nom": "", "contacts": {}, "experiences": [], "skills": []}

    for entite in entites:
        # Si l'entité est un nom propre
        if type(entite) == nltk.tree.Tree and entite.label() == "PERSON":
            
            nom = " ".join([mot[0] for mot in entite.leaves()])
            # add name to dictionnary
            infos["nom"] = nom
        # if it is a email
        elif type(entite) == tuple and entite[1] == "NN" and "@" in entite[0]:
            # 
            email = entite[0]
            # add email
            infos["contacts"]["email"] = email
        # if it is a number
        elif type(entite) == tuple and entite[1] == "CD" and len(entite[0]) >= 10:
            
            tel = entite[0]
            # add number
            infos["contacts"]["tel"] = tel
      
        elif type(entite) == nltk.tree.Tree and entite.label() == "ORGANIZATION":
            experience = " ".join([mot[0] for mot in entite.leaves()])
            # add experience
            infos["experiences"].append(experience)
        # if it is a skill
        elif type(entite) == tuple and entite[1] == "NN":
            skill = entite[0]
            # add to skill list
            infos["skills"].append(skill)

    # Return the dictionnary of essentials informations
    return infos

# give an example of resume file 
fichier_cv = "RESUME.pdf"
result = extract_info_cv(fichier_cv)
print(result)
