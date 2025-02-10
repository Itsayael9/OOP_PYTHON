class Vehicule :
    def __init__(self,couleur,anne,marque="non specifie",model="non specifie"):
        self.couleur=couleur
        self.anne=anne
        self.marque=marque
        self.model=model

    def toString(self):
        print (" la couleur est:" ,self.couleur)
        print (" l'anne :" ,self.anne)
        print (" la marque est :" ,self.marque)
        print (" le model est:",self.model)

V1 = Vehicule("noir","2000","dacia")
V1.toString()

V2= Vehicule("blanch","2010", "turan")
V2.toString()

V3 = Vehicule("rouge","2014","pegeu","208")
V3.toString()


