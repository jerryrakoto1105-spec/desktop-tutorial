class Employe:
    def _init_(self,nom,age):
     self.nom = nom 
     self.age = age
    
    def se_presenter(self):
     print ("Nom :",self.nom)
     print ("Age :",self.age)
    
    
    
class Developpeur(Employe):
    def _init_(self,nom,age,langage):
       super()._init_(nom,age)
       self.langage = langage 
       
       
    def se_presenter(self):
        super().se_presenter()
        print("langage préféré:", self.langage )
        
        
developpeur1=Developpeur ("soa",25,"python")
    
developpeur1.se_presenter()
    
    
    