from Autentificao import Autentificao
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

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
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
driver.find_element(By.XPATH,
    "/html/body/div/div[2]/div/div/div[1]/div[2]/ul/li/a"
).click()

Autentificao.autentificar(driver)

print("wait login_sso")
WebDriverWait(driver, 200).until(
    ec.visibility_of_element_located(
        (
            By.XPATH,
            "//html/body/div[1]/main/article/div/div[3]/div/form/div[1]/div/div/div/div/input",
        )
    )
)