#nom d'hôte et l'adresse IP de la machine locale#
import socket

# Obtient le nom d'hôte et l'adresse IP de la machine locale
nom_hote = socket.gethostname()
adresse_ip = socket.gethostbyname(nom_hote)

# Affiche les informations d'adresse IP
print ("Informations d'adresse IP :")
print(f"Nom d'hôte : {nom_hote}")
print(f"Adresse IP : {adresse_ip}")
