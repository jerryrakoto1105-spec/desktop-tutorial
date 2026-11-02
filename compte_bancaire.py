

class Compte_bancaire:
    def __init__(self, nom_titulaire, solde):
        self.nom_titulaire = nom_titulaire
        self.solde = solde

    def Afficher_solde(self):
        print("Nom titulaire :", self.nom_titulaire)
        print("Solde :", self.solde, "Ariary")


class Compte_epargne(Compte_bancaire):
    def __init__(self, nom_titulaire, solde, taux_interet):
        super().__init__(nom_titulaire, solde)
        self.taux_interet = taux_interet

    def Afficher_solde(self):
        super().Afficher_solde()
        print("Taux d'intérêt :", self.taux_interet, "%")

Compte_epargne1 = Compte_epargne("Miora", 500000, 5)
Compte_epargne1.Afficher_solde()
