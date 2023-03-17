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
import socket
import sys

socket.setdefaulttimeout(15)
pyautogui.FAILSAFE = False


def auto_down(url, filename):
    try:
        urllib.request.urlretrieve(url, filename)
        time.sleep(20)
    except:
        print("Network conditions is not good.Reloading.")
        auto_down(url, filename)


def salvar_erro(dados, number, index, nome, desc):
    print("error " + desc)
    dados[45][index] = "erro-" + nome
    dados.to_csv(
        "./arquivos/dados" + number + ".csv", header=None, sep=",", index=False,
    )


def salvar_sucesso(dados, number, index):
    dados[45][index] = "ok-img (" + datetime.today().strftime("%Y-%m-%d %H:%M:%S") + ")"
    dados.to_csv(
        "./arquivos/dados" + number + ".csv", header=None, sep=",", index=False,
    )


class Foto:
    def cadastrarFotos(dados, fotos, driver):
        number = sys.argv[1]
        links = []
        for index, row in dados.iterrows():
            if (
                pd.isna(dados[45][index])
                and str(dados[42][index]) != "1"
                and str(dados[42][index]) != "E"
            ):
                id_imovel_imob = dados[1][index]
                id_imovel = dados[42][index]

                if pd.isna(id_imovel) or id_imovel == "0":
                    # salvar_erro(dados,number,index,"id_imovel_nan", "id_imovel invalido")
                    continue

                check_file = "./imag/" + id_imovel

                # entrar no link
                print(
                    "start imagem imob (" + id_imovel_imob + ") 5A (" + id_imovel + ")"
                )

                # tenta entrar 2x na pag, se n conseguir o script para
                try:
                    print('enter url "fotografo/uploadFoto"')
                    driver.get(
                        ""
                        + id_imovel
                    )
                except:
                    try:
                        time.sleep(3)
                        print('retry url "fotografo/uploadFoto"')
                        driver.get(
                            ""
                            + id_imovel
                        )
                    except:
                        print('abort url "fotografo/uploadFoto"')
                        salvar_erro(dados, number, index, "abort_404", "abort_404")
                        continue

                # iniciar download fotos
                print("start download_photos")
                pasta = "./imag/" + id_imovel + "/"
                if os.path.isdir(check_file) != True:
                    os.mkdir(pasta)

                cont = 1
                down = 0
                has_images = False
                total_images = len(os.listdir(pasta))
                for link in fotos.loc[fotos[0] == id_imovel_imob][1]:
                    filename_atual = pasta + "/" + str(cont) + ".jpg"
                    if os.path.isfile(filename_atual) == False:
                        if has_images == False:
                            print("download photo")
                        has_images = True
                        print(str(cont))
                        save_name = pasta + "/" + str(cont) + ".jpg"
                        auto_down(link, save_name)
                        down += 1
                    cont += 1

                # print info de imagens
                print(
                    "\ntotal:"
                    + str(cont - 1)
                    + ", "
                    + str(down)
                    + " down, "
                    + str(total_images)
                    + " exists"
                )
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
                    driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight)"
                    )
                    time.sleep(1)
                    # print('wait')
                    WebDriverWait(driver, 200).until(
                        ec.visibility_of_element_located(
                            (By.XPATH, "//div[@class='content-pad blkEnviar']",)
                        )
                    )
                    time.sleep(1)
                    driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight)"
                    )

                    caminho_atual = (
                        os.path.dirname(os.path.realpath(__file__))
                        + "/imag/"
                        + id_imovel
                    )

                    # verifica se a pasta realmente tem imagens
                    if len(os.listdir(caminho_atual)) == 0:
                        salvar_erro(
                            dados, number, index, "sem_imgs", "sem_fotos_encontradas"
                        )
                        continue

                    # verifica se o imovel já tem imagens cadastradas
                    img_elements = driver.find_elements_by_xpath(
                        "//div[@class='foto-container']"
                    )
                    if len(img_elements) > 0:
                        # scroll para o final da tela e aguarda
                        try:
                            driver.execute_script(
                                "window.scrollTo(0, document.body.scrollHeight)"
                            )
                            driver.find_element(By.ID, "excluirTodasFotos").click()
                            WebDriverWait(driver, 10).until(
                                ec.visibility_of_element_located(
                                    (
                                        By.XPATH,
                                        '//button[@class="swal-button swal-button--confirm"]',
                                    )
                                )
                            )
                            driver.find_element(
                                By.XPATH,
                                '//button[@class="swal-button swal-button--confirm"]',
                            ).click()
                            time.sleep(1)
                            WebDriverWait(driver, 10).until(
                                ec.visibility_of_element_located(
                                    (
                                        By.XPATH,
                                        '//button[@class="swal-button swal-button--confirm"]',
                                    )
                                )
                            )
                            driver.find_element(
                                By.XPATH,
                                '//button[@class="swal-button swal-button--confirm"]',
                            ).click()
                        except:
                            salvar_erro(
                                dados, number, index, "ja_tem_imgs", "ja_tem_fotos"
                            )
                            continue

                    # enviando primeira foto (capa)
                    driver.find_element_by_id("input-fotos").send_keys(
                        caminho_atual + "/1.jpg"
                    )

                    # time.sleep(300)
                    # aguarda loading ficar invisível
                    WebDriverWait(driver, 30).until(
                        ec.invisibility_of_element_located(
                            (By.XPATH, "/html/body/div[15]")
                        )
                    )

                    # scroll para o final da tela e aguarda
                    driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight)"
                    )
                    time.sleep(3)

                    error_img = driver.find_elements_by_xpath(
                        "//div[@class='mensagem-erro-campo imagem tamanhoInvalido']"
                    )
                    if len(error_img) > 0:
                        salvar_erro(dados, number, index, "img_pequena", "img_pequena")
                        continue

                    # espera a miniatura da imagem aparecer e aguarda
                    WebDriverWait(driver, 10).until(
                        ec.visibility_of_element_located(
                            (By.XPATH, "//div[@class='img-view-container ']")
                        )
                    )
                    time.sleep(1)

                    # hover na miniatura para aparecer opcoes
                    hoverboy = driver.find_element(
                        By.XPATH, "//div[@class='img-view-container ']"
                    )
                    hov = ActionChains(driver).move_to_element(hoverboy)
                    hov.perform()
                    time.sleep(2)

                    # clica no link para definir capa para abrir aba
                    WebDriverWait(driver, 10).until(
                        ec.visibility_of_element_located(
                            (By.XPATH, '//a[@data-original-title="Definir como capa"]')
                        )
                    )
                    driver.find_element(
                        By.XPATH, '//a[@data-original-title="Definir como capa"]'
                    ).click()

                    # clica no button dentro da aba para salvar capa
                    WebDriverWait(driver, 10).until(
                        ec.visibility_of_element_located(
                            (By.XPATH, "//button[contains(text(), 'Salvar Capa')]")
                        )
                    )
                    time.sleep(4)
                    driver.find_element(
                        By.XPATH, "//button[contains(text(), 'Salvar Capa')]"
                    ).click()

                    #
                    # time.sleep(10000)
                    imagens_restantes = os.listdir(caminho_atual)[0:-1]
                    print(imagens_restantes)
                    for imagens in imagens_restantes:
                        print(caminho_atual + "/" + imagens)
                        driver.find_element_by_id("input-fotos").send_keys(
                            caminho_atual + "/" + imagens
                        )
                        WebDriverWait(driver, 120).until(
                            ec.invisibility_of_element_located(
                                (By.ID, "uploadProgressBar")
                            )
                        )
                    # NOVA PAG PUBLICAR

                    # tenta entrar 2x na pag publicacao, se n conseguir o script para
                    try:
                        driver.get(
                            ""
                            + id_imovel
                            + "/fotos"
                        )
                    except:
                        driver.get(
                            ""
                            + id_imovel
                            + "/fotos"
                        )

                    WebDriverWait(driver, 60).until(
                        ec.visibility_of_element_located((By.ID, "btnPublicar"))
                    )
                    driver.find_element_by_id("btnPublicar",).click()

                    WebDriverWait(driver, 60).until(
                        ec.visibility_of_element_located(
                            (By.ID, "popUpCallBackPublicar")
                        )
                    )

                    # FIM NOVA PAG PUBLICAR

                    # print("aguardando botao salvar")
                    # time.sleep(2)
                    # driver.execute_script(
                    #    "window.scrollTo(0, document.body.scrollHeight)"
                    # )
                    # time.sleep(2)
                    # WebDriverWait(driver, 200).until(
                    #    ec.visibility_of_element_located(
                    #        (By.XPATH, '//*[@id="salvar_publicar"]',)
                    #    )
                    # )
                    # print("chegou?")
                    # time.sleep(2)
                    # driver.execute_script(
                    #    "window.scrollTo(0, document.body.scrollHeight)"
                    # )
                    # time.sleep(2)
                    # driver.find_element(By.XPATH, '//*[@id="salvar_publicar"]',).click()
                    print(
                        "finish imagem imob ("
                        + id_imovel_imob
                        + ") 5A ("
                        + id_imovel
                        + ")"
                    )
                    try:
                        WebDriverWait(driver, 10).until(
                            ec.visibility_of_element_located(
                                (By.XPATH, '//div[@class="errosAdmin"]',)
                            )
                        )
                        dados[45][index] = (
                            "error-" + driver.find_element_by_class("errosAdmin").text
                        )
                        dados.to_csv(
                            "./arquivos/dados" + number + ".csv",
                            header=None,
                            sep=",",
                            index=False,
                        )
                    except TimeoutException:
                        driver.find_elements_by_class_name("foto-container")
                    salvar_sucesso(dados, number, index)
                except TimeoutException:
                    salvar_erro(dados, number, index, "pag_fotos", "pag_fotos")
        print("-- Finalizado --")
        print("-- Happy Ending :) --")

