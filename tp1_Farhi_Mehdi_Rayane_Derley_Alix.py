# Auteur: Alix Derley, Mehdi Rayane Farhi et Abdellah Kortobi
# Date: 22-06-2026

# Ce programme est une calculatrice postfixe.Le programme débute en demandant 
# à l’utilisateur de saisir une formule à calculer, et doit imprimer une
# phrase de validation ou sinon une phrase d'erreur.

# La fonction n_ieme_bite retourne le b-ième bit de a 
# (en comptant par la droite à partir de 0).

def n_ieme_bit(a, b):
    masque = 1 << b
    resultat = a & masque
    return resultat >> b

# Cette retourne True si tous les caractères de texte sont dans valides.

def est_chiffres_valides(texte, valide):
    if texte == "":
        return False
    for c in texte:
        if c not in valide:
            return False
    return True
    

# La fonction est_nombre reçoit un texte et repond vrai ou faux.

def est_nombre(texte):
    if texte == "":
        return False
    if texte[0] == "-":
        return False
    if texte[:2] == "0b"or texte[:2] == "0B":
        return est_chiffres_valides(texte[2:], "01")
    if texte[:2] == "0o"or texte[:2] == "0O":
        return est_chiffres_valides(texte[2:], "01234567")
    if texte[:2] == "0x"or texte[:2] == "0X":
        return est_chiffres_valides(texte[2:], "0123456789abcdefABCDEF")
    return est_chiffres_valides(texte, "0123456789")
    

# La fonction valeur_chiffre retourne la valeur numérique 
# d'un caractère (0-9, a-f ou A-F).

def valeur_chiffre(caractere):
    chiffres_min = "0123456789abcdef"
    chiffres_maj = "0123456789ABCDEF"
    for i in range(len(chiffres_min)):
        if caractere == chiffres_min[i] or caractere == chiffres_maj[i]:
            return i
    return 0

# La fonction convertir_base convertit un texte dans une 
# certaine base en entier.

def convertir_base(texte, base):
    resultat = 0
    for chiffre in texte:
        resultat = resultat * base + valeur_chiffre(chiffre)
    return resultat

# La fonction convertir_nombre convertit un texte en entier 
# (base 10, 2, 8 ou 16).

def convertir_nombre(texte):
    if texte[:2] == "0b" or texte[:2] == "0B":
        return convertir_base(texte[2:], 2)
    if texte[:2] == "0o" or texte[:2] == "0O":
        return convertir_base(texte[2:], 8)
    if texte[:2] == "0x" or texte[:2] == "0X":
        return convertir_base(texte[2:], 16)
    return convertir_base(texte, 10)

# La fonction est_operateur retourne True si texte est un opérateur valide.  

def est_operateur(texte):
    operateurs = ["+", "-", "*", "/", "//", "%", "&", "|", "^", "b"]
    for op in operateurs:
        if texte == op:
            return True
    return False
# La fonction appliquer_operateur applique l'opérateur op sur les nombres 
# a et b, et retourne le résultat.

def appliquer_operateur(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b
    if op == "//":
        return a // b
    if op == "%":
        return a % b
    if op == "&":
        return a & b
    if op == "|":
        return a | b
    if op == "^":
        return a ^ b
    if op == "b":
        return n_ieme_bit(a, b)
    
# La fonction calculer_formule calcule le résultat d'une formule postfixe, 
# ou retourne '#' si invalide.

def calculer_formule(texte):
    tokens = texte.split(" ")
    nombres = []

    for token in tokens:
        if token == "":
            continue  # on ignore les espaces superflus

        if est_nombre(token):
            if len(nombres) >= 2:
                return "#"  # un 3e nombre apparaît, formule invalide
            nombres.append(convertir_nombre(token))

        elif est_operateur(token):
            if len(nombres) < 2:
                return "#"  # pas assez de nombres pour calculer
            b = nombres.pop()
            a = nombres.pop()
            if (token == "/" or token == "//" or token == "%") and b == 0:
                return "#"  # division par zéro
            resultat = appliquer_operateur(a, b, token)
            nombres.append(resultat)

        else:
            return "#"  # symbole inconnu

    if len(nombres) != 1:
        return "#"  # il doit rester exactement un nombre à la fin

    return nombres[0]

# La fonction principal demande une formule à l'utilisateur et affiche 
# le résultat ou une erreur.

def principal():
    entree_utilisateur = input("Entrez une formule à calculer : ")
    resultat = calculer_formule(entree_utilisateur)

    if resultat == "#":
        print("Erreur, " + entree_utilisateur + \
              " n'est pas une formule valide.")
    else:
        print("Le résultat du calcul est : " , resultat , ".")

# Teste de la fonction n_ieme_bit.

def tests_n_ieme_bit():
    assert n_ieme_bit(9, 0) == 1   
    assert n_ieme_bit(9, 1) == 0    
    assert n_ieme_bit(9, 3) == 1  
    assert n_ieme_bit(0, 1) == 0   
    assert n_ieme_bit(1, 0) == 1 
    assert n_ieme_bit(8, 3) == 1  
    print("Tous les tests de n_ieme_bit ont réussi.")
    
# Teste de la fonction calculer_formule.

def tests_calculer_formule():
    # Cas de base : un seul nombre
    assert calculer_formule("0b1") == 1
    assert calculer_formule("42") == 42
    assert calculer_formule("0") == 0
    assert calculer_formule("0x1A") == 26
    assert calculer_formule("0o17") == 15

    # Opérations simples
    assert calculer_formule("1 2 +") == 3
    assert calculer_formule("6 3 -") == 3
    assert calculer_formule("4 5 *") == 20
    assert calculer_formule("7 2 /") == 3.5
    assert calculer_formule("7 2 //") == 3
    assert calculer_formule("7 2 %") == 1
    assert calculer_formule("6 3 &") == 2
    assert calculer_formule("6 3 |") == 7
    assert calculer_formule("6 3 ^") == 5
    assert calculer_formule("9 0 b") == 1
    assert calculer_formule("0 1 b") == 0

    # Plusieurs opérations enchaînées
    assert calculer_formule("1 3 + 5 %") == 4

    # Résultat négatif ou fractionnaire
    assert calculer_formule("3 5 -") == -2
    assert calculer_formule("1 2 /") == 0.5

    # Espaces superflus
    assert calculer_formule("1   2 +") == 3
    assert calculer_formule(" 1 2 + ") == 3
    
    # Trop de nombres
    assert calculer_formule("1 3 5 + %") == "#"

    # Pas assez de nombres
    assert calculer_formule("1 %") == "#"
    assert calculer_formule("+") == "#"

    # Symbole inconnu
    assert calculer_formule("a") == "#"
    assert calculer_formule("1 2 z") == "#"

    # Nombre négatif
    assert calculer_formule("-1") == "#"
    assert calculer_formule("1 -2 +") == "#"

    # Notation scientifique
    assert calculer_formule("1e5") == "#"

    # Formule vide
    assert calculer_formule("") == "#"

    # Division par zéro
    assert calculer_formule("5 0 /") == "#"
    assert calculer_formule("5 0 %") == "#"
    assert calculer_formule("5 0 //") == "#"

    # Pas assez d'opérateurs (reste 2 nombres à la fin)
    assert calculer_formule("1 2") == "#"

    print("Tous les tests de calculer_formule ont réussi.")
        
# Appelle 

tests_n_ieme_bit()
tests_calculer_formule()
principal()