class Magasin:
    def __init__(self):
        self.produits = []
    
    def ajouter_produit(self, produit):
        if produit not in self.produits:
            self.produits.append(produit)
            print(f"Le produit '{produit}' a été ajouté.")
        else:
            print(f"Le produit '{produit}' existe déjà.")
    
    def supprimer_produit(self, produit):
        if produit in self.produits:
            self.produits.remove(produit)
            print(f"Le produit '{produit}' a été supprimé.")
        else:
            print(f"Le produit '{produit}' n'existe pas dans le magasin.")
    
    def afficher_produits(self):
        if self.produits:
            print("\nListe des produits:")
            for produit in self.produits:
                print(f"- {produit}")
        else:
            print("\nLe magasin n'a aucun produit.")
    
    def rechercher_produit(self, produit):
        existe = produit in self.produits
        print(f"Le produit '{produit}' {'existe' if existe else 'n''existe pas'} dans le magasin.")
        return existe
    
    def trier_produits(self):
        self.produits.sort()
        print("Les produits ont été triés par ordre alphabétique.")
        self.afficher_produits()
    
    def modifier_produit(self, ancien_produit, nouveau_produit):
        if ancien_produit in self.produits:
            index = self.produits.index(ancien_produit)
            self.produits[index] = nouveau_produit
            print(f"Le produit '{ancien_produit}' a été remplacé par '{nouveau_produit}'.")
        else:
            print(f"Le produit '{ancien_produit}' n'existe pas dans le magasin.")
    
    def compter_produits(self):
        nombre = len(self.produits)
        print(f"Il y a {nombre} produit(s) dans le magasin.")
        return nombre
    
    def vider_liste(self):
        self.produits.clear()
        print("Tous les produits ont été supprimés.")

# Programme principal
magasin = Magasin()

# Input pour ajouter des produits
nb = int(input("Combien de produits voulez-vous ajouter ? "))
for i in range(nb):
    nom_produit = input(f"Entrez le nom du produit {i+1}: ")
    magasin.ajouter_produit(nom_produit)

# Input pour afficher
magasin.afficher_produits()

# Input pour rechercher
nom_recherche = input("Quel produit voulez-vous rechercher ? ")
magasin.rechercher_produit(nom_recherche)

# Input pour modifier
ancien = input("Quel produit voulez-vous modifier ? ")
nouveau = input("Nouveau nom du produit : ")
magasin.modifier_produit(ancien, nouveau)

# Trier la liste
magasin.trier_produits()

# Input pour supprimer
a_supprimer = input("Quel produit voulez-vous supprimer ? ")
magasin.supprimer_produit(a_supprimer)

# Compter les produits
magasin.compter_produits()

# Input pour vider la liste
choix = input("Voulez-vous vider la liste ? (oui/non) : ")
if choix.lower() == "oui":
    magasin.vider_liste()

# Afficher l'état final
magasin.afficher_produits()