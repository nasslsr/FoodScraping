import requests

url = "https://recipe-by-api-ninjas.p.rapidapi.com/v1/recipe"

querystring = {"query":""}

headers = {
	"X-RapidAPI-Key": "c2eea8a81fmsha2cba9d9c3840f2p195d04jsn76a0cf0025dd",
	"X-RapidAPI-Host": "recipe-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())