import requests
import re
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




list = ['2 tb Butter or oil|2 Big onions; peeled and sliced|2 Big cloves garlic; peeled and crushed|1 kg To 1.25kg chuck or bladebone steak|2 tb Plain flour|1 tb Dry mustard|1 sm Can; (370ml) beer|2 tb Brown vinegar|1 Heaped teaspoon brown sugar|1/2 ts Salt|Bouquet garni; (parsley, thyme and bay leaf tied to a piece of celery with white cotton or string)|Chopped fresh parsley', '1/4 lb To 1/2 lb bacon or pancetta|1 c Milk|2 tb Vinegar|2 Eggs or 1-4 oz. carton egg substitute|1/4 c Grated parmesan', '1 lb Bacon; chopped in 1" pieces|8 tb Sweet butter|1 Medium onion; chopped|1 c Light cream (half-n-half)|1 Egg; lightly beaten|1 c Parmesan cheese; grated|1/2 c Italian parsley; chopped|1 lb Spaghetti or linguine|3/4 c Chicken broth; heated|Pepper; freshly ground']
list = ','.join(list)
pattern = r"[0-9]|oz|tb|lg|ts|/|kg|To|or|and|ml|sm|lb|-|c "
ingredient_names_dirty = [re.sub(pattern, '', ingredient).strip() for ingredient in list.split('|')]

ingredients_names=[]
for element in ingredient_names_dirty:
	clean_element = element.split(';')[0]
	ingredients_names.append((clean_element))


print(ingredients_names)