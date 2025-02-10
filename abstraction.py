from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def donner_a_manger(self):
        pass

class Cheval(Animal):
    def donner_a_manger(self):
        print("Le cheval mange du foin.")

# Exemple d'utilisation
po = Cheval()
po.donner_a_manger()
