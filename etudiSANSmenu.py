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

# Exemple d'utilisation
etudiants = Etudiant()
etudiants.AjouterEtudiant("Alice")
etudiants.AjouterEtudiant("Bob")
etudiants.AjouterEtudiant("Charlie")
etudiants.AfficherEtudiant()
etudiants.Recherche("Bob")
etudiants.triAlphabetique()
etudiants.AfficherEtudiant()
etudiants.modification("Alice", "Alicia")
etudiants.AfficherEtudiant()
etudiants.SupprimeEtudiant("Charlie")
etudiants.AfficherEtudiant()
