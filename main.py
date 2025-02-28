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

    def calculate_md5(self, chunk_size=4096):
        """Calcule la signature MD5 du fichier."""
        hash_md5 = hashlib.md5()
        with open(self.path, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def get_first_bytes(self, num_bytes=5):
        """Lit les 5 premiers octets du fichier et les convertit en hexadécimal."""
        with open(self.path, "rb") as f:
            return ''.join(f'{byte:02x}' for byte in f.read(num_bytes))

    def __eq__(self, other):
        """Compare deux fichiers par leur signature MD5 et leur taille."""
        return self.signature == other.signature and self.size == other.size

    def __repr__(self):
        """Représentation lisible de l'objet File."""
        return f"File(name={self.name}, size={self.size}, date={self.date}, signature={self.signature})"
