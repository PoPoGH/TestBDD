import mysql.connector
import logging

# Configuration de la journalisation avec l'encodage UTF-8
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s', encoding='utf-8')

# Paramètres de connexion à la base de données
config = {
    'user': 'user',
    'password': 'pass',
    'host': '127.0.0.1',  # Adresse IP ou nom d'hôte du serveur MySQL
    'port': 3306,  # Numéro de port MySQL
    'database': 'database',  # Remplacez par le nom de votre base de données
}

# Tentative de connexion à la base de données
try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Connexion réussie à la base de données MySQL")
        logging.info(f"Connexion réussie à la base de données MySQL sur l'hôte {config['host']}")

        # Vous pouvez exécuter des requêtes ou effectuer d'autres opérations ici

except mysql.connector.Error as e:
    error_message = f"Erreur de connexion à la base de données MySQL: {e}"
    print(error_message)
    logging.error(error_message)

finally:
    # Fermez la connexion à la base de données
    if 'connection' in locals():
        connection.close()
