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

# 2) Somme d'un répertoire (taille des fichiers par catégorie)

# On définit des catégories de fichiers (texte, image, vidéo, audio...).
# On scanne tous les fichiers du dossier et on ajoute leur taille à la bonne catégorie.
# Si un fichier ne rentre dans aucune catégorie, il est classé dans "autre".

def sum_directory(directory):
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

def print_sums(sums):
    """Affiche la taille des fichiers par catégorie."""
    for category, total_size in sums.items():
        print(f"Total {category}: {total_size} octets")

# 3) Comparaison de deux répertoires (identification des doublons dans rep2)
def compare_directories(dir1, dir2):
    """Compare deux répertoires et identifie les doublons dans rep2."""
    files_dir1 = {}
    for root, _, files in os.walk(dir1):
        for file in files:
            file_path = os.path.join(root, file)
            file_obj = File(file_path)
            files_dir1[file_obj.signature] = file_obj
    
    duplicates = []
    for root, _, files in os.walk(dir2):
        for file in files:
            file_path = os.path.join(root, file)
            file_obj = File(file_path)
            if file_obj.signature in files_dir1:
                duplicates.append(file_obj)
    
    return duplicates

def print_comparison(duplicates):
    """Affiche les fichiers en doublon dans rep2."""
    for file in duplicates:
        print(f"Doublon trouvé dans rep2: {file.path}")

# 4) Suppression des doublons dans rep2

def delete_duplicates(duplicates):
    """Supprime les fichiers en doublon dans rep2."""
    for file in duplicates:
        print(f"Suppression de {file.path}")
        os.remove(file.path)
