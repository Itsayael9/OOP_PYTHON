class Livre:
    def __init__(self,titre,auteur,nb_pages):
        try :
            if not isinstance(nb_pages,int) or nb_pages <=0 :
                raise ValueError("le nombre de pages doit etre un entier positif ")
            self.titre = titre 
            self.auteur  = auteur 
            self.nb_pages = nb_pages
        except ValueError as e :
            print(f"erreur lors de la creation de livre {e}")
        else:
            print(f"le nv livre a ete cree avec succes ")
        finally:
            print("fin de l'operation")
class Biblio :
    def __init__(self):
        self.livres = []
    def ajouter_livre(self,livre):
        try:
            if not isinstance(livre,Livre):
                raise TypeError("l'objet ajoute doit etre une nstance de la class livre ")
            self.livres.append(livre)
        except TypeError as e :
            print(f"erreur lors de la j'ajoute :{e}")
        else:
            print("le livre a ete ajouter avec succes ")
        finally :
            print("fin de l'opertaion d'ajoute ")
def supprimer_livre(self, titre):
    try:
        livre_a_supprimer = None
        for livre in self.livres:
            if livre.titre == titre:
                livre_a_supprimer = livre
                break
        
        if livre_a_supprimer is None:
            raise KeyError(f"Le livre avec ce titre n'existe pas")
        
        self.livres.remove(livre_a_supprimer)
    except KeyError as ke:
        print(f"Erreur lors de la suppression : {ke}")
    else:
        print("Le livre a été supprimé")
    finally:
        print("fin de l'operation du suppression")
    
    
biblio1= Biblio()

livre1 =Livre("la boite a merveille","ahmda sefriou ",323) 
biblio1.ajouter_livre("livre2")
biblio1.supprimer_livre("livre enixistant ")        
            