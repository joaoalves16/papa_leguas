from Cadastro import Cadastro
from Foto import Foto
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pandas as pd
import logging
import time
import traceback
import sys


number = sys.argv[1]
fotos = pd.read_csv("./arquivos/Fotos.csv", header=None, sep=",", dtype=str)
dados = pd.read_csv(
    "./arquivos/dados" + number + ".csv", header=None, sep=",", dtype=str
)

def start_driver():
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=chrome-data")
    if sys.argv[-1] != '-h':
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-setuid-sandbox")

    s = Service()
    driver = webdriver.Chrome(service=s, options=chrome_options)
    # driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
    driver.get("https://crm.quintoandar.com.br")

    # AUTENTICACAO
    print(":: start AUTENTICACAO ::")
    try:
        WebDriverWait(driver, 60).until(
            ec.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div/div[2]/div/div/div[1]/div[2]/ul/li/a",
                )
            )
        )
    except TimeoutException:
        driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
    print("click login_sso")
    driver.find_element(By.XPATH,
        "/html/body/div/div[2]/div/div/div[1]/div[2]/ul/li/a"
    ).click()
    print("wait login_sso")

    # espera botão login google
    WebDriverWait(driver, 60).until(
        ec.visibility_of_element_located(
            (
                By.XPATH,
                '//div[@class="loginBtn loginGoogle"]',
            )
        )
    )

    # clicar botão login google pra abrir no CRM
    driver.find_element(By.XPATH,
        '//div[@class="loginBtn loginGoogle"]'
    ).click()

    # esperar CRM abrir
    WebDriverWait(driver, 60).until(
        ec.visibility_of_element_located(
            (
                By.ID,
                'mainPanel',
            )
        )
    )

    return driver

# FOTOS
def run_foto(dados, fotos, driver):
    try:
        print(":: start FOTO ::")
        Foto.cadastrarFotos(dados, fotos, driver)
    except Exception as e:
        print('DEU ERRO:')
        print(e)
        logging.error(traceback.format_exc())
        driver.save_screenshot(
            "./erros/foto-" + datetime.today().strftime("%Y-%m-%d %H:%M" + ".png")
        )
        driver.quit()
        run_foto(dados, fotos, start_driver())

run_foto(dados, fotos, start_driver())
