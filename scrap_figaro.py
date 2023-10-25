from bs4 import BeautifulSoup as bs
import requests
import re

# EXO1

url = 'https://leconjugueur.lefigaro.fr/frlistedeverbe.php'
response = requests.get(url)

html = response.content

pattern = re.compile(r'/conjugaison/verbe/.*\.html$')

soup = bs(html, "html.parser")

verbes = soup.find_all("a",href=pattern)
liste_verbes  = [i.get_text() for i in verbes]

#print(liste_verbes)

#EXO 2

base_url = 'https://leconjugueur.lefigaro.fr/conjugaison/verbe/'

dic_verbes  = {i.get_text() : base_url + i.get_text() +'.html' for i in verbes}
#print(dic_verbes)

#EXO 3

dict = {}

for verbe in liste_verbes:
    lettre = verbe[0]
    print(lettre)
