class Etudiant:
    def __init__(self, fichier):
        self.fichier = fichier

    def AjouterEtudiant(self, nom):
        with open(self.fichier, "a") as file:
            file.write(nom.strip() + "\n")
        print(f"L'étudiant {nom} a ete ajouter  dans le fichier {self.fichier}.")

    def SupprimeEtudiant(self, nom):
        with open(self.fichier, "r") as file:
            lignes = file.readlines()

        nom = nom.strip() + "\n"
        if nom in lignes:
            lignes.remove(nom)
            with open(self.fichier, "w") as file:
                file.writelines(lignes) 
            print(f"L'étudiant {nom.strip()} a été supprimé du fichier {self.fichier}.")
        else:
            print(f"L'étudiant {nom.strip()} n'existe pas dans le fichier.")

    def AfficherEtudiant(self):
        with open(self.fichier, "r") as file:
            lignes = file.readlines()
        if lignes:
            print("Voici la liste des étudiants :")
            for ligne in lignes:
                print(ligne.strip())
        else:
            print("La liste des étudiants est vide.")

    def Recherche(self, nom):
        with open(self.fichier, "r") as file:
            lignes = file.readlines()
        nom = nom.strip() + "\n"
        if nom in lignes:
            print(f"L'étudiant {nom.strip()} est dans la liste.")
        else:
            print(f"L'étudiant {nom.strip()} n'existe pas dans le fichier.")

    def triAlphabetique(self):
        with open(self.fichier, "r") as file:
            lignes = file.readlines()
        lignes.sort()
        with open(self.fichier, "w") as file:
            file.writelines(lignes)
        print("La liste des étudiants a été triée par ordre alphabétique.")

    def modification(self, ancien_nom, nouveau_nom):
        with open(self.fichier, "r") as file:
            lignes = file.readlines()

        ancien_nom = ancien_nom.strip() + "\n"
        nouveau_nom = nouveau_nom.strip() + "\n"
        with open(self.fichier, "w") as file:
            for ligne in lignes:
                if ligne == ancien_nom:
                    file.write(nouveau_nom)
                    print(f"Le nom de l'étudiant a été modifié de {ancien_nom.strip()} à {nouveau_nom.strip()}.")
                else:
                    file.write(ligne)


def afficher_menu():
    fichier = "etudiants.txt"
    eleve = Etudiant(fichier)

    while True:
        print("\n-------- MENU --------")
        print("1. Ajouter un étudiant")
        print("2. Supprimer un étudiant")
        print("3. Afficher la liste des étudiants")
        print("4. Rechercher un étudiant")
        print("5. Trier la liste alphabétiquement")
        print("6. Modifier un étudiant")
        print("7. Quitter")

        choix = input("Entrez votre choix : ").strip()

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
