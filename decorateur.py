class Livre:
    def __init__(self, titre, auteur):
        self.__titre = titre
        self.__auteur = auteur 
    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, nv_titre):
        self.__titre = nv_titre

    @property
    def auteur(self):
        return self.__auteur

    @auteur.setter
    def auteur(self, nv_auteur):
        self.__auteur = nv_auteur

    def afficher_information(self):
        print("le titre de ce livre est : ", self.__titre)
        print("le auteur de ce livre est : ", self.__auteur)
    

livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupery")
livre1.afficher_information()