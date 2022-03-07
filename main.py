from Cadastro import Cadastro
from Foto import Foto
from Autentificao import Autentificao
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import pandas as pd
import time

fotos = pd.read_csv("./arquivos/Fotos.csv", header=None, sep=",", dtype=str)
dados = pd.read_csv("./arquivos/dados_test2.csv", header=None, sep=",", dtype=str)
s = Service("/usr/local/bin/chromedriver")
# options = webdriver.ChromeOptions()
# options.add_argument("headless")
# options.add_argument(
#    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/85.0.4183.102 Safari/537.36"
# )
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-gpu")
driver = webdriver.Chrome(service=s)
driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
Autentificao.autentificar(driver)
print("ok")
WebDriverWait(driver, 200).until(
    ec.visibility_of_element_located(
        (
            By.XPATH,
            "//html/body/div[1]/main/article/div/div[3]/div/form/div[1]/div/div/div/div/input",
        )
    )
)
# Cadastro.cadastrar(dados, driver)
driver.get("https://user.quintoandar.com.br/admin/menu")
Foto.cadastrarFotos(dados, fotos, driver)
