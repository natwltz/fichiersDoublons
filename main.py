import os
import hashlib
import time

class File:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.size = os.path.getsize(path)
        self.date = time.ctime(os.path.getmtime(path))
        self.signature = self.calculate_md5()
        self.first_bytes = self.get_first_bytes()



def lister_fichiers_recursivement(repertoire):
    for racine, repertoires, fichiers in os.walk(repertoire):
        for fichier in fichiers:
            print(os.path.join(racine, fichier))
 
lister_fichiers_recursivement('c:\\Users')
