class Livre:
    def __init__(self,titre,auteur,annee):
        self.titre = titre
        self.auteur=auteur
        self.annee =annee
        
    def afficher_details(self):
        print("Name:",self.titre)
        print("Writter:",self.auteur)
        print("Years:",self.annee)
    
class Bibliotheque:
    def __init__(self):
        self.livres = []
        
    def ajouter_livre(self ,livres):
       
          self.livres.append(livres)
        
    def afficher_catalogue(self):
        for livre in self.livres:
            livre .afficher_details()
            
            
            

livre1 =Livre ("python", "mika",2024)
 
livre2 =Livre ("html", "domer",2026) 

livre3= Livre ("js" , "isma",2020)


biblio =Bibliotheque()

biblio.ajouter_livre(livre1 )
biblio.ajouter_livre(livre2 )
biblio.ajouter_livre(livre3 )


biblio.afficher_catalogue()