

#
# lister les fichiers d'un répertoire
#

import os
 
def lister_fichiers(repertoire):
    return os.listdir(repertoire)
 
print(lister_fichiers('.'))


#
# lister récursivement les fichiers d'un répertoire
#

import os
 
def lister_fichiers_recursivement(repertoire):
    for racine, repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            print(os.path.join(racine, fichier))
 
lister_fichiers_recursivement('c:\\Users')




#
# obtention d'une signature MD5 d'un fichier sous Python.
#


import hashlib

def calculate_md5(file_path):
    '''calcule le MD5 du fichier nommé file_path'''
    with open(file_path, 'rb') as f:
        hash_md5 = hashlib.md5()
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
print('hash:', calculate_md5('md5.py'))



#
# lecture et affichage en hexadecimal des 5 premiers octets d'un fichier
#

def octets_vers_chaine_hex(octets):
    '''converti la chaine d'octets en format hexadécimal'''
    return ''.join(f'{octet:02x}' for octet in octets)

# Lecture des 5 premiers octets d'un fichier
with open("md5.py", "rb") as f:
    premiers_octets = f.read(5)

# Conversion en chaîne hexadécimale
chaine_hex = octets_vers_chaine_hex(premiers_octets)

print('chaine hexa: ', chaine_hex)


#
# lecture de la date de modification d'un fichier sous python
#

import os
import time

fichier = "md5.py"

# Récupère le temps de modification en secondes depuis l'époque Unix
temps_modification = os.path.getmtime(fichier)

# Convertit en un objet datetime pour une meilleure lisibilité
date_modification = time.ctime(temps_modification)

print("Dernière modification :", date_modification)




#
# lecture des dates de modification des fichier d'un répertoire sous python
#




import os
import time

def afficher_date_modification(dossier):
    for racine, dossiers, fichiers in os.walk(dossier):
        for fichier in fichiers:
            chemin_complet = os.path.join(racine, fichier)
            temps_modification = os.path.getmtime(chemin_complet)
            date_modification = time.ctime(temps_modification)
            print(f"Fichier: {chemin_complet} - Modifié le: {date_modification}")

# Exemple d'utilisation
afficher_date_modification(".")



#
# découpage du nom complet d'un fichier sous python
#


import os

chemin_fichier = "/home/utilisateur/documents/mon_fichier.txt"

print("Ensemble:", chemin_fichier)

# Obtenir le répertoire
repertoire = os.path.dirname(chemin_fichier)
print("Répertoire:", repertoire)

# Obtenir le nom de base
nom_base = os.path.basename(chemin_fichier)
print("Nom de base:", nom_base)

# Séparer nom et extension
nom, extension = os.path.splitext(nom_base)
print("Nom:", nom)
print("Extension:", extension)