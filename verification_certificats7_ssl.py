import ssl
import socket
from datetime import datetime
import matplotlib.pyplot as plt

# Fonction pour vérifier les certificats SSL
def verifier_certificat_ssl(site_web):
    try:
        # Établir une connexion sécurisée avec le site web
        context = ssl.create_default_context()
        with socket.create_connection((site_web, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=site_web) as ssock:
                cert = ssock.getpeercert()

        # Extraire la date d'expiration
        expiration = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
        return expiration

    except Exception as e:
        print(f"Erreur lors de la vérification de {site_web} : {e}")
        return None

# Fonction principale
if __name__ == "__main__":
    # Liste des sites web à vérifier
    sites_web = ["google.com", "expired.badssl.com", "github.com", "example.com"]

    certificats_valides = 0
    certificats_expires = 0
    certificats_data = []

    for site in sites_web:
        print(f"Vérification du site : {site}")
        expiration = verifier_certificat_ssl(site)

        if expiration:
            jours_restants = (expiration - datetime.now()).days
            if jours_restants > 0:
                print(f"Certificat valide pour {site}, expire dans {jours_restants} jours.")
                certificats_valides += 1
                certificats_data.append((site, "Valide", jours_restants))
            else:
                print(f"Certificat expiré pour {site}.")
                certificats_expires += 1
                certificats_data.append((site, "Expiré", 0))
        else:
            certificats_expires += 1
            certificats_data.append((site, "Inconnu", 0))

    # Générer un graphique
    labels = ['Valides', 'Expirés']
    valeurs = [certificats_valides, certificats_expires]

    plt.figure(figsize=(6, 6))
    plt.pie(valeurs, labels=labels, autopct='%1.1f%%', startangle=140, colors=['green', 'red'])
    plt.title("Statistiques des Certificats SSL")
    plt.savefig("certificats_ssl.png")
    plt.show()

    # Sauvegarder un rapport
    with open("rapport_certificats_ssl.txt", "w") as f:
        for site, statut, jours in certificats_data:
            f.write(f"{site} : {statut} ({jours} jours restants)\n")

    print("Rapport généré : rapport_certificats_ssl.txt")
    print("Graphique généré : certificats_ssl.png")
