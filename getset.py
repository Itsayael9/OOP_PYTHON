class Adherent: 
    # Constructeur avec des attributs privés 
    def __init__(self, nom, age, prenom):
        self.__nom = nom
        self.__age = age
        self.__prenom = prenom

    # Getter pour le nom
    @property
    def nom(self):
        return self.__nom

    # Setter pour le nom
    @nom.setter
    def nom(self, nv_nom):
        self.__nom = nv_nom 

    # Getter pour l'âge
    @property
    def age(self):
        return self.__age

    # Setter pour l'âge
    @age.setter
    def age(self, nv_age):
        self.__age = nv_age

    # Getter pour le prénom
    @property
    def prenom(self):
        return self.__prenom

    # Setter pour le prénom
    @prenom.setter
    def prenom(self, nv_prenom):
        self.__prenom = nv_prenom

    # Méthode pour savoir si l'adhérent est majeur
    def majeur(self):
        return self.__age >= 18


# Instanciation de la classe
A1 = Adherent("Aya", 19, "El Ouahabi")

# Affichage des informations en utilisant les getters
print("Le nom est :", A1.nom)
print("L'âge est :", A1.age)
print("Le prénom est :", A1.prenom)

# Vérification de la majorité
print("\nEst majeur :", A1.majeur())

# Modification des attributs avec les setters (avec l'affectation)
A1.nom = "Eya"
A1.age = 17
A1.prenom = "Ben Salah"

# Affichage après modification avec les getters
print("\nAprès modification :")
print("Le nom est :", A1.nom)
print("L'âge est :", A1.age)
print("Le prénom est :", A1.prenom)

# Vérification de la majorité après modification
print("\nEst majeur :", A1.majeur())
