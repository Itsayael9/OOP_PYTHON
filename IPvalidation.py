import re

# Les logs contenant des adresses IP
ip_adress = """
        192.168.1.1 
        10.0.0.5 
        999.999.999.999
        172.16.254.1 
        255.255.255.255 
        241.300.25.256
        0.0.0.0 
"""

# validation de ip adres 
ip_pattern = r"(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"

# find all the ip adress valid 
valid_ips = re.findall(ip_pattern, ip_adress )
print("tout les adress valider trouver sont  :")
for ip in valid_ips:
    print(f"- {ip}")

# Trouver la 1er adresse IP valide
first_ip = re.search(ip_pattern, ip_adress)
if first_ip:
    print(f"\n1er adress valider a etait trouver est  : {first_ip.group()}")
else:
    print("\naucune adress valider ") 

# # re.sub remplacement de  toutes les adresses IP valides par un texte masqué
Logs_masques = re.sub(ip_pattern, "[IP_masquee]", ip_adress)
print("\nLogs_masques :")
print(Logs_masques)

# Diviser les logs
entries = re.split(r"\n+",ip_adress.strip())
print("\nEntrées des logs :")
for entry in entries:
    print(f"- {entry}")
    
#match fct 
first_ip = re.match(ip_pattern, ip_adress.strip())  # Notice we strip the input text
if first_ip:
    print(f"\nPremière adresse IP valide trouvée : {first_ip.group()}")
else:
    print("\nAucune adresse IP valide trouvée au début de la chaîne.")