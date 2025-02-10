class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def afficher_information(self):
        print(self.nom, self.age)
    #nv method majeur    
    def est_majeur(self):
        #la personne est majeur ou non 
        return self.age >= 18

class Employe(Personne):
    def __init__(self, nom: str, age: int, salaire: float):
        Personne.__init__(self, nom, age)  
        self.salaire = salaire
        
    #redifinition de la methode est majeur 
    def est_majeur(self):
       return super().est_majeur() and self.age >= 18

    def afficher_information_employe(self):
        print(f"Nom : {self.nom}, Age : {self.age}, Salaire : {self.salaire}")

class Etudiant(Personne):
    def __init__(self, nom: str, age: int, domaine_etude: str):
        Personne.__init__(self, nom, age) 
        self.domaine_etude = domaine_etude
        
    #redifinition de la methode est majeur 
    def est_majeur(self):
       return super().est_majeur() and self.age >= 18

    def afficher_information_etudiant(self):
        print(self.nom, self.age, self.domaine_etude)

class AssistantPedagogique(Employe, Etudiant):
    def __init__(self, nom: str, age: int, salaire: float, domaine_etude: str, heure_de_travail: int):
        Employe.__init__(self, nom, age, salaire) 
        Etudiant.__init__(self, nom, age, domaine_etude)  
        self.heure_de_travail = heure_de_travail

    def afficher_information_assistant(self):
        print(
            f"Nom : {self.nom}, Age : {self.age}, Salaire : {self.salaire}, "
            f"Domaine d'etude : {self.domaine_etude}, Heures de travail : {self.heure_de_travail}"
        )
        
etudiant1 = Etudiant("el bakkali", 26, "economie")
print(etudiant1.est_majeur())

employer1 = Employe("elouahabi",17,300000)
print(employer1.est_majeur())


A1 = AssistantPedagogique("Aya", 19, 90000, "Informatique", 8)
A1.afficher_information_assistant()



