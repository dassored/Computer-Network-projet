#easy-Static-IPadress

import ipaddress

base_ip ="192.168.2.0" # Adresse IP de départ
increment = 1 # Valeur d'incrément pour générer les adresses IP
num_computers = 100 

# Convertir l'adresse IP de départ en un objet ipaddress.IPv4Address
ip = ipaddress.ip_address(base_ip)

# Générer les adresses IP pour chaque ordinateur en utilisant l'incrément
for i in range(num_computers):
    # Afficher l'adresse IP générée
    print(f"Adresse IP pour ordinateur {i+1}: {ip}")

    # Incrémenter l'adresse IP pour le prochain ordinateur
    ip += increment

