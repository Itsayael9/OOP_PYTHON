import random
import sys
import os
import os
import time
import calendar
import urllib.request
import re
import profile
import math
print("exemple avec random : genere unn nombre aleatoire entre 1 et 10 ")
random_number= random.randint(1,10)
print("nombre aleatoire genere ",random_number)


print("/n exemple avec math : calculer les cosinus d'un angle (en radiant )")
angle= math.pi/4
cos_value= math.cos(angle)
print("cosinus de 45 degre :", cos_value)


print("\n exemple avec sys : afficher la version de python  ")
print("version de python : ", sys.version )


print("\n exemple avec os : aficher le repertoire courante ")
current_directory=os.getcwd
print("repertoire actuelle ", current_directory)


print("\n exemple avec time : afficher l'heure actuelle ")
current_time = time.strftime("%H:%M:%S",time.localtime())
print("heure actuelle :",current_time)


#exemple avec calendar
print("\n exemple avec calendar : afficher le calendrier de l'annee actuelle ")
calendar_month= calendar.month(2024,12)
print(calendar_month)


#exemple avec urllib

print("\n exemple avec urllib : afficher le contenu d'une page web ")
url = 'https://www.example.com'
reponse = urllib.request.urlopen(url)
html_content = reponse.read()
print("centonue de la page :", html_content[:200])


#exemple avec re 
print(" \n exemple avec re : rechercher un mot dans chaine de text  ")
text = "voici un exemple de text avec  le mot python "
pattern = re.compile(r'python')
matches = pattern.findall(text)
print("mots trouver :", matches)


# exemple avec le medeule profile
print("n\ exemple avec profile : mesure le temps d exeqution d une fct ")
def slow_function():
    time.sleep(2)

profile.run('slow_function()')

