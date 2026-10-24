
import functools

def valider_positif(*indices: int):
    """Décorateur qui valide que les arguments aux indices donnés sont positifs."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for idx in indices:
                if idx < len(args):
                    value = args[idx]
                else:
                    continue

                if not isinstance(value, (int, float)) or value <= 0:
                    raise ValueError(
                        f"L'argument à l'index {idx} doit être un nombre positif."
                    )

            return func(*args, **kwargs)
        return wrapper
    return decorator


class Rectangle:
    def __init__(self, largeur: float, hauteur: float):
        if largeur <= 0 or hauteur <= 0:
            raise ValueError("La largeur et la hauteur doivent être positives.")

        self.largeur = largeur
        self.hauteur = hauteur

    @valider_positif(1)
    def aire(self, facteur: float = 1.0) -> float:
        return self.largeur * self.hauteur * facteur


# Programme principal
rect = Rectangle(5, 10)

print(rect.aire())  # 50.0

try:
    rect.aire(-1)
except ValueError as e:
    print(e)
