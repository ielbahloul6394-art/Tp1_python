class Article:
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def valeur_stock(self) -> float:
        """Calcule la valeur totale du stock en HT."""
        return self.prix_ht * self.stock

    def ajouter_stock(self, quantite: int):
        """Ajoute une quantité au stock actuel."""
        if quantite < 0:
            raise ValueError("La quantité ajoutée ne peut pas être négative.")
        self.stock += quantite

    def __str__(self):
        return f"[{self.reference}] {self.designation} - Stock: {self.stock} - Prix HT: {self.prix_ht:.2f}€"
    
article1 = Article("A001", "Clavier", 150.0, 10)

print(article1)
print("Valeur du stock :", article1.valeur_stock(), "DH")

article1.ajouter_stock(5)

print("Après ajout :", article1)
print("Nouvelle valeur :", article1.valeur_stock(), "DH")
