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


# 1) Analyse d'un répertoire (détection des doublons)

def analyze_directory(directory):
    """Analyse un répertoire et détecte les fichiers en doublon."""
    files_dict = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_obj = File(file_path)
            files_dict[file_obj.signature].append(file_obj)
    
    duplicates = {signature: files for signature, files in files_dict.items() if len(files) > 1}
    return duplicates

def print_duplicates(duplicates):
    """Affiche les fichiers en doublon."""
    for signature, files in duplicates.items():
        print(f"Doublons trouvés pour la signature {signature}:")
        for file in files:
            print(f"  - {file.path}")
