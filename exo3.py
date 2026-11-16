class Produit :
    def __init__(self,nom ,prix):
       self.nom=nom
       self.prix=prix
        
class Commande:
    def __init__(self,produit,quantité):
        self.produit=produit
        self.quantité=quantité
        
    def calculer_total(self):
        return self.produit.prix * self.quantité
        
    def afficher_commande(self):
        print ( "product_name :",self.produit.nom )
        print ( "quantity :",self.quantité)
        print ( "total_amount:",self.calculer_total(), "Ariary ")
        
        
produit1 = Produit("ordinateur",80000)
commande1= Commande (produit1 ,2)



commande1.afficher_commande()
        
