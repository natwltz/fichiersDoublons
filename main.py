import os
import hashlib
import time

class File:
    def __init__(self, chemin):
        self.chemin = chemin
        self.taille = 
        self.hexa = 
        self.date =
        self.signature =



def lister_fichiers_recursivement(repertoire):
    for racine, repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            print(os.path.join(racine, fichier))
 
lister_fichiers_recursivement('c:\\Users')
