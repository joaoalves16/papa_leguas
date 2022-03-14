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
import os


number = sys.argv[1]
fotos = pd.read_csv("./arquivos/Fotos.csv", header=None, sep=",", dtype=str)
# dados = pd.read_csv("./arquivos/dados.csv", header=None, sep=",", dtype=str)
dados = pd.read_csv(
    "./arquivos/dados" + number + ".csv", header=None, sep=",", dtype=str
)

chrome_options = Options()
if os.getenv('APPDATA') == None:
    print('OSX')
    chrome_options.add_argument("--user-data-dir=chrome-data")
else:
    print('Win')
    chrome_options.add_argument("--user-data-dir=" + os.getenv('APPDATA') + "\chrome-data")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-setuid-sandbox")

s = Service()
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
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
driver.find_element_by_xpath(
    "/html/body/div/div[2]/div/div/div[1]/div[2]/ul/li/a"
).click()
print("wait login_sso")
WebDriverWait(driver, 200).until(
    ec.visibility_of_element_located(
        (
            By.XPATH,
            "/html/body/div[1]/main/article/div/div[3]/div/form/div[1]/div/div/div/div/div/input",
        )
    )
)


def run_cadastro(dados, driver):
    try:
        print(":: start CADASTRO ::")
        Cadastro.cadastrar(dados, driver)
    except Exception as e:
        logging.error(traceback.format_exc())
        driver.save_screenshot(
            "./erros/" + datetime.today().strftime("%Y-%m-%d %H:%M" + ".png")
        )
        driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
        run_cadastro(dados, driver)


# IMÓVEL
run_cadastro(dados, driver)

# FOTO
# print("start foto");
# try:
#     driver.get("https://user.quintoandar.com.br/admin/menu")
#     Foto.cadastrarFotos(dados, fotos, driver)
# except:
#     driver.save_screenshot("./erros/foto-"+datetime.today().strftime("%Y-%m-%d %H:%M"+'.png'))
