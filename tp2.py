# Créer une variable chaine
chaine = "Il fait beau aujourd'hui. Je veux en profiter."

#Remplacer les points par des (!) On doit donc avoir à la fin de l’exécution : "Il fait beau aujourd'hui ! Je veux en profiter ! "
chaine = chaine.replace(".", "!")
print(chaine)  


# Mettre toute la chaine en minuscule 
chaine_minuscule = chaine.lower()
print(chaine_minuscule)


# Mettre toute la chaine en Majuscule 
chaine_majuscule = chaine.upper()
print(chaine_majuscule)



# Quel est l’indice du caractère ‘b’ 

indice_b = chaine.index('b')
print(indice_b)  # L'indice du premier 'b'



#Exercice 2

def premierMot(chaine):
    mots = chaine.split()
    return mots[0] if mots else ""
# Exemple d'utilisation
print(premierMot("samedi soir, je vais au cinéma"))  # "samedi"



#Exercice 3
def majuscule_mot(chaine):
    mots = chaine.split()
    mots_capitalises = [mot.capitalize() for mot in mots]
    return " ".join(mots_capitalises)

# Exemple d'utilisation
print(majuscule_mot("je mange du fromage"))  # "Je Mange Du Fromage"


#Exercice 4

def retourner_phrase(chaine):
    mots = chaine.split()
    mots_inverses = mots[::-1]
    return " ".join(mots_inverses)

# Exemple d'utilisation
print(retourner_phrase("J’en suis tout retourné"))  # "retourné tout suis J’en"



#Exercice5 
def image(mot):
    resultat = ""
    i = 0
    while i < len(mot):
        count = 1
        while i + 1 < len(mot) and mot[i] == mot[i + 1]:
            i += 1
            count += 1
        resultat += str(count) + mot[i]
        i += 1
    return resultat

# Générer les 20 premiers termes de la suite
u = "1"
for _ in range(20):
    print(u)
    u = image(u)

