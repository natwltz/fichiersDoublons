import os
import hashlib
import time

class File:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.size = os.path.getsize(path)
        self.date = self.afficher_date_modification()
        self.signature = self.calculate_md5()
        self.first_bytes = self.octets_vers_chaine_hex()

