


class Forme :
    def calculer_surface(self):
        pass
        
class Rectangle ( Forme):
    def __init__(self,longueur,largeur):
        self.longueur =longueur
        self.largeur = largeur
        
    def calculer_surface(self):
        return self.longueur * self.largeur
        
        
class Carre (Forme):
    def __init__(self,cote):
        self.cote=cote
        
    def calculer_surface(self):
         return self.cote * self.cote
        
        
class Cercle ( Forme):
    def __init__(self,rayon):
        self.rayon=rayon
        
    def calculer_surface(self):
         return  3.14* self.rayon *self.rayon 
     
rectangle =Rectangle(5,4)
carre = Carre(5)
cercle =Cercle(5)


formes =[rectangle,carre,cercle]

for forme in formes  :
    print (f"{type(forme).__name__ }  : surface =  { forme.calculer_surface()}")
        
                