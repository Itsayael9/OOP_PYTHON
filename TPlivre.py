class Livre :
    def __init__(self,titre,auteur,nb_pages):
         # le nombre doit etre positive et et un entier 
        if not isinstance(nb_pages, int) or nb_pages <= 0:
            raise ValueError("le nombre de page doit etre un entier positive ")
        self.titre= titre 
        self.auteur = auteur 
        self.nb_pages= nb_pages
   
class Biblio :
    def __init__(self):
        self.livres = [] 
    def ajouter_livre(self, livre):
        if livre not in self.livres :
            self.livres.append(livre)
            print("le livre a ete a ajouter ")
        else:
            print("le livre deja existe dans la liste ")
            
    def supprimer_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                self.livres.remove(livre)
            else:  
                raise ValueError("Le livre n existe pas")  

try:              
    L1 = Livre("python","aya",4)
    b1=Biblio()
    b1.ajouter_livre(L1)
except TypeError as e :
    print(f"{e}")
finally:
    print("fin d'operation ")

try:              
    L2 = Livre("js","amal",-4)
    b2=Biblio()
    b2.ajouter_livre(L2)
except ValueError as e :
    print(f"{e}")
finally:
    print("fin d'operation ")
    

      