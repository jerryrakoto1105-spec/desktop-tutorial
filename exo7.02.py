class Employe :
    def __init__(self,nom,salaire_base):
        self .nom= nom
        self.salaire_base= salaire_base
        
    def calculer_salaire(self):
        return self.salaire_base
    
class Developpeur(Employe):
    def __init__(self,nom,salaire_base,prime_technique):
        super().__init__(nom,salaire_base)
        self .prime_technique = prime_technique
    def calculer_salaire(self):
        return self.salaire_base +self.prime_technique
        
        
class Commercial(Employe):
    def __init__(self,nom,salaire_base,commission):
        super().__init__(nom,salaire_base)
        self.commission =commission
        
    def calculer_salaire(self):
            return self.salaire_base + self.commission
        
    
developpeur1=Developpeur("jerry",15000 ,5000)
developpeur2=Developpeur("domer",25000,5000)
developpeur3=Developpeur("tsila",20000,2000)

commercial1= Commercial("faneva",50000,10000)
commercial2=Commercial("Mika",40000,10000)
commercial3=Commercial("Ranto",60000,8000)

Employes =[developpeur1,developpeur2,developpeur3, commercial1, commercial2,commercial3] 

for employe in Employes:
    print ( f"{employe.nom } : {employe.calculer_salaire()} Ariary")


        
        
        
        
    
        