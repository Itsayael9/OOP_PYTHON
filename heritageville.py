class pays:
    #constructeur 
    def __init__(self,nom_pays):
        self.nom_pays = nom_pays

class ville(pays):#heritage de pays 
    def __init__(self,surface_ville,nom_ville ,nom_pays):
        super().__init__(nom_pays)
        self.surface_ville = surface_ville        
        self.nom_ville = nom_ville
        
    #affichage de siple methode 
    def to_string(self):
        print(self.surface_ville) 
        print(self.nom_pays)
        print(self.nom_ville)
V1 = ville("5000m2","tanger","marroc")
V1.to_string()