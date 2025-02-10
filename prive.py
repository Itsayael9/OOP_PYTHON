class Livre :
    def __init__(self, titre , auteur):
        self.__titre = titre
        self.__auteur = auteur
    def get_titre(self) :
        return self.__titre
    def get_auteur(self) :
        return self.__auteur
    
    def set_titre(self , titre):
        self.__titre = titre 
    def set_auteur(self , auteur):
        self.__auteur = auteur
        
    def afficher_information(self):
        
        print("le titre de ce livre est : ", self.__titre )
        print( "le auteur de ce livre est : ", self.__auteur)
              


livre = Livre("learn Python", "John Doe")
livre.afficher_information()

