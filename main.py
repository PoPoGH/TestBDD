import mysql.connector

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

        # Vous pouvez exécuter des requêtes ou effectuer d'autres opérations ici

except mysql.connector.Error as e:
    print(f"Erreur de connexion à la base de données MySQL: {e}")

finally:
    # Fermez la connexion à la base de données
    if 'connection' in locals():
        connection.close()
