
class JournalTaches:
    def __init__(self, nom_fichier: str = "journal.txt"):
        self.nom_fichier = nom_fichier
        self.fichier = None

    def __enter__(self):
        self.fichier = open(self.nom_fichier, "a", encoding="utf-8")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fichier:
            self.fichier.close()
        return False

    def ajouter_tache(self, description: str):
        if self.fichier:
            self.fichier.write(f"- {description}\n")
        else:
            raise RuntimeError(
                "Le journal n'est pas ouvert. Utilisez 'with'."
            )


# Test du programme
with JournalTaches("taches_demo.txt") as journal:
    journal.ajouter_tache("Réviser la POO")
    journal.ajouter_tache("Faire le TP 1")

# Vérification du contenu
with open("taches_demo.txt", "r", encoding="utf-8") as f:
    print(f.read())
