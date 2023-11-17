import pytest
from compteSimple import *
@pytest.fixture 
def p1():
    return Personne("Martin", "Dupont")


def p2():
    return Personne("JEan", "Benrard")

@pytest.fixture 
def c1():
    return CompteSimple( p1,25)


@pytest.fixture 
def c2():
    return CompteCourant( p2,45)

@pytest.fixture 
def b1():
    b1 = Banque()
    b1.ouvrir_compte(p1,35)
    b1.ouvrir_compte(p2,20)
    return b1

@pytest.fixture 
def b2():
    b2 = Banque()
    b2.ouvrir_compte(p1,35)
    b2.ouvrir_compte_courant(p2,20)
    return b2



def test_numero_compte(c1,c2):
    assert c1.numero_compte == 10001
    assert c2.numero_compte == 10002

def test_crediter(c1):
    c1.crediter(15)
    assert c1.solde == 40
def test_debiter(c1):
    c1.debiter(15)
    assert c1.solde == 10

def test_calcul_total_argent(b1):
    assert b1.total_argent() == 55


def test_prelever_frais(b1):

    b1.prelever_frais(15)
    assert b1.total_argent() == 25

def test_credit_compte_courant(c2):
    c2.crediter(15)
    assert c2.solde == 60


def test_debiter_compte_courant(c2):
    c2.debiter(15)
    assert c2.solde == 30

# def test_editer_relever_compte_courant(capfd,c2):
#     c2.crediter(15)
#     c2.debiter(25)
#     c2.editer_releve()
#     out, _ = capfd.readouterr()
#     assert out == "Credit de 15 euros\nDebit de -25 euros\n"


def test_calcul_total_argent_different_type_de_compte(b2):
    assert b2.total_argent() == 55


def test_prelever_frais_different_type_de_compte(b2):
    b2.prelever_frais(15)
    assert b2.total_argent() == 25


# def test_editer_releve_comptes(capfd, b2):
#     b2.prelever_frais(15)
#     b2.editer_releve_comptes()
#     out, _ = capfd.readouterr()
#     assert out == "Debit de -15 euros\n"

