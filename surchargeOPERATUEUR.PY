#multiplication
class Point :
    def __init__(self,x,y):
        self.x= x
        self.y = y
    def __mul__(self,point):
        #multiplication 
        return Point(self.x * point.x,self.y * point.y)
    def __str__(self):
        return f"POINT ({self.x},{self.y})"  #print le format de point (x,y)

p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1 * p2 #utiliser la surcharge de l'operateur 
print(p3)  
    

#addition 
  

class Point :
    def __init__(self,x,y):
        self.x= x
        self.y = y
    def __add__(self,point):
        #addition 
        return Point(self.x + point.x,self.y + point.y)
    def __str__(self):
        return f"POINT ({self.x},{self.y})"

p1 = Point(1,2)
p2 = Point(3,4)
p3 = p1 + p2 #utiliser la surcharge de l'operateur 
print(p3)        
