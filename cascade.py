class Grande_parent :
    def __init__(self, nom_grande_parent):
        self.nom_grande_parent = nom_grande_parent
class Parent(Grande_parent) :
    def __init__(self, nom_parent, nom_grande_parent):
        super().__init__(nom_grande_parent)
        self.nom_parent = nom_parent
class Enfant(Parent) :
    def __init__(self,nom_enfant,nom_parent,nom_grande_parent):
        super().__init__(nom_parent,nom_grande_parent)
        self.nom_enfant = nom_enfant
    def to_string(self):
        print("Nom du grand-parent :", self.nom_grande_parent)
        print("Nom du parent :", self.nom_parent)
        print("Nom de l'enfant :", self.nom_enfant)  
        
E1= Enfant("jad","Ahmed/malika","khalid/khadija") 
E1.to_string()