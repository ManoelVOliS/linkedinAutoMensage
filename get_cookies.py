import pickle
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")

print("Faça o login manualmente no navegador e aguarde a página inicial carregar.")

time.sleep(60)

pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
print("Arquivo cookies.pkl gerado com sucesso!")
driver.quit()