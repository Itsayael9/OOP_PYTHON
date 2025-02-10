class Etudiant:
    def __init__(self):
        
        self.etudiants = []

    def AjouterEtudiant(self, nom):
        if nom not in self.etudiants:
            self.etudiants.append(nom)
            print(f"L'étudiant {nom} a été ajouté à la liste.")
        else:
            print(f"L'étudiant {nom} est déjà dans la liste.")

    def SupprimeEtudiant(self, nom):
        if nom in self.etudiants:
            self.etudiants.remove(nom)
            print(f"L'étudiant {nom} a été supprimé de la liste.")
        else:
            print(f"L'étudiant {nom} n'existe pas dans la liste.")

    def AfficherEtudiant(self):
        if self.etudiants:
            print("Voici la liste des étudiants :")
            for etudiant in self.etudiants:
                print(etudiant)
        else:
            print("La liste des étudiants est vide.")

    def Recherche(self, nom):
        if nom in self.etudiants:
            print(f"L'étudiant {nom} est dans la liste.")
        else:
            print(f"L'étudiant {nom} n'existe pas dans la liste.")

    def triAlphabetique(self):
        self.etudiants.sort()
        print("La liste des étudiants a été triée par ordre alphabétique.")

    def modification(self, ancien_nom, nouveau_nom):
        if ancien_nom in self.etudiants:
            index = self.etudiants.index(ancien_nom)
            self.etudiants[index] = nouveau_nom
            print(f"Le nom de l'étudiant a été modifié de {ancien_nom} à {nouveau_nom}.")
        else:
            print(f"L'étudiant {ancien_nom} n'existe pas dans la liste.")

def afficher_menu():
    eleve = Etudiant() #instantiation 

    while True:
        print("\n-------- MENU --------")
        print("1. Ajouter un étudiant")
        print("2. Supprimer un étudiant")
        print("3. Afficher la liste des étudiants")
        print("4. Rechercher un étudiant")
        print("5. Trier la liste alphabétiquement")
        print("6. Modifier un étudiant")
        print("7. Quitter")

        choix = input("Entrez votre choix : ").strip()#efface de l'espace 

        if choix == "1":
            nom_ajouter = input("Entrez le nom de l'étudiant à ajouter : ").strip()
            eleve.AjouterEtudiant(nom_ajouter)
        elif choix == "2":
            nom_supprimer = input("Entrez le nom de l'étudiant à supprimer : ").strip()
            eleve.SupprimeEtudiant(nom_supprimer)
        elif choix == "3":
            eleve.AfficherEtudiant()
        elif choix == "4":
            nom_recherche = input("Entrez le nom de l'étudiant à rechercher : ").strip()
            eleve.Recherche(nom_recherche)
        elif choix == "5":
            eleve.triAlphabetique()
        elif choix == "6":
            ancien_nom = input("Entrez le nom de l'étudiant à modifier : ").strip()
            nouveau_nom = input("Entrez le nouveau nom : ").strip()
            eleve.modification(ancien_nom, nouveau_nom)
        elif choix == "7":
            print("Fin du programme.")
            break
        else:
            print("Choix non valide. Veuillez réessayer.")

if __name__ == "__main__":
    afficher_menu()
