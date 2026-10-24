
from contact import Contact
from carnet import Carnet

carnet = Carnet()

c1 = Contact("Alice Dupont", "0612345678", "alice@example.com")
c2 = Contact("Bob Martin", "0698765432", "bob@example.com")

carnet.ajouter(c1)
carnet.ajouter(c2)

print(c1.initiale)

resultats = carnet.chercher("ali")
print(resultats)

print(len(carnet))
