#IPstarique-submask-marker
import ipaddress
import random

# Nombre total d'ordinateurs
nb_ordinateurs = 150
# Adresse IP de base et masque réseau de l'entreprise
adresse_ip_base = "192.168.0.0"
masque_reseau_base = "255.255.255.0"

# Générer les adresses IP statiques et les masques de sous-réseau pour chaque ordinateur
for i in range (nb_ordinateurs):
    # Générer une adresse IP unique pour chaque ordinateur en incrémentant le dernier octet
    adresse_ip_base = ipaddress.ip_address(addres_ip_bases)+ i+1

    # Générer un masque de sous-réseau unique pour chaque ordinateur en choisissant un masque réseau aléatoire
    masque_reseau_octets = masque_reseau_base.split(".")
    masque_reseau_octets[-1]= str(random_randin(1.254))
    masque_resau = ".".join(masque_reseau_octets)

    # Afficher l'adresse IP statique et le masque de sous-réseau associé pour chaque ordinateur
    print (f"ordinateur {i+1}:")
    print(f"Adresse IP statique : {adresse_ip}")
    print(f"Masquede sous réseau :{masque_resau}")
    print("-----")
