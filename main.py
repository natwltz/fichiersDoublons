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

    def comparaisons(self, other):
        """Compare deux fichiers par leur signature MD5 et leur taille."""
        return self.signature == other.signature and self.size == other.size

    
    def representation(self):
        """Représentation lisible de l'objet File."""
        return f"File(name={self.name}, size={self.size}, date={self.date}, signature={self.signature})"

# 1) Analyse d'un répertoire (détection des doublons)
def analyse_repertoire(directory):
    """Analyse un répertoire et détecte les fichiers en doublon."""
    files_dict = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_obj = File(file_path)
            if file_obj.signature not in files_dict:
                files_dict[file_obj.signature] = []
            files_dict[file_obj.signature].append(file_obj)
    
    duplicates = {signature: files for signature, files in files_dict.items() if len(files) > 1}
    return duplicates

def print_doublons(duplicates):
    """Affiche les fichiers en doublon."""
    for signature, files in duplicates.items():
        print(f"Doublons trouvés pour la signature {signature}:")
        for file in files:
            print(f"  - {file.path}")

# 2) Somme d'un répertoire (taille des fichiers par catégorie)
def sommes_repertoire(directory):
    """Calcule la taille des fichiers par catégorie."""
    categories = {
        'texte': ['txt', 'doc', 'docx', 'odt', 'csv', 'xls', 'ppt', 'odp'],
        'images': ['jpg', 'png', 'bmp', 'gif', 'svg'],
        'video': ['mp4', 'avi', 'mov', 'mpeg', 'wmv'],
        'audio': ['mp3', 'mp2', 'wav', 'bwf'],
        'autre': []
    }
    
    sums = {category: 0 for category in categories}
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_obj = File(file_path)
            ext = file.split('.')[-1].lower()
            found = False
            for category, exts in categories.items():
                if ext in exts:
                    sums[category] += file_obj.size
                    found = True
                    break
            if not found:
                sums['autre'] += file_obj.size
    
    return sums