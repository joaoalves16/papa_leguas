from Cadastro import Cadastro
from Foto import Foto
from outros.Autentificao import Autentificao
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pandas as pd
import time

fotos = pd.read_csv("./arquivos/Fotos.csv", header=None, sep=",", dtype=str)
dados = pd.read_csv("./arquivos/Dados.csv", header=None, sep=",", dtype=str)

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")

s = Service()
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
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
driver.find_element_by_xpath(
    "/html/body/div/div[2]/div/div/div[1]/div[2]/ul/li/a"
).click()
WebDriverWait(driver, 200).until(
    ec.visibility_of_element_located(
        (
            By.XPATH,
            "//html/body/div[1]/main/article/div/div[3]/div/form/div[1]/div/div/div/div/input",
        )
    )
)
Cadastro.cadastrar(dados, driver)
driver.get("https://user.quintoandar.com.br/admin/menu")
Foto.cadastrarFotos(dados, fotos, driver)
