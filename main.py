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
            
    def calculate_md5(self, chunk_size=4096):
        """Calcule la signature MD5 du fichier."""
        with open(self.path, "rb") as f:
            hash_md5 = hashlib.md5()
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hash_md5.update(chunk)
            return hash_md5.hexdigest()

    def octets_vers_chaine_hex(self, num_bytes=5):
        """Lit les 5 premiers octets du fichier et les convertit en hexadécimal."""
        with open(self.path, "rb") as f:
            premiers_octets = f.read(num_bytes)
            return ''.join(f'{octet:02x}' for octet in premiers_octets)

    def afficher_date_modification(self):
        """Récupère la date de modification du fichier."""
        temps_modification = os.path.getmtime(self.path)
        return time.ctime(temps_modification)