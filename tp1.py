#1  Bonjour le Monde
print("Bonjour le Monde")


#2  Calcul de l'Âge
annee_naissance = int(input("Entrez votre année de naissance : "))
annee_actuelle = 2024
age = annee_actuelle - annee_naissance
print(f"Vous avez {age} ans.")

#3  Pair ou Impair
nombre = int(input("Saisissez un nombre : "))
if nombre % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")


#4 Somme des Nombres
n = int(input("Saisissez un nombre : "))
somme = 0
for i in range(1, n + 1):
    somme += i
print(f"La somme des nombres de 1 à {n} est {somme}.")

#5 Table de Multiplication

for i in range(1, 11):  #  lignes
    for j in range(1, 11):  #  colonnes
        print(f"{i * j:4}", end=" ")  # Affiche le produit formaté
    print()

#6  Trouver le Plus Grand Nombre
nombres = []
for i in range(5):
    nombre = int(input(f"Saisissez le nombre {i + 1} : "))
    nombres.append(nombre)
print(f"Le plus grand nombre est : {max(nombres)}")

#7 Compter les Voyelles

phrase = input("Saisissez une phrase : ").lower()
voyelles = "aeiou"
compteur = 0
for caractere in phrase:
    if caractere in voyelles:
        compteur += 1
print(f"Le nombre de voyelles dans la phrase est : {compteur}")


#8 Inverser une Chaîne
chaine = input("Saisissez une chaîne : ")
chaine_inversee = chaine[::-1]
print(f"Chaîne inversée : {chaine_inversee}")



#9 Palindrome

mot = input("Saisissez un mot : ").lower()
if mot == mot[::-1]:
    print("Le mot est un palindrome.")
else:
    print("Le mot n'est pas un palindrome.")





#10 Factorielle

def factorielle(n):
    if n == 0 or n == 1:
        return 1
    return n * factorielle(n - 1)

nombre = int(input("Saisissez un nombre : "))
resultat = factorielle(nombre)
print(f"La factorielle de {nombre} est : {resultat}")
