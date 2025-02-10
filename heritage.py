class Mere:
    def __init__(self, nom):
        self.nom_Mere = nom

class Pere:
    def __init__(self, age):
        self.age = age

class Enfant(Mere, Pere):
    def __init__(self, nom_enfant, nom_mere, age):
        super().__init__(nom_mere) 
        Pere.__init__(self, age)  #appele de constructeur de pere 
        self.nom_enfant = nom_enfant

    def to_string(self):
        print("Nom de l'enfant :", self.nom_enfant)
        print("Nom de la mère :", self.nom_Mere)
        print("Âge du père :", self.age)

E1 = Enfant("Ahmed", "Malika", 45)
E1.to_string()


