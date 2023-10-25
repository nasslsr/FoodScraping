import requests
import re
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



url = "https://recipe-by-api-ninjas.p.rapidapi.com/v1/recipe"

querystring = {"query": "pizza"}

headers = {
	"X-RapidAPI-Key": "c2eea8a81fmsha2cba9d9c3840f2p195d04jsn76a0cf0025dd",
	"X-RapidAPI-Host": "recipe-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

title = []
ingredients = []
instructions = []

for i in range(0, 3):
	print(i)
	title.append(response.json()[i]['title'])
	ingredients.append(response.json()[i]['ingredients'])
	instructions.append(response.json()[i]['instructions'])


	recipes = list(zip(title, ingredients, instructions))

print('voici les tires', title)
print('voici les ingrédients', ingredients)
print('voici les instructions', instructions)
print(recipes[0])

import re

def extract_ingredient_names(ingredients):
    # Utilisation d'une expression régulière pour extraire les noms d'ingrédients
    pattern = r"[0-9]|oz|tb|lg|ts|/"
    ingredient_names = [re.sub(pattern, '', ingredient).strip() for ingredient in ingredients.split('|')]
    return ingredient_names

ingredients = '4 oz Prunes|4 oz Dried apricots|1/2 c Toasted split almonds|3 tb Extra virgin olive oil|8 Portions chicken|1 ts Salt|20 Grinds black pepper|1 lg Onion|2 Cloves garlic|1 ts Ground turmeric|3 Cardamom pods|1 ts Ground ginger|2 ts Ground cinnamon|2 1/2 c Chicken stock (or half stock, half white wine)|1 tb Honey|2 ts Cornstarch|2 ts Lemon juice or water'

ingredient_names = extract_ingredient_names(ingredients)

print(ingredient_names)


def scrap_walmart():

	driver = webdriver.Firefox()
	driver.get('https://www.carrefour.fr/')

	wait = WebDriverWait(driver, 10)
	cookie = wait.until(
		EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Continuer sans accepter')]")))
	cookie.click()

	input_search = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Pain, lait, oeufs...')]")
	input_search.send_keys('chicken')

	search_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Rechercher parmi le contenu du site')]")
	search_button.click()

	product_card = driver.find_element(By.XPATH, "//li[@style='order: 5;']")






scrap_walmart()

