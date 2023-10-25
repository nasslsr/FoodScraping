from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://cemantix.certitudes.org')

cookies = driver.find_element(By.XPATH,'//*[@id="dialog-close"]')
cookies.click()
driver.implicitly_wait(5)

input_word = driver.find_element(By.ID,'cemantix-guess')
input_word.click()
driver.implicitly_wait(5)
input_word.send_keys('chien')
driver.implicitly_wait(5)
search_button = driver.find_element(By.ID,'cemantix-guess-btn')
search_button.click()
driver.implicitly_wait(5)



td_element = driver.find_element(By.CSS_SELECTOR, 'td.number[style="color: rgb(128,200,255)"]')

# Afficher le contenu de la balise <td>
print("Contenu de la balise <td> :", td_element.text)

