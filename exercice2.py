class Formation:
    def __init__(self,intitule,duree):
        self.intitule =intitule
        self.duree = duree
    
    
class Etudiant(Formation):
    def __init__(self,nom,age,formation):
        super.__init__(formation)
        self.nom =nom
        self.age =age
        
        
    def affiche_information(self):
        print("nom:", self.nom) 
        print("age:",self.age)  
        print("formation:",self.fomration.intitule)
        
formation =Formation ("devellopeur ",5)

etudiant = Etudiant ("jerry",21)
etudiant1 =Etudiant("domer",22)


etudiant.affiche_information()
etudiant1.affiche_information()

 
        

        