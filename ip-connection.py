import subprocess
import platform

# Demande à l'utilisateur d'entrer l'adresse IP ou le nom d'hôte
adresse = input("Entrez l'adresse IP ou le nom d'hôte à vérifier : ")

# Vérifie le système d'exploitation
syst_exploitation = platform.system()

# Exécute la commande de ping en fonction du système d'exploitation
if syst_exploitation == 'Windows':
    commande_ping = ['ping', '-n', '1', adresse]
elif syst_exploitation == 'Linux' or syst_exploitation == 'Darwin':
    commande_ping = ['ping', '-c', '1', adresse]
else:
    print("Système d'exploitation non pris en charge.")
    exit()

# Exécute la commande de ping et capture la sortie
resultat_ping = subprocess.run(commande_ping, stdout=subprocess.PIPE)

# Vérifie si l'hôte est en ligne ou hors ligne
if resultat_ping.returncode == 0:
    print(f"L'hôte {adresse} est en ligne.")
else:
    print(f"L'hôte {adresse} est hors ligne.")
