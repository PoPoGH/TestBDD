# Test de Connexion MySQL en Python

Ce projet contient un code Python simple pour tester une connexion à une base de données MySQL en utilisant le module `mysql-connector-python`. Ce code vous permettra de vérifier si vous pouvez vous connecter à votre base de données MySQL depuis votre application Python.

## Configuration requise

Avant d'utiliser ce code, assurez-vous d'avoir les éléments suivants installés :

- Python : Assurez-vous d'avoir Python installé sur votre système. Vous pouvez le télécharger depuis [python.org](https://www.python.org/downloads/).

- MySQL : Vous devez avoir un serveur MySQL en cours d'exécution et connaître les informations de connexion nécessaires, telles que l'hôte, le nom d'utilisateur, le mot de passe et le nom de la base de données.

- Module MySQL Connector : Vous devez installer le module `mysql-connector-python` en utilisant `pip` :

pip install mysql-connector-python

## Utilisation

1. Clonez ce référentiel sur votre machine locale en utilisant la commande suivante :

git clone https://github.com/VotreNomDeCompte/connexion-mysql-python.git

2. Modifiez le fichier `connexion_mysql.py` pour mettre à jour les informations de connexion à votre base de données MySQL. Remplacez les valeurs suivantes :

```python
host = "votre-hote"
utilisateur = "votre-utilisateur"
mot_de_passe = "votre-mot-de-passe"
base_de_donnees = "votre-base-de-donnees"
Exécutez le script en utilisant la commande suivante :

python connexion_mysql.py
Vous devriez voir un message indiquant si la connexion à la base de données MySQL a réussi ou échoué.

Journalisation
Ce projet inclut désormais la journalisation des événements dans un fichier texte (log.txt). Les journaux incluent des informations sur la réussite ou l'échec de la connexion, ainsi que des détails sur l'hôte de la connexion.

Contribuer
Si vous souhaitez contribuer à ce projet, vous pouvez ouvrir une demande d'extraction (pull request) avec vos modifications/améliorations.