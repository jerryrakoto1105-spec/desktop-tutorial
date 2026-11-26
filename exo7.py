class Transport:
    def se_deplacer(self):
       print ("le transport se deplace")
       
class Voiture(Transport):
    def se_deplacer(self):
        print ("le voiture se deplace sur la route.")
        
class Avion(Transport):
    def se_deplacer(self):
        print ("lavion vole dans les airs.")
class Bateau(Transport):
    def se_deplacer(self):
        print ("le bateau navigue sur l'eau.")
        
voiture= Voiture()
avion=Avion()
bateau =Bateau()


transports =[voiture,avion,bateau]
for transport in transports:
    transport.se_deplacer()


