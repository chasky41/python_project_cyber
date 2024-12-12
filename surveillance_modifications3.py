import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import matplotlib.pyplot as plt
from datetime import datetime

# Gestionnaire d'événements pour la surveillance
events_log = []
class SurveillanceHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        event_time = datetime.now()
        events_log.append((event_time, "Modification", event.src_path))
        print(f"Fichier modifié : {event.src_path} à {event_time}")

    def on_created(self, event):
        if event.is_directory:
            return
        event_time = datetime.now()
        events_log.append((event_time, "Création", event.src_path))
        print(f"Fichier créé : {event.src_path} à {event_time}")

    def on_deleted(self, event):
        if event.is_directory:
            return
        event_time = datetime.now()
        events_log.append((event_time, "Suppression", event.src_path))
        print(f"Fichier supprimé : {event.src_path} à {event_time}")

# Fonction pour visualiser les événements
def visualiser_evenements(events_log):
    if not events_log:
        print("Aucun événement détecté.")
        return

    types = [event[1] for event in events_log]
    temps = [event[0] for event in events_log]

    plt.figure(figsize=(10, 5))
    plt.scatter(temps, types, c='blue')
    plt.title("Événements de modification de fichiers")
    plt.xlabel("Temps")
    plt.ylabel("Type d'événement")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("evenements_fichiers.png")
    plt.show()

# Démarrage de la surveillance
def surveiller_repertoire(repertoire):
    event_handler = SurveillanceHandler()
    observer = Observer()
    observer.schedule(event_handler, repertoire, recursive=True)
    observer.start()
    print(f"Surveillance démarrée sur le répertoire : {repertoire}")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Surveillance arrêtée.")
    
    observer.join()
    
    # Sauvegarder les logs dans un fichier
    with open("evenements_log.txt", "w") as f:
        for event_time, event_type, src_path in events_log:
            f.write(f"{event_time} - {event_type} - {src_path}\n")

# Entrée utilisateur
if __name__ == "__main__":
    repertoire = input("Entrez le chemin du répertoire à surveiller : ")
    surveiller_repertoire(repertoire)

    # Visualiser les événements après arrêt
    visualiser_evenements(events_log)
