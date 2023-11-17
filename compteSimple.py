

class Personne:
    def __init__(self, nom, prenom):
        self.prenom = prenom
        self.nom = nom

    def __str__(self) -> str:
        return f"{self.nom} {self.prenom}"


class CompteSimple:

    numero_compte_courant = 10000

    def __init__(self, titulaire: Personne, depot=0 ):
        self.__solde = depot
        self.titulaire = titulaire
        self.numero_compte =  CompteSimple.numero_compte_courant + 1
        CompteSimple.numero_compte_courant += 1 

    @property # accès en lecture à solde, comme si c’était un attribut
    def solde(self):
        return self.__solde

    def crediter(self, montant):
        if(montant >0):                
            self.__solde += montant
        else:
            raise ValueError

    def debiter(self, montant):    
        if(montant >0):                
            self.__solde -= montant
        else:
            raise ValueError

    def __str__(self) -> str:
        return f"le Solde de {self.titulaire} est de : {self.__solde}  euros"
    


class Banque: 
    def __init__(self):
        self.__comptes = []

    def ouvrir_compte(self, client , depot):
         compte_ouvert = CompteSimple(client, depot)              
         self.__comptes.append(compte_ouvert)
         return compte_ouvert
    
    def ouvrir_compte_courant(self, client , depot):
         compte_ouvert = CompteCourant(client, depot)              
         self.__comptes.append(compte_ouvert)
         return compte_ouvert
    @property # accès en lecture à solde, comme si c’était un attribut
    def somme_solde(self):
        return sum(compte.solde for compte in self.__comptes)

        
    def prelever_frais(self, montant_frais):
        for compte in self.__comptes:
            compte.debiter(montant_frais)

    def editer_releve_comptes(self):
        for compte in self.__comptes:
            try:
                compte.editer_releve()
            except AttributeError: 
                print("Aucun relevé pour ce compte")
                



class CompteCourant(CompteSimple):
    def __init__(self, titulaire: Personne, depot=0):
        super().__init__(titulaire, depot)
        if depot != 0:
            self.__operations = []

    def crediter(self, montant):                
         super().crediter(montant)
         self.__operations.append(montant)

    def debiter(self, montant):    
        super().debiter(montant)
        self.__operations.append(-montant)
    
    def editer_releve(self):
        print (f"Relevé du compte numéro {self.numero_compte} :")
        for operation in self.__operations:
            if operation > 0:
                print(f"Credit de {operation} euros")
            else:
                print(f"Debit de {operation} euros")