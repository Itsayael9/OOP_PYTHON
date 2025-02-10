from abc import ABC, abstractmethod
import math

class FormeGeometrique(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def aire(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass

    def afficher_nom(self):
        print(f"Forme : {self.nom}")

class Rectangle(FormeGeometrique):
    def __init__(self, nom, longueur, largeur):
        super().__init__(nom)
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

class Cercle(FormeGeometrique):
    def __init__(self, nom, rayon):
        super().__init__(nom)
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon

# Création d'un objet rectangle et affichage des résultats
rectangle1 = Rectangle("Mon Rectangle", 5, 3)
rectangle1.afficher_nom()
print(f"Aire : {rectangle1.aire()}")
print(f"Périmètre : {rectangle1.perimetre()}")

# Création d'un objet cercle et affichage des résultats
cercle1 = Cercle("Mon Cercle", 4)
cercle1.afficher_nom()
print(f"Aire : {cercle1.aire()}")
print(f"Périmètre : {cercle1.perimetre()}")
