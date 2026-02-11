import pickle
import time
import os
import random  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def enviar_mensagens():

    atraso_inicial = random.randint(60, 600)
    print(f"Aguardando {atraso_inicial} segundos para iniciar a sessão...")
    time.sleep(atraso_inicial)

    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://www.linkedin.com")

        if not os.path.exists("cookies.pkl"):
            print("Arquivo cookies.pkl não encontrado!")
            return

        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        
        driver.refresh()
        time.sleep(random.randint(5, 10))

        driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
        time.sleep(random.randint(5, 8))

        botoes_mensagem = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Enviar mensagem')]")

        contagem = 0
        for botao in botoes_mensagem[:15]:
            try:
                botao.click()
                time.sleep(random.randint(3, 6)) 

                caixa_texto = driver.switch_to.active_element
                texto = "Olá! Tudo bem? Sou Desenvolvedor Full-Stack e vi que temos interesses em comum. Vamos trocar ideias!"

                caixa_texto.send_keys(texto)
                time.sleep(random.randint(2, 4))
                caixa_texto.send_keys(Keys.ENTER) 

                print(f"Mensagem {contagem + 1} enviada.")

                try:
                    fechar = driver.find_element(By.XPATH, "//button[contains(@data-control-name, 'close_aside')]")
                    fechar.click()
                except:
                    pass
                
                contagem += 1
                time.sleep(random.randint(30, 90)) 

            except Exception as e:
                print(f"Erro ao enviar para uma conexão: {e}")
                continue

    finally:
        print(f"Processo finalizado. Total de mensagens: {contagem}")
        driver.quit()

if __name__ == "__main__":
    enviar_mensagens()