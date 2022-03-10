from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time
import urllib.request
import os
import pandas as pd
import pyautogui
import sys

pyautogui.FAILSAFE = False

def auto_down(url,filename):
    try:
        urllib.request.urlretrieve(url, filename)
    except:
        print('Network conditions is not good.Reloading.')
        auto_down(url,filename)

class Foto:
    def cadastrarFotos(dados, fotos, driver):
        number = sys.argv[1]
        links = []
        for index, row in dados.iterrows():
            cont = 1
            if pd.isna(dados[45][index]) and str(dados[42][index]) != "1" and str(dados[42][index]) != "E":
                id_imovel_imob = dados[1][index]
                id_imovel = dados[42][index]
                check_file = "./imag/" + id_imovel
                print(
                    "start imagem imob ("
                    + id_imovel_imob
                    + ") 5A ("
                    + id_imovel
                    + ")"
                )
                print("start download_photos")
                pasta = "./imag/" + id_imovel + "/"
                if os.path.isdir(check_file) != True:
                    os.mkdir(pasta)

                for link in fotos.loc[fotos[0] == id_imovel_imob][1]:
                    filename_atual = pasta + "/" + str(cont) + ".jpg"
                    if os.path.isfile(filename_atual) == False:
                        print("start photo"+str(cont))
                        save_name = pasta + "/" + str(cont) + ".jpg"
                        auto_down(link, save_name)
                    cont += 1
                # else:
                #     print("error sem_fotos_encontradas")
                #     dados[45][index] = "erro-sem_imgs"
                #     dados.to_csv(
                #         "./arquivos/dados" + number + ".csv",
                #         header=None,
                #         sep=",",
                #         index=False,
                #     )
                #     continue
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
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                        caminho_atual = (
                            os.path.dirname(os.path.realpath(__file__))
                            + "/imag/"
                            + id_imovel
                        )

                        if len(os.listdir(caminho_atual)) == 0:
                            print("error sem_fotos_encontradas")
                            dados[45][index] = "erro-sem_imgs"
                            dados.to_csv(
                                "./arquivos/dados" + number + ".csv",
                                header=None,
                                sep=",",
                                index=False,
                            )
                            continue

                        driver.find_element_by_id("input-fotos").send_keys(
                            caminho_atual + "/1.jpg"
                        )
                        WebDriverWait(driver, 10).until(
                            ec.invisibility_of_element_located(
                                (By.XPATH, "/html/body/div[15]")
                            )
                        )

                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                        time.sleep(4)
                        hoverboy = driver.find_element_by_xpath(
                            "/html/body/div[8]/div/div/form/div[2]/div[7]/div[6]/div[5]/div/div/div[1]"
                        )
                        hov = ActionChains(driver).move_to_element(hoverboy)
                        hov.perform()
                        time.sleep(2)


                        WebDriverWait(driver, 10).until(
                            ec.visibility_of_element_located(
                                (By.XPATH, '//a[@data-original-title="Definir como capa"]')
                            )
                        )

                        driver.find_element_by_xpath('//a[@data-original-title="Definir como capa"]').click()

                        WebDriverWait(driver, 10).until(
                            ec.visibility_of_element_located(
                                (By.XPATH, "//button[contains(text(), 'Salvar Capa')]")
                            )
                        )
                        time.sleep(4)
                        driver.find_element_by_xpath("//button[contains(text(), 'Salvar Capa')]").click()

                        # time.sleep(10000)
                        imagens_restantes = os.listdir(caminho_atual)[0:-1]
                        print(imagens_restantes)
                        for imagens in imagens_restantes:
                            print(caminho_atual + "/" + imagens)
                            driver.find_element_by_id("input-fotos").send_keys(
                                caminho_atual + "/" + imagens
                            )
                            WebDriverWait(driver, 60).until(
                                ec.invisibility_of_element_located(
                                    (By.XPATH, "/html/body/div[15]")
                                )
                            )
                        WebDriverWait(driver, 60).until(
                            ec.invisibility_of_element_located(
                                (By.XPATH, "/html/body/div[15]")
                            )
                        )

                        # driver.find_element_by_xpath('/html/body/div[9]/div/div/form/div[2]/div[5]/div/div[2]/div[1]/div[1]/label').click()

                        # NOVA PAG PUBLICAR
                        driver.get("https://user.quintoandar.com.br/imovel/editar/"+id_imovel+"/fotos")

                        WebDriverWait(driver, 60).until(
                            ec.visibility_of_element_located(
                                (By.ID, "btnPublicar")
                            )
                        )
                        driver.find_element_by_id(
                            'btnPublicar',
                        ).click()


                        WebDriverWait(driver, 60).until(
                            ec.visibility_of_element_located(
                                (By.ID, "popUpCallBackPublicar")
                            )
                        )

                        # FIM NOVA PAG PUBLICAR


                        # time.sleep(10000)
                        # print("aguardando botao salvar")
                        # time.sleep(2)
                        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                        # time.sleep(2)
                        # WebDriverWait(driver, 200).until(
                        #     ec.visibility_of_element_located(
                        #         (
                        #             By.XPATH,
                        #             '//*[@id="salvar_publicar"]',
                        #         )
                        #     )
                        # )

                        # time.sleep(2)
                        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                        # time.sleep(2)

                        # driver.find_element_by_xpath(
                        #     '//*[@id="salvar_publicar"]',
                        # ).click()

                        print(
                            "finish imagem imob ("
                            + id_imovel_imob
                            + ") 5A ("
                            + id_imovel
                            + ")"
                        )


                        # try:
                        #     WebDriverWait(driver, 10).until(
                        #         ec.visibility_of_element_located(
                        #             (
                        #                 By.XPATH,
                        #                 '//div[@class="errosAdmin"]',
                        #             )
                        #         )
                        #     )
                        #     dados[45][index] = "error-" + driver.find_element_by_class("errosAdmin").text
                        #     dados.to_csv(
                        #         "./arquivos/dados" + number + ".csv",
                        #         header=None,
                        #         sep=",",
                        #         index=False,
                        #     )
                        # except TimeoutException:

                        # driver.find_elements_by_class_name("foto-container")
                        #
                        # ec.visibility_of_element_located(
                        #     (
                        #         By.XPATH,
                        #         '//div[@class="errosAdmin"]',
                        #     )
                        # )

                        dados[45][index] = "ok-img ("+datetime.today().strftime("%Y-%m-%d %H:%M:%S")+")"
                        dados.to_csv(
                            "./arquivos/dados" + number + ".csv",
                            header=None,
                            sep=",",
                            index=False,
                        )
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        driver.get("https://user.quintoandar.com.br/admin/menu")
                    except TimeoutException:
                        driver.get("https://user.quintoandar.com.br/admin/menu")
                        dados[45][index] = "erro-pag_fotos"
                        dados.to_csv(
                            "./arquivos/dados" + number + ".csv",
                            header=None,
                            sep=",",
                            index=False,
                        )
                except TimeoutException:
                    driver.get("https://user.quintoandar.com.br/admin/menu")
                    dados[45][index] = "erro-pesq_id"
                    dados.to_csv(
                        "./arquivos/dados" + number + ".csv",
                        header=None,
                        sep=",",
                        index=False,
                    )
