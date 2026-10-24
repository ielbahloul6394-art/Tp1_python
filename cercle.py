
import math

class Cercle:
    def __init__(self, rayon: float):
        self.rayon = rayon

    @property
    def rayon(self):
        return self._rayon

    @rayon.setter
    def rayon(self, valeur: float):
        if valeur <= 0:
            raise ValueError("Le rayon doit être strictement positif.")
        self._rayon = valeur

    def aire(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def __str__(self):
        return f"Cercle(rayon={self.rayon})"


# Test du programme
c = Cercle(5.0)

print(c)
print("Aire :", c.aire())
print("Périmètre :", c.perimetre())

try:
    c.rayon = -10
except ValueError as e:
    print("Erreur interceptée :", e)


