import pytest
from compteSimple import *


p1 = Personne("Martin", "Dupont")
p2 = Personne("Jean", "Benrard")

c1 = CompteSimple( p1,25)
c2 = CompteCourant( p2,45)
c2.editer_releve()
b1 = Banque()
b1.ouvrir_compte(p1,35)
b1.ouvrir_compte(p2,20)


b2 = Banque()
b2.ouvrir_compte(p1,35)
b2.ouvrir_compte_courant(p2,20)



c2.crediter(15)
c2.debiter(25)
c2.editer_releve()
c1.crediter(15)
c1.debiter(25)


total = b1.total_argent()
print(total)
b1.prelever_frais(15)
total2 = b1.total_argent()
print(total2)
b1.editer_releve_comptes()



b2.prelever_frais(15)
b2.editer_releve_comptes()
total3 = b2.total_argent()
print(total3)