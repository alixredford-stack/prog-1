######################################################
# Derley Alix, 20300901,                             #
######################################################

#####################################
# Description du contenu du fichier #
#####################################


import random

########################################################################
# Ne pas modifier ce qui suit jusqu'à ce que vous voyez "Modifier ici" #
########################################################################

def readFile(path):
	return open(path, "rb").read().decode("utf-8")
	
def writeFile(path, txt):
	file = open(path, "wb")
	file.write(txt.encode("utf-8"))
	file.close()

# Dessine le bonhomme pendu
#  I-----
#  I    o
#  I   /I\
#  I   / \
#  I   
# __________
# Fournir un nombre d'étapes de 0 à 6 où 0 est le bonhomme vide
def dessiner_bonhomme(etape):
    
    print("  I-----")
    if etape > 0:
        print("  I    o")
    else:
        print("  I")
    if etape > 3:
        print("  I   /I\\")
    elif etape > 2:
        print("  I   /I")
    elif etape > 1:
        print("  I    I")
    else:        
        print("  I")
    if etape > 5:
        print("  I   / \\")
    elif etape > 4:
        print("  I   / ")
    else:
        print("  I")
    print("  I")    
    print("__________")
    
    
##########################################################################
# Modifier ici : Ajouter vos fonctions auxiliaires telles que nécessaire #
##########################################################################

# Choisit un mot aléatoire parmi tous les mots contenus dans les fichiers donnés.
# Chaque mot a une probabilité égale d'être choisi, peu importe le fichier d'origine.

def choisir_mot(mots_possibles):
    ############################################################################
    # Modifier ici : Modifiez le contenu de cette fonction (incluant le return)#
    ############################################################################
    tous_les_mots = []
    for chemin in mots_possibles:
        contenu = readFile(chemin)
        mots_du_fichier = contenu.split("\n")
        for mot in mots_du_fichier:
            if mot != "":  # ignore les lignes vides potentielles
                tous_les_mots.append(mot)
    
    return random.choice(tous_les_mots)

# Détermine la prochaine lettre à tester, en se basant sur la fréquence des
# lettres dans les mots possibles (fichiers donnés), en excluant les lettres
# déjà testées. En cas d'égalité, la lettre alphabétiquement première est choisie.
    
def deviner_lettre(mot, lettres, mots_possibles):
    ############################################################################
    # Modifier ici : Modifiez le contenu de cette fonction (incluant le return)#
    ############################################################################

    tous_les_mots = ""
    for chemin in mots_possibles:
        tous_les_mots += readFile(chemin)
    

    frequences = {}
    for lettre in tous_les_mots:
        if lettre.isalpha():  # ignore les \n et autres caractères non-alphabétiques
            if lettre in frequences:
                frequences[lettre] = frequences[lettre] + 1
            else:
                frequences[lettre] = 1
    

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    meilleure_lettre = None
    meilleure_frequence = -1
    for lettre in alphabet:
        if lettre in frequences and lettre not in lettres:
            if frequences[lettre] > meilleure_frequence:
                meilleure_lettre = lettre
                meilleure_frequence = frequences[lettre]
    
    return meilleure_lettre

    
    
def deviner_lettre_bonus(mot, lettres, mots_possibles):
    ############################################################################
    # Modifier ici : Modifiez le contenu de cette fonction (incluant le return)#
    ############################################################################
    
    return deviner_lettre(mot, lettres, mots_possibles)
    
def bonhomme_pendu(mots_possibles, interactif = False):
    
    print("Bienvenue au jeu de bonhomme pendu")
    print("Choix du mot en cours...")
    
    mot = choisir_mot(mots_possibles) # Mot à deviné    
    mot_devine = "_" * len(mot)       # Mot tel que actuellement deviné
    lettres = []            # Tableau de caractères pour les lettres testées
    etape = 0               # Étape de dessin du bonhomme pendu
       
    
    ############################################################################
    # Modifier ici : Modifiez le contenu de cette fonction (incluant le return)#
    # Certaines lignes de code vous sont fournis pour vous aider, vous aurez   #
    # à les modifier                                                           #
    ############################################################################
    
    dessiner_bonhomme(etape)
    
    print("Lettres : " + "") # À modifier
    print("Mot à deviner : " + "") # À modifier
    c = ""
    
    if interactif:
        c = input("Entrez une lettre : ")
    else:
        # Appelez directement la version avec le bonus, qui appelle par défaut 
        # la version sans bonus
        c = deviner_lettre_bonus("", lettres, mots_possibles)
        print("Entrez une lettre : " + c)
    
    # print("Oups! Le mot était " + mot + ".")
    # print("Vous avez gagné!")
    
    return 0 # À modifier
    
    
interactif = False
    
bonhomme_pendu(["mots.txt", "mots_longs.txt"], interactif)