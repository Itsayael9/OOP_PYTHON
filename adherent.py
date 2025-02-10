class adherent : 
#constructeur avec des attribut prive 
    def __init__ (self,nom,age,prenom):
        
        self.__nom= nom 
        self.__age= age 
        self.__prenom = prenom 
    def to_string (self):
        print("le nom est ",self.__nom)
        print("ton age est ",self.__age)
        print("tonn prenom est ",self.__prenom)
   
   #method pour savoire si est majeur ou bien non 
    def majeur (self):
        if self.__age > 18:
            return True 
        else: 
            return False
#getter de nom     
    def getNom(self):
        return self.__nom
#setter de nom (modification de nom )
    def setNom(self,nvNom):
        self.__nom = nvNom
#getter de age 
    def getAge(self):
        return self.__age
#setter de nom 
    def setAge(self,nvAge):
        self.__age=nvAge 
#instantiation 
A1 = adherent("aya",19 , "el ouahabi  ")
#affichage 
A1.to_string()
#appel de fct majeur 
print(A1.majeur)
#get and set le nom
print(A1.getNom())
print(A1.setNom("sara"))

#get and set age 
print(A1.getAge())
print(A1.setAge("77"))
A1.to_string()


    








