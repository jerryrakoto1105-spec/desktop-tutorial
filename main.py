class Moteur:
    def __init__(self,marque,puissance):
        self.marque =marque
        self.puissance =puissance
        
        
    def demarrer(self):
        print ("le moteur démarre")
        
class Voiture:
    
    def _init_(self,moteur):
        self.moteur=moteur
        
    def demarrer(self):
        self.moteur.demarrer()
        
        
voiture =Moteur ("TOYOTA",120)




voiture.demarrer()