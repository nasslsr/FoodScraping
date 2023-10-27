from flask import Flask, render_template, request
import requests
import re
import requests
import re
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




app = Flask(__name__)

selected_products = []

def get_recipe(name):

	url = "https://recipe-by-api-ninjas.p.rapidapi.com/v1/recipe"

	querystring = {"query": f"{name}"}

	headers = {
		"X-RapidAPI-Key": "c2eea8a81fmsha2cba9d9c3840f2p195d04jsn76a0cf0025dd",
		"X-RapidAPI-Host": "recipe-by-api-ninjas.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	title = []
	ingredients = []
	instructions = []
	for i in range(0, 3):
		title.append(response.json()[i]['title'])
		ingredients.append(response.json()[i]['ingredients'])
		instructions.append(response.json()[i]['instructions'])

	recipes = list(zip(title, ingredients, instructions))

	print('voici les tires', title)
	print('voici les ingrédients', ingredients)
	print('voici les instructions', instructions)
	print(recipes[0])

	return recipes

def extract_ingredient_names(recipes):
	ingredients = recipes[1]
	list = ','.join(ingredients)
	pattern = r"[0-9]|oz|tb|lg|ts|/|kg|To|or|and|ml|sm|lb|-|c "
	ingredient_names_dirty = [re.sub(pattern, '', ingredient).strip() for ingredient in list.split('|')]

	ingredients_names = []
	for element in ingredient_names_dirty:
		clean_element = element.split(';')[0]
		ingredients_names.append((clean_element))

	return ingredients_names

@app.route('/buy_products', methods=['POST'])
def buy_products():
    selected_ingredients = request.form.getlist('selected_ingredients')

    # Ici, vous devriez effectuer le scraping en fonction des produits sélectionnés
    for ingredient in selected_ingredients:
        driver = webdriver.Firefox()
        driver.get('https://www.carrefour.fr/')

        wait = WebDriverWait(driver, 10)
        cookie = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Continuer sans accepter')]")))
        cookie.click()

        input_search = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Pain, lait, oeufs...')]")
        input_search.send_keys(ingredient)

        search_button = driver.find_element(By.XPATH,
                                           "//button[contains(@aria-label, 'Rechercher parmi le contenu du site')]")
        search_button.click()

        product_card = driver.find_element(By.XPATH, "//li[@style='order: 5;']")

        product_info = product_card  # Assurez-vous que product_card contient les informations du produit
        if product_info:
            selected_products.append(product_info)

        driver.quit()  # Fermez le navigateur après avoir terminé le scraping

    return render_template('shopping_basket.html', selected_products=selected_products)



@app.route('/')
def index():
    return render_template('interface.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    print("Name submitted:", name)
    recipes = get_recipe(name)
    return render_template('interface.html', recipes=recipes)

@app.route('/recipe')
def display_products():
    name = request.args.get('name')
    recipes = get_recipe(name)
    ingredients_names = extract_ingredient_names(recipes)
    return render_template('recipe.html', ingredients_names=ingredients_names)






if __name__ == '__main__':
    app.run(port=5009)