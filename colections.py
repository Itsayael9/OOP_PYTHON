from collections import namedtuple ,Counter ,deque , ChainMap
  
Point = namedtuple('Point',['x','y'])
p = Point(10,20)
print(p.x,p.y)
p2 = Point(30,50)
print(p2.x,p2.y)

data = ['a','b','b','c','a','a','b']
counter = Counter(data)
print(counter)

de = deque([1,2,3])
de.append(4)
de.appendleft(0)

print(de)

de.pop()
de.popleft()
print(de)

d1= {'prenom':6 ,'age':20}
d2 = {'x':5,'y':6}
cm = ChainMap(d1,d2)
print(cm['prenom'])
print(cm['age'])
print(cm['y'])
