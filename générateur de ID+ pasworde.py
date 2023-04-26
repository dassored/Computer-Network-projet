import random
import string

def generate_wifi_name():
    """Génère un nom de réseau Wi-Fi aléatoire"""
    adjectives = ['Mark', 'MSG', 'Red', 'black', 'MS', 'RS', 'KNIGHTS', '', 'RX-0']
    nouns = ['89', '1000', 'II', 'III', 'ptoto', 'dragon', 'lighning', 'Star', 'stormbreaker', 'break']
    return random.choice(adjectives) + '-' + random.choice(nouns)

def generate_wifi_password():
    """Génère un mot de passe Wi-Fi complexe"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(15))
    return password

# Générer un nom de réseau Wi-Fi et un mot de passe
wifi_name = generate_wifi_name()
wifi_password = generate_wifi_password()

# Afficher le résultat
print("Nom de réseau Wi-Fi : ", wifi_name)
print("Mot de passe Wi-Fi : ", wifi_password)