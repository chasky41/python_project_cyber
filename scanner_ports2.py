import socket
import matplotlib.pyplot as plt
import ipaddress

def verifier_adresse_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def scanner_ports(ip, ports):
    ports_ouverts = []
    print(f"Démarrage du scan sur {ip}...")
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                if s.connect_ex((ip, port)) == 0:
                    ports_ouverts.append(port)
                    print(f"Port {port} ouvert.")
        except Exception as e:
            print(f"Erreur sur le port {port}: {e}")
    return ports_ouverts

def visualiser_ports(ports_ouverts):
    if not ports_ouverts:
        print("Aucun port ouvert trouvé.")
        return
    
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(ports_ouverts)), ports_ouverts, tick_label=ports_ouverts)
    plt.title("Ports Ouverts")
    plt.xlabel("Index du Port")
    plt.ylabel("Numéro du Port")
    plt.tight_layout()
    plt.savefig("ports_ouverts.png")
    plt.show()
    print("Graphique généré : ports_ouverts.png")

# Adresse IP cible et liste de ports
ip = input("Entrez l'adresse IP de la machine cible : ")

if verifier_adresse_ip(ip):
    ports = range(1, 1025)  # Scanner les ports 1 à 1024
    ports_ouverts = scanner_ports(ip, ports)
    print(f"Ports ouverts : {ports_ouverts}")
    visualiser_ports(ports_ouverts)
else:
    print(f"L'adresse IP {ip} est invalide. Veuillez réessayer.")
