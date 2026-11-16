class Formation:
    def __init__(self,intitule,duree):
        self.intitule =intitule
        self.duree = duree
    
    
class Etudiant:
    def __init__(self,nom,age,formation):
        self.formation =formation
        self.nom =nom
        self.age =age
        
        
    def affiche_information(self):
       print(f"{self.nom} est s'inscrits en {self.formation.intitule}.")
        
formation =Formation ("devellopeur ",5)
etudiant1 =Etudiant ("jerry",21,formation)
etudiant2 =Etudiant("domer",22,formation)


etudiant1.affiche_information()
etudiant2.affiche_information()

 
        

        