from abc import ABC, abstractmethod
# interface
class Vehicule(ABC):
    @abstractmethod
    def demarrer(self):
        pass

    @abstractmethod
    def arreter(self):
        pass
class Voiture(Vehicule):
    def demarrer(self):
        return "La voiture demmarre"

    def arreter(self):
        return "La voiture s'aret."
class Velo(Vehicule):
    def demarrer(self):
        return "Le velo demmare en pedalant "

    def arreter(self):
        return "Le velo s'arret avec le frin manuelle"

   
voiture1 = Voiture()
print(voiture1.demarrer())
print(voiture1.arreter())

velo1 = Velo()
print(velo1.demarrer())
print(velo1.arreter())
