class Personne:
    #attribut de la classe partager par tout les instances
    nom_etablissement = "cmc tanger"
    

    def __init__(self,nom,prenom,age): #__init__
        self.nom = nom
        self.prenom = prenom
        self.age = age
        
    def afficher_information(self):
        #methode pour afficher les information
        print(f"Nom: {self.nom}")
        print(f"Prenom: {self.prenom}")
        print(f"Age: {self.age}")
        print(f"Etablissement: {self.nom_etablissement}")
        
        
personne1 = Personne("aya","el ouahabi",19)
personne1.afficher_information()

personne2 = Personne("sara","loudiy",20)
personne2.afficher_information()

personne3 = Personne("ihssane","khalil",20)
personne3.afficher_information()