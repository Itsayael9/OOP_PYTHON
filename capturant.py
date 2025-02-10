import re

pattern = re.compile(r"(\d\d) (\w+) (\d{4})")
given_string = pattern.search("Tanger le 08 janvier 2025")
print("La date :")
print("corresp_date.group():", given_string.group())
print("corresp_date.group(1):", given_string.group(1))
print("corresp_date.group(2):", given_string.group(2))
print("corresp_date.group(3):", given_string.group(3))
print("corresp_date.groups():", given_string.groups()) #en ajoute la date dans un  touple  entres les 'semi bracets '

motif_IP = re.compile(
    r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."   # 0 => 255
    r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."  # 0 => 255
    r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\."  # 0 => 255
    r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"  # 0 = >255
)

# Utilisation du bloc try-except
try:
    # Recherche d'une adresse IP
    corresp_IP = motif_IP.search("234567890")  # L'adresse IP doit etre valide, c'est-à-dire ne pas dépasser 255 par exemple

    if corresp_IP:
        print("L'adresse IP : ")
        print("corresp_IP.group():", corresp_IP.group())          
        print("corresp_IP.group(1):", corresp_IP.group(1))        
        print("corresp_IP.group(2):", corresp_IP.group(2))       
        print("corresp_IP.group(3):", corresp_IP.group(3))      
        print("corresp_IP.group(4):", corresp_IP.group(4))       
        print("corresp_IP.groups():", corresp_IP.groups())  
    else:
        raise ValueError("Aucune adresse IP valide trouvée.")
    
except Exception as e: 
    print("Erreur lors de l'extraction de l'adresse IP :", e)
