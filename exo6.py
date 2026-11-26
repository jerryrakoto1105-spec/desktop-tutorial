class Module :
    def __init__(self, titre, duree):
        self.titre =titre
        self.duree =duree
class Formation :
    
    def __init__(self,intitule):
        self.intitule=intitule
        self.module = []
        
    def ajouter_module(self,modules):
      self.module.append(modules )
      
      
class Apprenant :
    def __init__(self,nom,):
        self.nom =nom
        self.formations =[]
        
        
    def S_inscrire (self ,formations ):
        self.formations.append(formations)
         
    def Afficher_parcours(self):
        print (f" parcour de  {self.nom}")
    
        for Formation in self.formations :
        
            print (f" formation : {Formation.intitule}")
    
            for module in Formation.module:
        
                print (f"{module.titre}  ({module.duree} heures)")
         
module = Module("Python",24)
module1 = Module("PPO",24)
module2 = Module("html",24)
module3 = Module("sql",24)


formation1 =Formation ( "devellopement python")
formation1.ajouter_module(module)
formation1.ajouter_module(module1)

formation2 =Formation ("devellopement web")
formation2.ajouter_module(module2)
formation2.ajouter_module(module3)



apprenant =Apprenant ( "jerry")
apprenant1 =Apprenant ( "Domer")

apprenant .S_inscrire (formation1)
apprenant1.S_inscrire ( formation2)


apprenant .Afficher_parcours()
apprenant1 .Afficher_parcours()











        
    
        
    
       
        
        