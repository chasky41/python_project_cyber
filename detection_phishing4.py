import re
import matplotlib.pyplot as plt

# Fonction pour analyser le contenu des emails
def analyser_emails(emails):
    emails_suspects = []
    liens_suspects = re.compile(r"http[s]?://[^\s<>\"']+")


    expediteurs_non_verifies = ["fake@example.com", "phishing@scam.com"]

    for email in emails:
        contenu = email.get("contenu", "")
        expediteur = email.get("expediteur", "")
        
        est_suspect = False
        motifs_detectes = []

        # Vérifier les liens suspects
        if liens_suspects.search(contenu):
            est_suspect = True
            motifs_detectes.append("Lien suspect")

        # Vérifier les expéditeurs
        if expediteur in expediteurs_non_verifies:
            est_suspect = True
            motifs_detectes.append("Expéditeur non vérifié")

        if est_suspect:
            emails_suspects.append({
                "expediteur": expediteur,
                "motifs": motifs_detectes
            })

    return emails_suspects

# Générer un rapport
def generer_rapport(emails_suspects):
    rapport = "Rapport des emails suspects:\n"
    for email in emails_suspects:
        rapport += f"Expéditeur : {email['expediteur']}\n"
        rapport += f"Motifs : {', '.join(email['motifs'])}\n\n"

    with open("rapport_phishing.txt", "w") as f:
        f.write(rapport)

    print("Rapport généré : rapport_phishing.txt")

# Visualiser les statistiques
def visualiser_statistiques(emails, emails_suspects):
    total_emails = len(emails)
    total_suspects = len(emails_suspects)

    labels = ['Phishing détecté', 'Non suspecté']
    valeurs = [total_suspects, total_emails - total_suspects]

    plt.figure(figsize=(6, 6))
    plt.pie(valeurs, labels=labels, autopct='%1.1f%%', startangle=140, colors=['red', 'green'])
    plt.title("Statistiques des Emails")
    plt.savefig("statistiques_phishing.png")
    plt.show()
    print("Graphique généré : statistiques_phishing.png")

# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple d'emails à analyser
    emails = [
        {"expediteur": "trusted@example.com", "contenu": "Bonjour, visitez notre site : http://example.com"},
        {"expediteur": "fake@example.com", "contenu": "Attention ! Cliquez ici : http://scam.com"},
        {"expediteur": "phishing@scam.com", "contenu": "Votre compte est compromis. Visitez http://malicious.com pour sécuriser."},
        {"expediteur": "secure@example.com", "contenu": "Pas de lien suspect ici."}
    ]

    # Analyse des emails
    emails_suspects = analyser_emails(emails)

    # Générer le rapport
    generer_rapport(emails_suspects)

    # Visualiser les statistiques
    visualiser_statistiques(emails, emails_suspects)
