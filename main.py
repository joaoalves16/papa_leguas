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
dados = pd.read_csv("./arquivos/Dados.csv", header=None, sep=",", dtype=str)
s = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
Autentificao.autentificar(driver)
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
