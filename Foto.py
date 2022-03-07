from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import urllib.request
import os
import pyautogui
import sys

pyautogui.FAILSAFE = False


class Foto:
    def cadastrarFotos(dados, fotos, driver):
        links = []
        for index, row in dados.iterrows():
            cont = 1
            if str(dados[45][index]) != "ok" and str(dados[42][index]) != "1":
                id_imovel_imob = dados[1][index]
                id_imovel = dados[42][index]
                check_file = "./imag/" + id_imovel
                if os.path.isdir(check_file) != True:
                    links = fotos.loc[fotos[0] == id_imovel_imob][1]
                    pasta = "./imag/" + id_imovel + "/"
                    os.mkdir(pasta)
                    for link in links:
                        save_name = pasta + "/" + str(cont) + ".jpg"
                        urllib.request.urlretrieve(link, save_name)
                        cont += 1
                try:
                    WebDriverWait(driver, 200).until(
                        ec.visibility_of_element_located(
                            (
                                By.XPATH,
                                "/html/body/div[10]/div/div[2]/div[2]/form/div[2]/ul/li[1]/input",
                            )
                        )
                    )
                    driver.find_element_by_xpath(
                        "/html/body/div[10]/div/div[2]/div[2]/form/div[2]/ul/li[1]/input"
                    ).send_keys(id_imovel)
                    driver.find_element_by_xpath(
                        "/html/body/div[10]/div/div[2]/div[2]/form/div[1]/input"
                    ).click()
                    try:
                        WebDriverWait(driver, 200).until(
                            ec.visibility_of_element_located(
                                (
                                    By.XPATH,
                                    "/html/body/div[10]/div/div[11]/ul/li/div[2]/div/div[1]/div/div[1]/a[2]/span/i",
                                )
                            )
                        )
                        driver.find_element_by_xpath(
                            "/html/body/div[10]/div/div[11]/ul/li/div[2]/div/div[1]/div/div[1]/a[2]/span/i"
                        ).click()
                        driver.switch_to.window(driver.window_handles[1])
                        WebDriverWait(driver, 200).until(
                            ec.visibility_of_element_located(
                                (
                                    By.XPATH,
                                    "/html/body/div[9]/div/div/form/div[2]/div[7]/div[6]/div[2]/div/label",
                                )
                            )
                        )
                        driver.find_element_by_xpath(
                            "/html/body/div[9]/div/div/form/div[2]/div[7]/div[6]/div[5]/div/label/div"
                        ).click()
                        caminho = (
                            os.path.dirname(os.path.realpath(__file__))
                            + "/imag/"
                            + id_imovel
                            + "/1.jpg"
                        )
                        print(caminho)
                        pyautogui.write(caminho)
                        time.sleep(1)
                        pyautogui.press("enter")
                        time.sleep(2)
                        pyautogui.hotkey("command", "a")
                        pyautogui.press("enter")
                        try:
                            WebDriverWait(driver, 3).until(ec.alert_is_present())
                            alert = driver.switch_to.alert
                            alert.accept()
                        except TimeoutException:
                            print("no alert")
                        try:
                            WebDriverWait(driver, 10).until(
                                ec.visibility_of_element_located(
                                    (By.XPATH, "/html/body/div[15]")
                                )
                            )
                            while True:
                                try:
                                    WebDriverWait(driver, 3).until(
                                        ec.visibility_of_element_located(
                                            (By.XPATH, "/html/body/div[15]")
                                        )
                                    )
                                except TimeoutException:
                                    break
                            dados[45][index] = "ok"
                            dados.to_csv(
                                "./arquivos/dados_test2.csv",
                                header=None,
                                sep=",",
                                index=False,
                            )
                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])
                            driver.get("https://user.quintoandar.com.br/admin/menu")
                        except TimeoutException:
                            pyautogui.press("esc")
                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])
                            driver.get("https://user.quintoandar.com.br/admin/menu")
                    except TimeoutException:
                        driver.get("https://user.quintoandar.com.br/admin/menu")
                except TimeoutException:
                    driver.get("https://user.quintoandar.com.br/admin/menu")
