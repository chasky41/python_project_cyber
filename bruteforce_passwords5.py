import itertools
import time
import matplotlib.pyplot as plt

# Service simulé pour valider les mots de passe
def service_simule(username, password):
    utilisateur_valide = "admin"
    mot_de_passe_valide = "12345@abcdef"

    return username == utilisateur_valide and password == mot_de_passe_valide

# Fonction brute-force
def bruteforce(username, wordlist):
    tentatives_reussies = 0
    tentatives_echouees = 0

    for password in wordlist:
        print(f"Tentative : {username} -> {password}")
        time.sleep(0.1)  # Simuler un délai
        if service_simule(username, password):
            print(f"Succès ! Le mot de passe est : {password}")
            tentatives_reussies += 1
            break
        else:
            tentatives_echouees += 1

    return tentatives_reussies, tentatives_echouees

# Visualiser les résultats
def visualiser_resultats(reussies, echouees):
    labels = ['Réussies', 'Échouées']
    valeurs = [reussies, echouees]

    plt.figure(figsize=(6, 6))
    plt.pie(valeurs, labels=labels, autopct='%1.1f%%', startangle=140, colors=['green', 'red'])
    plt.title("Résultats des Tentatives de Bruteforce")
    plt.savefig("bruteforce_resultats.png")
    plt.show()
    print("Graphique généré : bruteforce_resultats.png")

# Exemple d'utilisation
if __name__ == "__main__":
    # Liste des mots de passe courants
    wordlist = ["password", "123456", "12345", "qwerty", "admin", "letmein","12345@abcdef"]

    # Utilisateur cible
    username = "admin"

    # Lancer l'attaque brute-force
    tentatives_reussies, tentatives_echouees = bruteforce(username, wordlist)

    # Afficher les résultats
    print(f"Tentatives réussies : {tentatives_reussies}")
    print(f"Tentatives échouées : {tentatives_echouees}")

    # Visualiser les résultats
    visualiser_resultats(tentatives_reussies, tentatives_echouees)
