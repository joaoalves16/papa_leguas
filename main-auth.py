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
import os

chrome_options = Options()

# if os.getenv("APPDATA") == None:
#    print("OSX")
#    chrome_options.add_argument("--user-data-dir=chrome-data")
# else:
#    print("Win")
#    chrome_options.add_argument(
#        "--user-data-dir=" + os.getenv("APPDATA") + "\chrome-data"
#    )
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-setuid-sandbox")

s = Service()
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("")

# AUTENTICACAO
print(":: start AUTENTICACAO ::")
try:
    WebDriverWait(driver, 60).until(
        ec.visibility_of_element_located(
            (By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/ul/li/a",)
        )
    )
except TimeoutException:
    driver.get("")
print("click login_sso")

Autentificao.autentificar(driver)

WebDriverWait(driver, 60).until(
    ec.visibility_of_element_located(
        (By.XPATH, '//div[@class="loginBtn loginGoogle"]',)
    )
)
print("click google_sso_button")
driver.find_element(By.XPATH, '//div[@class="loginBtn loginGoogle"]').click()
print("wait login_sso")
WebDriverWait(driver, 200).until(
    ec.visibility_of_element_located(
        (
            By.XPATH,
            "//html/body/div[1]/main/article/div/div[3]/div/form/div[1]/div/div/div/div/input",
        )
    )
)
