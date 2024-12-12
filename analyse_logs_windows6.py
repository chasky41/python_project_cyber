import pandas as pd
import matplotlib.pyplot as plt

# Fonction pour analyser les logs de sécurité Windows
def analyser_logs(fichier_csv):
    try:
        # Charger les logs
        logs = pd.read_csv(fichier_csv)

        # Vérifier les colonnes nécessaires
        if 'EventID' not in logs.columns or 'Message' not in logs.columns:
            print("Le fichier CSV doit contenir les colonnes 'EventID' et 'Message'.")
            return

        # Filtrer les événements suspects (par exemple, tentatives de connexion échouées)
        evenements_suspects = logs[logs['EventID'] == 4625]  # EventID 4625 correspond aux échecs de connexion

        # Générer un rapport des événements suspects
        rapport = "Rapport des événements suspects:\n"
        for _, row in evenements_suspects.iterrows():
            rapport += f"Time: {row['TimeCreated']} - Message: {row['Message']}\n"

        # Sauvegarder le rapport dans un fichier
        with open('rapport_evenements_suspects.txt', 'w') as f:
            f.write(rapport)

        print("Rapport généré : rapport_evenements_suspects.txt")

        # Visualiser les types d'événements et leur fréquence
        type_evenements = logs['EventID'].value_counts()

        plt.figure(figsize=(10, 5))
        type_evenements.plot(kind='bar')
        plt.title("Fréquence des types d'événements")
        plt.xlabel("ID de l'événement")
        plt.ylabel("Nombre d'occurrences")
        plt.tight_layout()
        plt.savefig("frequence_evenements.png")
        plt.show()
        print("Graphique généré : frequence_evenements.png")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exécution principale
if __name__ == "__main__":
    fichier_csv = input("Entrez le chemin du fichier de logs de sécurité Windows (format CSV) : ")
    analyser_logs(fichier_csv)
