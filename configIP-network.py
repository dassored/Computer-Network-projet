import os

def configure_ip_address(ip_address, subnet_mask, gateway):
    """
    Fonction pour configurer l'adresse IP sur un poste client.
    Args:
        ip_address (str): Adresse IP à configurer.
        subnet_mask (str): Masque de sous-réseau à configurer.
        gateway (str): Passerelle par défaut à configurer.
    """
# Commandes pour configurer l'adresse IP, le masque de sous-réseau et la passerelle par défaut
    cmd_ip = f"netsh interface ipv4 set address name=\"Ethernet\" static {ip_address} {subnet_mask} {gateway}"
    cmd_gateway = f"netsh interface ipv4 set addressname=\"Ethernet\" gateway={gateway}"

    # Exécution des commandes
    os.system(cmd_ip)
    os.system(cmd_gateway)
    print(f"L'adresse IP {ip_address} a été configurée avec succès !")

# Exemple d'utilisation
ip_address = "192.168.1.100"
subnet_mask = "255.255.255.0"
gateway = "192.168.1.1"

configure_ip_address(ip_address, subnet_mask, gateway)
