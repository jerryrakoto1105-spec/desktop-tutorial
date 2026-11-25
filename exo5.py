class Apprenant:
    def __init__(self,nom,identifiant,):
        self.nom = nom
        self.identifiant=identifiant
        self.modules=[]
        
    def inscrire(self,modules):
        
         self.modules.append(modules)
         
    def afficher_module(self):
        print (f"name :{self.nom}" )
        print(f"id :{self.identifiant }" )
        print (" tracking_module : ")
        
        
        for module in self.modules:
            
         print (f"{module.titre}({module.nombre_heures} heures)")
            
            
        
class Module:
    def __init__(self,titre,nombre_heures):
        self.titre=titre
        self.nombre_heures=nombre_heures
        
apprenant1 =Apprenant("jean",100)
apprenant2 = Apprenant("mickael",101)
apprenant3 = Apprenant ("faneva",105)


module1 =Module ( "html" ,10)
module2 =Module ("python",12)
module3 =Module ( "js",20)


apprenant1.inscrire (module1)
apprenant2.inscrire (module2)
apprenant3.inscrire (module3)

apprenant1.afficher_module()
apprenant2.afficher_module()
