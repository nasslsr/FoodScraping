from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

driver = webdriver.Firefox()
driver2 = webdriver.Firefox()

 # Question 1

driver.get('https://sutom.nocle.fr/#')


 # Question 2

cookies = driver.find_element(By.XPATH,'//*[@id="panel-fenetre-bouton-fermeture"]')
cookies.click()

 # Question 3
first_letter_case = driver.find_element(By.XPATH,'/html/body/div/div[3]/table/tr[1]/td[1]')
first_letter = first_letter_case.text

table = driver.find_element(By.CSS_SELECTOR,'div#grille table')
premiere_ligne = table.find_element(By.TAG_NAME,'tr')
taille_mot = len(premiere_ligne.find_elements(By.TAG_NAME,'td'))


print(f"taille du mot : {taille_mot} et sa première lettre : {first_letter}")

first_letter_minuscule = first_letter.lower()
print(first_letter_minuscule)

# Question 4
driver2.get(f'https://www.listesdemots.net/d/{first_letter_minuscule}/1/mots{taille_mot}lettresdebutant{first_letter_minuscule}.htm')
driver2.implicitly_wait(20)



# Question 5

liste_mots =driver2.find_element(By.CLASS_NAME, "mt").text
liste_mots=liste_mots.split()
print(liste_mots)

# Question 6

random_mot = random.choice(liste_mots)
print("Mot au hasard :", random_mot)
lettres = list(random_mot)
for lettre in lettres:
    driver.find_element(By.CSS_SELECTOR, f'div.input-lettre[data-lettre="{lettre}"]').click()
driver.find_element(By.CSS_SELECTOR, f'div.input-lettre[data-lettre="_entree"]').click()


# Question 7

tr = driver.find_element(By.TAG_NAME, "tr")


tds = driver.find_elements(By.TAG_NAME, "td")

liste = []
for td in tds:
    className = td.get_attribute("class")
    liste.append(className)

info = [x for x in liste if x != '']

print(info)
print(lettres)

resultat=[]
for i,j in zip(lettres,info):
    resultat.append((i,j))
print(resultat)





"""

return first_letter

def liste_mots(first_letter):

    cookies = driver.find_element(By.CSS_SELECTOR,'.sc-17rhrsc-2')
    cookies.click()

    taille = driver.find_element(By.XPATH,'//a[@class="ln" and @href="mots7lettres.htm"]')
    taille.click()




"""