from Cadastro import Cadastro
from Foto import Foto
from Autentificao import Autentificao
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
dados = pd.read_csv(
    "./arquivos/dados" + number + ".csv", header=None, sep=",", dtype=str
)


def start_driver():
    chrome_options = Options()
    # if os.getenv('APPDATA') == None:
    #    print('OSX')
    #    chrome_options.add_argument("--user-data-dir=chrome-data")
    # else:
    #    print('Win')
    #    chrome_options.add_argument("--user-data-dir=" + os.getenv('APPDATA') + "\chrome-data")
    if sys.argv[-1] != "-h":
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
    Autentificao.autentificar(driver)
    driver.get("https://crm.quintoandar.com.br")
    WebDriverWait(driver, 60).until(
        ec.visibility_of_element_located(
            (
                By.XPATH,
                "/html/body/qa-tasks/paper-header-panel/paper-toolbar/div[1]/qa-header/div[1]/qa-search/input",
            )
        )
    )
    # try:
    #     WebDriverWait(driver, 60).until(
    #         ec.visibility_of_element_located(
    #             (
    #                 By.XPATH,
    #                 "/html/body/div/div[2]/div/div/div[1]/div[2]/ul/li/a",
    #             )
    #         )
    #     )
    # except TimeoutException:
    #     driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")

    # espera primeiro botao login
    # print("wait login_sso")
    # WebDriverWait(driver, 60).until(
    #    ec.visibility_of_element_located((By.ID, "zocial-google",))
    # )
    #
    ## clica primeiro botao login
    # print("click login_sso")
    # driver.find_element(By.ID, "zocial-google").click()
    #
    ## espera botão login google
    # print("wait google_button")
    # WebDriverWait(driver, 60).until(
    #    ec.visibility_of_element_located(
    #        (By.XPATH, '//div[@class="loginBtn loginGoogle"]',)
    #    )
    # )
    ##
    ## # clicar botão login google pra abrir no CRM
    # print("click google_sso_button")
    # driver.find_element(By.XPATH, '//div[@class="loginBtn loginGoogle"]').click()
    #
    ## esperar CRM abrir
    # print("wait crm_page_open")
    # WebDriverWait(driver, 60).until(
    #    ec.visibility_of_element_located((By.ID, "mainPanel",))
    # )

    return driver


# FOTOS
def run_foto(dados, fotos, driver):
    try:
        print(":: start FOTO ::")
        Foto.cadastrarFotos(dados, fotos, driver)
    except Exception as e:
        print("DEU ERRO:")
        print(e)
        logging.error(traceback.format_exc())
        driver.save_screenshot(
            "./erros/foto-" + datetime.today().strftime("%Y-%m-%d %H:%M" + ".png")
        )
        driver.quit()
        run_foto(dados, fotos, start_driver())


run_foto(dados, fotos, start_driver())
