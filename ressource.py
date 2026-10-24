
import gc

class Ressource:
    def __init__(self, nom: str):
        self.nom = nom
        print(f"[INIT] Création de la ressource '{nom}'")

    def __del__(self):
        print(f"[DEL] Destruction de la ressource '{self.nom}'")

    def utiliser(self):
        print(f"[USE] Utilisation de '{self.nom}'")


r = Ressource("Fichier de données")
r.utiliser()

del r

gc.collect()
