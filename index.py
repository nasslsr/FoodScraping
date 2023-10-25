from flask import Flask, render_template, request
import requests
import re



app = Flask(__name__)


def get_recipe(name):

	url = "https://recipe-by-api-ninjas.p.rapidapi.com/v1/recipe"

	querystring = {"query": f"{name}"}

	headers = {
		"X-RapidAPI-Key": "c2eea8a81fmsha2cba9d9c3840f2p195d04jsn76a0cf0025dd",
		"X-RapidAPI-Host": "recipe-by-api-ninjas.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	print(response.json()[0]['ingredients'])
	print(response.json()[0]['ingredients'])

	pattern = r"[0-9]|oz|tb|lg|ts|/"

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

	return recipes



@app.route('/')
def index():
    return render_template('interface.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    print("Name submitted:", name)
    recipes = get_recipe(name)
    return render_template('interface.html', recipes=recipes)

if __name__ == '__main__':
    app.run(port=5009)