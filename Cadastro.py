from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import pandas as pd
import time
import sys


def check_exists_by_xpath(xpath, webdriver):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


class Cadastro:
    def cadastrar(dados, driver):
        number = sys.argv[1]
        for index, row in dados.iterrows():
            if str(dados[42][index]) == "0":
                dados[42][index] = "E"
                dados.to_csv(
                    "./arquivos/dados" + number + ".csv",
                    header=None,
                    sep=",",
                    index=False,
                )
                id_imovel_imob = dados[1][index]
                nome_proprietario = dados[5][index]
                telefone_proprietario = dados[6][index]
                email_proprietario = dados[7][index]
                cep = dados[14][index]
                numero = dados[13][index]
                andar = dados[15][index]
                complemento = dados[16][index]
                tipo = dados[11][index]
                tipo = tipo.replace(" ", "")
                quartos = int(dados[17][index])
                suites = int(dados[18][index])
                banheiros = int(dados[19][index])
                metros = int(dados[20][index])
                portaria = dados[22][index]
                vagas = int(dados[23][index])
                descricao = dados[24][index]
                morador = dados[25][index]
                chave = dados[27][index]
                chave_obs = dados[29][index]
                obs_interna = dados[31][index]
                valor = dados[33][index]
                condominio = dados[34][index]
                iptu = dados[35][index]
                iptu_pagamento = dados[36][index]
                senha_obs = "null"
                senha = "null"
                data_saida = "null"
                try:
                    WebDriverWait(driver, 200).until(
                        ec.visibility_of_element_located(
                            (
                                By.XPATH,
                                "/html/body/div[1]/main/article/div/div[3]/div/form/div[1]/div/div/div/div/input",
                            )
                        )
                    )
                    print("start dados proprietario")
                    driver.find_element_by_xpath(
                        "/html/body/div[1]/main/article/div/div[3]/div/form/div[1]/div/div/div/div/input"
                    ).send_keys(nome_proprietario)
                    driver.find_element_by_xpath(
                        "/html/body/div[1]/main/article/div/div[3]/div/form/div[2]/div/div/div/div/input"
                    ).send_keys(str(telefone_proprietario))
                    driver.find_element_by_xpath(
                        "/html/body/div[1]/main/article/div/div[3]/div/form/div[4]/div/div/div/div/input"
                    ).send_keys(email_proprietario)
                    driver.find_element_by_xpath(
                        "/html/body/div[1]/main/article/div/div[3]/div/form/div[5]/div/div/div/button[1]"
                    ).click()
                    driver.find_element_by_xpath(
                        "/html/body/div[1]/main/footer/div/div[1]/button"
                    ).click()
                    try:
                        WebDriverWait(driver, 200).until(
                            ec.visibility_of_element_located(
                                (
                                    By.XPATH,
                                    "/html/body/div[1]/main/article/div/form/div/div[3]/button",
                                )
                            )
                        )
                        if check_exists_by_xpath(
                            "/html/body/div[1]/main/article/div/form/div/div[2]/div/div/div[2]",
                            driver,
                        ):
                            cont = 1
                            time.sleep(2)
                            caminho = (
                                "/html/body/div[1]/main/article/div/form/div/div[2]/div/div/div["
                                + str(cont)
                                + "]"
                            )
                            while check_exists_by_xpath(caminho, driver):
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/article/div/form/div/div[2]/div/div/div["
                                    + str(cont)
                                    + "]/button/span[1]/div/div[3]"
                                ).click()
                                driver.switch_to.window(driver.window_handles[1])
                                try:
                                    WebDriverWait(driver, 60).until(
                                        ec.visibility_of_element_located(
                                            (
                                                By.XPATH,
                                                "/html/body/div/div[1]/div[1]/div/div[1]/div[4]/a/span",
                                            )
                                        )
                                    )
                                    check_telefone = driver.find_element_by_xpath(
                                        "/html/body/div/div[1]/div[1]/div/div[1]/div[4]/a/span"
                                    ).text
                                    check_telefone = check_telefone.replace(" ", "")
                                    check_telefone = check_telefone.replace("-", "")
                                    check_telefone = check_telefone.replace("+55", "")
                                    if str(check_telefone) == str(
                                        telefone_proprietario
                                    ):
                                        driver.close()
                                        driver.switch_to.window(
                                            driver.window_handles[0]
                                        )
                                        time.sleep(2)
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/form/div/div[2]/div/div/div["
                                            + str(cont)
                                            + "]/button/span[1]/div/div[1]/label/span[1]"
                                        ).click()
                                        time.sleep(2)
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/footer/div/div[1]/button"
                                        ).click()
                                    else:
                                        cont += 1
                                        caminho = (
                                            "/html/body/div[1]/main/article/div/form/div/div[2]/div/div/div["
                                            + str(cont)
                                            + "]"
                                        )
                                        driver.close()
                                        driver.switch_to.window(
                                            driver.window_handles[0]
                                        )
                                except TimeoutException:
                                    cont += 1
                                    caminho = (
                                        "/html/body/div[1]/main/article/div/form/div/div[2]/div/div/div["
                                        + str(cont)
                                        + "]"
                                    )
                                    driver.close()
                                    driver.switch_to.window(driver.window_handles[0])
                        else:
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/main/article/div/form/div/div[2]/div/div/div[1]/button/span[1]/div/div[1]/label/span[1]"
                            ).click()
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/main/footer/div/div[1]/button"
                            ).click()
                        if tipo == "Casa" or tipo == "Casaemcondominio":
                            try:
                                WebDriverWait(driver, 60).until(
                                    ec.visibility_of_element_located(
                                        (
                                            By.XPATH,
                                            "/html/body/div[1]/main/article/div/div/div[2]/form/div[1]/div/div/button[3]",
                                        )
                                    )
                                )
                                print("start localizacao")
                                match tipo:
                                    case "Casa":
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div/div[2]/form/div[1]/div/div/button[3]"
                                        ).click()
                                    case "Casaemcondominio":
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div/div[2]/form/div[1]/div/div/button[4]"
                                        ).click()
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[1]/div[2]/label[2]/span[1]"
                                ).click()
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[2]/div/div/input"
                                ).send_keys(str(cep))
                                try:
                                    WebDriverWait(driver, 60).until(
                                        ec.visibility_of_element_located(
                                            (
                                                By.XPATH,
                                                "/html/body/div[1]/main/article/div/div/div[2]/form/div[3]/div/div[2]/div[1]/label/span[1]",
                                            )
                                        )
                                    )
                                except TimeoutException:
                                    dados[43][index] = "Mapa não encontrado"
                                    dados[42][index] = "1"
                                    dados.to_csv(
                                        "./arquivos/dados" + number + ".csv",
                                        header=None,
                                        sep=",",
                                        index=False,
                                    )
                                    continue
                                if check_exists_by_xpath(
                                    "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[3]/div/div/div/div[2]/span[1]",
                                    driver,
                                ):
                                    erro_cep = driver.find_element_by_xpath(
                                        "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[3]/div/div/div/div[2]/span[1]"
                                    ).text
                                    dados[43][index] = erro_cep
                                    dados[42][index] = "1"
                                    dados.to_csv(
                                        "./arquivos/dados" + number + ".csv",
                                        header=None,
                                        sep=",",
                                        index=False,
                                    )
                                    driver.get(
                                        "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                    )
                                    continue
                                elif check_exists_by_xpath(
                                    "/html/body/div[1]/main/article/div/div/div[2]/form/p[1]/span",
                                    driver,
                                ):
                                    erro_cep = driver.find_element_by_xpath(
                                        "/html/body/div[1]/main/article/div/div/div[2]/form/p[1]/span"
                                    ).text
                                    dados[43][index] = erro_cep
                                    dados[42][index] = "1"
                                    dados.to_csv(
                                        "./arquivos/dados" + number + ".csv",
                                        header=None,
                                        sep=",",
                                        index=False,
                                    )
                                    driver.get(
                                        "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                    )
                                    continue
                                else:
                                    try:
                                        WebDriverWait(driver, 60).until(
                                            ec.visibility_of_element_located(
                                                (
                                                    By.XPATH,
                                                    "/html/body/div[1]/main/article/div/div/div[2]/form/div[3]/div/div[2]/div[1]/label/span[1]",
                                                )
                                            )
                                        )
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[3]/div/div[3]/div/div/div/div/input"
                                        ).send_keys(str(numero))
                                        if str(complemento) != "nan":
                                            driver.find_element_by_xpath(
                                                "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[3]/div/div[4]/div/div/div/div/input"
                                            ).send_keys(complemento)
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div/div[2]/form/div[3]/div/div[2]/div[1]/label/span[1]"
                                        ).click()
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/footer/div/div[1]/button"
                                        ).click()
                                    except TimeoutException:
                                        dados[43][
                                            index
                                        ] = "Elemento não encontrado na pagina 'Localização'"
                                        dados[42][index] = "1"
                                        driver.get(
                                            "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                        )
                                        continue
                            except TimeoutException:
                                dados[43][
                                    index
                                ] = "Elemento não encontrado na pagina 'Localização'"
                                dados[42][index] = "1"
                                driver.get(
                                    "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                )
                                continue
                        elif tipo == "Apartamento" or tipo == "Kitnet":
                            try:
                                WebDriverWait(driver, 60).until(
                                    ec.visibility_of_element_located(
                                        (
                                            By.XPATH,
                                            "/html/body/div[1]/main/article/div/div/div[2]/form/div[1]/div/div/button[1]",
                                        )
                                    )
                                )
                                print("start localizacao")
                                match tipo:
                                    case "Apartamento":
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div/div[2]/form/div[1]/div/div/button[1]"
                                        ).click()
                                    case "Kitnet":
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div/div[2]/form/div[1]/div/div/button[2]"
                                        ).click()
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[1]/div[2]/label[2]/span[1]"
                                ).click()
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[2]/div/div/input"
                                ).send_keys(str(cep))
                                try:
                                    WebDriverWait(driver, 60).until(
                                        ec.visibility_of_element_located(
                                            (
                                                By.XPATH,
                                                "/html/body/div[1]/main/article/div/div/div[2]/form/div[3]/div/div[2]/div[1]/label/span[1]",
                                            )
                                        )
                                    )
                                except TimeoutException:
                                    dados[43][index] = "Mapa não encontrado"
                                    dados[42][index] = "1"
                                    dados.to_csv(
                                        "./arquivos/dados" + number + ".csv",
                                        header=None,
                                        sep=",",
                                        index=False,
                                    )
                                    continue
                                if check_exists_by_xpath(
                                    "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[3]/div/div/div/div[2]/span[1]",
                                    driver,
                                ):
                                    erro_cep = driver.find_element_by_xpath(
                                        "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[3]/div/div/div/div[2]/span[1]"
                                    ).text
                                    dados[43][index] = erro_cep
                                    dados[42][index] = "1"
                                    dados.to_csv(
                                        "./arquivos/dados" + number + ".csv",
                                        header=None,
                                        sep=",",
                                        index=False,
                                    )
                                    driver.get(
                                        "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                    )
                                    continue
                                elif check_exists_by_xpath(
                                    "/html/body/div[1]/main/article/div/div/div[2]/form/p/span",
                                    driver,
                                ):
                                    erro_cep = driver.find_element_by_xpath(
                                        "/html/body/div[1]/main/article/div/div/div[2]/form/p/span"
                                    ).text
                                    dados[43][index] = erro_cep
                                    dados[42][index] = "1"
                                    dados.to_csv(
                                        "./arquivos/dados" + number + ".csv",
                                        header=None,
                                        sep=",",
                                        index=False,
                                    )
                                    driver.get(
                                        "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                    )
                                    continue
                                elif check_exists_by_xpath(
                                    "/html/body/div[1]/main/article/div/div/div[2]/form/p[2]/span",
                                    driver,
                                ):
                                    erro_cep = driver.find_element_by_xpath(
                                        "/html/body/div[1]/main/article/div/div/div[2]/form/p[2]/span"
                                    ).text
                                    dados[38][index] = erro_cep
                                    dados[42][index] = "1"
                                    dados.to_csv(
                                        "./arquivos/dados" + number + ".csv",
                                        header=None,
                                        sep=",",
                                        index=False,
                                    )
                                    driver.get(
                                        "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                    )
                                    continue
                                else:
                                    try:
                                        WebDriverWait(driver, 60).until(
                                            ec.visibility_of_element_located(
                                                (
                                                    By.XPATH,
                                                    "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[3]/div/div[5]/div/div/div/div/input",
                                                )
                                            )
                                        )
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[3]/div/div[3]/div/div/div/div/input"
                                        ).send_keys(str(numero))
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[3]/div/div[4]/div/div/div/div/input"
                                        ).send_keys(str(andar))
                                        if str(complemento) != "nan":
                                            driver.find_element_by_xpath(
                                                "/html/body/div[1]/main/article/div/div/div[2]/form/div[2]/div[3]/div/div[5]/div/div/div/div/input"
                                            ).send_keys(complemento)
                                        try:
                                            WebDriverWait(driver, 60).until(
                                                ec.visibility_of_element_located(
                                                    (
                                                        By.XPATH,
                                                        "/html/body/div[1]/main/article/div/div/div[2]/form/div[3]/div/div[2]/div[1]/label/span[1]",
                                                    )
                                                )
                                            )
                                            driver.find_element_by_xpath(
                                                "/html/body/div[1]/main/article/div/div/div[2]/form/div[3]/div/div[2]/div[1]/label/span[1]"
                                            ).click()
                                            driver.find_element_by_xpath(
                                                "/html/body/div[1]/main/footer/div/div[1]/button"
                                            ).click()
                                        except TimeoutException:
                                            dados[43][
                                                index
                                            ] = "Elemento não encontrado na pagina 'Localização'"
                                            dados[42][index] = "1"
                                            driver.get(
                                                "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                            )
                                            continue
                                    except TimeoutException:
                                        dados[43][
                                            index
                                        ] = "Elemento não encontrado na pagina 'Localização'"
                                        dados[42][index] = "1"
                                        driver.get(
                                            "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                        )
                                        continue
                            except TimeoutException:
                                dados[43][
                                    index
                                ] = "Elemento não encontrado na pagina 'Localização'"
                                dados[42][index] = "1"
                                driver.get(
                                    "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                )
                                continue
                        try:
                            # time.sleep(5000000)
                            # driver.find_element_by_xpath('/html/body/div[1]/main/article').scroll(0,0)
                            driver.execute_script(
                                "document.getElementsByClassName('fXELdk')[0].scroll(0,0)"
                            )
                            WebDriverWait(driver, 60).until(
                                ec.visibility_of_element_located(
                                    (
                                        By.XPATH,
                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[1]/div/div/div/div/button[2]",
                                    )
                                )
                            )
                            # print("dorme")
                            # time.sleep(5000000)
                            # driver.save_screenshot('error.png')

                            print("start detalhes do imovel")
                            for x in range(0, quartos):
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[1]/div/div/div/div/button[2]"
                                ).click()
                            for x in range(0, banheiros):
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[3]/div/div/div/div/button[2]"
                                ).click()
                            for x in range(0, suites):
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[2]/div/div/div/div/button[2]"
                                ).click()
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/main/article/div/div[2]/div/form/div[4]/div/div/div/div/input"
                            ).send_keys(str(metros))
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/main/article/div/div[2]/div/form/div[5]/div/div/button[1]"
                            ).click()
                            for x in range(0, vagas):
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[7]/div/div/div/div/button[2]"
                                ).click()
                            if pd.isna(descricao) == False:
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[8]/div/div/div/textarea[1]"
                                ).send_keys(descricao)
                            if portaria == "Não":
                                time.sleep(2)
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[1]/div/div/button[4]"
                                ).click()
                                match morador:
                                    case "DESOCUPADO":
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[2]/div/div/button[3]"
                                        ).click()
                                        match chave:
                                            case str("Chave Comum"):
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[1]"
                                                ).click()
                                                time.sleep(2)
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button"
                                                ).click()
                                            case "Senha":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[2]"
                                                ).click()
                                                if senha_obs == "Sim":
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[1]"
                                                    ).click()
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/div/div/input"
                                                    ).send_keys(senha)
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                    ).click()
                                                else:
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[2]"
                                                    ).click()
                                            case "Biometria":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[3]"
                                                ).click()
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                ).click()
                                    case "PROPRIETÁRIO":
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[2]/div/div/button[2]"
                                        ).click()
                                        match chave:
                                            case "Chave Comum":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[1]"
                                                ).click()
                                                time.sleep(2)
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button"
                                                ).click()
                                            case "Senha":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[2]"
                                                ).click()
                                                if senha_obs == "Sim":
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[1]"
                                                    ).click()
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/div/div/input"
                                                    ).send_keys(senha)
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                    ).click()
                                                else:
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[2]"
                                                    ).click()
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                    ).click()
                                            case "Biometria":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[3]"
                                                ).click()
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                ).click()
                                    case "INQUILINO":
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[2]/div/div/button[1]"
                                        ).click()
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/div/div/input"
                                        ).send_keys(data_saida)
                                        match chave:
                                            case "Chave Comum":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[1]"
                                                ).click()
                                                time.sleep(2)
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                ).click()
                                            case "Senha":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[2]"
                                                ).click()
                                                if senha_obs == "Sim":
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[1]"
                                                    ).click()
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/div/div/input"
                                                    ).send_keys(senha)
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                    ).click()
                                                else:
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[2]"
                                                    ).click()
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                    ).click()
                                            case "Biometria":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[3]"
                                                ).click()
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                ).click()
                            else:
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[1]/div/div/button[1]    "
                                ).click()
                                match morador:
                                    case "DESOCUPADO":
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[2]/div/div/button[3]"
                                        ).click()
                                        match chave:
                                            case "Chave Comum":
                                                time.sleep(2)
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[1]"
                                                ).click()
                                                time.sleep(2)
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[1]"
                                                ).click()
                                            case "Senha":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[2]"
                                                ).click()
                                                if senha_obs == "Sim":
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[1]"
                                                    ).click()
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/div/div/input"
                                                    ).send_keys(senha)
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                    ).click()
                                                else:
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[2]"
                                                    ).click()
                                            case "Biometria":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[3]"
                                                ).click()
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                ).click()
                                    case "PROPRIETÁRIO":
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[2]/div/div/button[2]"
                                        ).click()
                                        match chave:
                                            case "Chave Comum":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[1]"
                                                ).click()
                                                time.sleep(2)
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button"
                                                ).click()
                                            case "Senha":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[2]"
                                                ).click()
                                                if senha_obs == "Sim":
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[1]"
                                                    ).click()
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/div/div/input"
                                                    ).send_keys(senha)
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                    ).click()
                                                else:
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[2]"
                                                    ).click()
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                    ).click()
                                            case "Biometria":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[3]"
                                                ).click()
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                ).click()
                                    case "INQUILINO":
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[2]/div/div/button[1]"
                                        ).click()
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/div/div/input"
                                        ).send_keys(data_saida)
                                        match chave:
                                            case "Chave Comum":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[1]"
                                                ).click()
                                                time.sleep(2)
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                ).click()
                                            case "Senha":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[2]"
                                                ).click()
                                                if senha_obs == "Sim":
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[1]"
                                                    ).click()
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/div/div/input"
                                                    ).send_keys(senha)
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                    ).click()
                                                else:
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[4]/div/div/button[2]"
                                                    ).click()
                                                    driver.find_element_by_xpath(
                                                        "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                    ).click()
                                            case "Biometria":
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[3]/div/div/button[3]"
                                                ).click()
                                                driver.find_element_by_xpath(
                                                    "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button"
                                                ).click()
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/main/article/div/div[2]/div/form/div[9]/div[5]/div/div/button[1]"
                            ).click()
                            driver.find_element_by_xpath(
                                "//textarea[@name='additionalInfo']"
                            ).send_keys(chave_obs)
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/main/article/div/div[2]/div/form/div[10]/div/div/div/textarea[1]"
                            ).send_keys("3P\n" + obs_interna)
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/main/footer/div/div[1]/button"
                            ).click()
                        except TimeoutException:
                            dados[43][
                                index
                            ] = "Elemento não encontrado na pagina 'Detalhe do imovel'"
                            dados[42][index] = "1"
                            dados.to_csv(
                                "./arquivos/dados" + number + ".csv",
                                header=None,
                                sep=",",
                                index=False,
                            )
                            driver.get(
                                "https://owner-conversion.quintoandar.com.br/register/new/owner"
                            )
                            continue
                        try:
                            WebDriverWait(driver, 60).until(
                                ec.visibility_of_element_located(
                                    (
                                        By.XPATH,
                                        "/html/body/div[1]/main/article/div/form/div[1]/label[2]/span[1]",
                                    )
                                )
                            )
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/main/article/div/form/div[1]/label[2]/span[1]"
                            ).click()
                            time.sleep(2)
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/main/article/div/form/div[2]/div/div/div"
                            ).click()
                            driver.find_element_by_xpath(
                                "/html/body/div[3]/div[3]/ul/li[2]"
                            ).click()
                            time.sleep(2)
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/main/footer/div/div[1]/button"
                            ).click()
                        except TimeoutException:
                            dados[43][
                                index
                            ] = "Elemento não encontrado na pagina 'Aluguel'"
                            dados[42][index] = "1"
                            dados.to_csv(
                                "./arquivos/dados" + number + ".csv",
                                header=None,
                                sep=",",
                                index=False,
                            )
                            driver.get(
                                "https://owner-conversion.quintoandar.com.br/register/new/owner"
                            )
                            continue
                        try:
                            print("start venda")
                            # driver.execute_script("document.getElementsByClassName('fXELdk')[0].scroll(0,0)")
                            WebDriverWait(driver, 60).until(
                                ec.visibility_of_element_located(
                                    (
                                        By.XPATH,
                                        "/html/body/div[1]/main/article/div/form/div/label[1]/span[1]",
                                    )
                                )
                            )
                            driver.find_element_by_xpath(
                                "/html/body/div[1]/main/article/div/form/div/label[1]/span[1]"
                            ).click()
                            time.sleep(2)
                            driver.find_element_by_xpath(
                                '//*[@id="sale"]/div[3]/div[1]/div/div/div/div/div/div[2]/input'
                            ).send_keys(str(valor))
                            if condominio != 0:
                                driver.find_element_by_xpath(
                                    '//*[@id="sale"]/div[3]/div[2]/div/div/div/div/div/div[2]/input'
                                ).send_keys(str(condominio))
                            match iptu_pagamento:
                                case "Anualmente":
                                    driver.find_element_by_xpath(
                                        "/html/body/div[1]/main/article/div/form/div[4]/div[2]/button[2]"
                                    ).click()
                                    if iptu != 0:
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/form/div[5]/div/div/div[2]/div/div[2]/input"
                                        ).send_keys(str(iptu))
                                case "Não pago":
                                    driver.find_element_by_xpath(
                                        "/html/body/div[1]/main/article/div/form/div[4]/div[2]/button[1]"
                                    ).click()
                                case "Mensalmente":
                                    driver.find_element_by_xpath(
                                        "/html/body/div[1]/main/article/div/form/div[4]/div[2]/button[3]"
                                    ).click()
                                    driver.find_element_by_xpath(
                                        "/html/body/div[1]/main/article/div/form/div[5]/div[1]/div/div/div"
                                    ).click()
                                    driver.find_element_by_xpath(
                                        "/html/body/div[3]/div[3]/ul/li[12]"
                                    ).click()
                                    if iptu != 0:
                                        driver.find_element_by_xpath(
                                            "/html/body/div[1]/main/article/div/form/div[5]/div[2]/div/div[2]/div/div[2]/input"
                                        ).send_keys(str(iptu))
                            try:
                                WebDriverWait(driver, 10).until(
                                    ec.element_to_be_clickable(
                                        (
                                            By.XPATH,
                                            "/html/body/div[1]/main/footer/div/div/button",
                                        )
                                    )
                                )
                                # driver.get(
                                #     "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                # )
                                # continue
                                driver.find_element_by_xpath(
                                    "/html/body/div[1]/main/footer/div/div/button"
                                ).click()

                                print("finish imovel " + str(id_imovel_imob))
                            except TimeoutException:
                                dados[43][index] = "Erro de dados"
                                dados[42][index] = "1"
                                dados.to_csv(
                                    "./arquivos/dados" + number + ".csv",
                                    header=None,
                                    sep=",",
                                    index=False,
                                )
                                driver.get(
                                    "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                )
                                continue
                        except TimeoutException:
                            dados[43][
                                index
                            ] = "Elemento não encontrado na pagina 'Venda'"
                            dados[42][index] = "1"
                            dados.to_csv(
                                "./arquivos/dados" + number + ".csv",
                                header=None,
                                sep=",",
                                index=False,
                            )
                            driver.get(
                                "https://owner-conversion.quintoandar.com.br/register/new/owner"
                            )
                            continue
                        try:
                            WebDriverWait(driver, 60).until(
                                ec.visibility_of_element_located(
                                    (
                                        By.XPATH,
                                        "/html/body/div[1]/main/article/div/form/div/div[2]/div/label/span/span",
                                    )
                                )
                            )
                            id_imovel = driver.find_element_by_xpath(
                                "/html/body/div[1]/main/article/div/div/h1/span"
                            ).text
                            id_imovel = id_imovel.replace(
                                "Sessão de fotos do imóvel ", ""
                            )
                            print(id_imovel)
                            dados[42][index] = id_imovel
                            dados[44][index] = datetime.today().strftime(
                                "%Y-%m-%d %H:%M"
                            )
                            dados.to_csv(
                                "./arquivos/dados" + number + ".csv",
                                header=None,
                                sep=",",
                                index=False,
                            )
                            driver.get("https://crm.quintoandar.com.br/tarefas/")
                            try:
                                WebDriverWait(driver, 60).until(
                                    ec.visibility_of_element_located(
                                        (
                                            By.XPATH,
                                            "/html/body/qa-tasks/paper-header-panel/paper-toolbar/div[1]/qa-header/div[1]/qa-search/input",
                                        )
                                    )
                                )
                                driver.find_element_by_xpath(
                                    "/html/body/qa-tasks/paper-header-panel/paper-toolbar/div[1]/qa-header/div[1]/qa-search/input"
                                ).send_keys(id_imovel)
                                try:
                                    WebDriverWait(driver, 60).until(
                                        ec.visibility_of_element_located(
                                            (
                                                By.XPATH,
                                                "/html/body/qa-tasks/paper-header-panel/paper-toolbar/div[1]/qa-header/div[1]/qa-search/iron-dropdown/div/qa-loading/div/div[4]/div/qa-search-item/div/qa-search-task-item",
                                            )
                                        )
                                    )
                                except TimeoutException:
                                    dados[43][index] = "Tarefa não encontrada"
                                    dados.to_csv(
                                        "./arquivos/dados" + number + ".csv",
                                        header=None,
                                        sep=",",
                                        index=False,
                                    )
                                    driver.get(
                                        "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                    )
                                    continue
                                driver.find_element_by_xpath(
                                    "/html/body/qa-tasks/paper-header-panel/paper-toolbar/div[1]/qa-header/div[1]/qa-search/iron-dropdown/div/qa-loading/div/div[4]/div/qa-search-item/div/qa-search-task-item"
                                ).click()
                                WebDriverWait(driver, 5).until(
                                    ec.number_of_windows_to_be(2)
                                )
                                driver.switch_to.window(driver.window_handles[1])
                                try:
                                    WebDriverWait(driver, 60).until(
                                        ec.visibility_of_element_located(
                                            (
                                                By.XPATH,
                                                "/html/body/qa-tasks/paper-header-panel/div/div[1]/paper-drawer-panel/iron-selector/div[1]/div[1]/qa-task-details/paper-drawer-panel/iron-selector/div[1]/div[1]/div/div[2]/qa-link[3]/paper-button",
                                            )
                                        )
                                    )
                                    driver.find_element_by_xpath(
                                        "/html/body/qa-tasks/paper-header-panel/div/div[1]/paper-drawer-panel/iron-selector/div[1]/div[1]/qa-task-details/paper-drawer-panel/iron-selector/div[1]/div[1]/div/div[2]/qa-link[3]/paper-button"
                                    ).click()
                                    try:
                                        WebDriverWait(driver, 60).until(
                                            ec.visibility_of_element_located(
                                                (
                                                    By.XPATH,
                                                    "/html/body/qa-tasks/paper-header-panel/div/div[1]/paper-drawer-panel/iron-selector/div[1]/div[1]/qa-task-details/paper-drawer-panel/iron-selector/div[1]/div[1]/div/div[2]/qa-link[3]/dialog-comentar/form/paper-textarea/paper-input-container/div[1]/div/iron-autogrow-textarea/div[2]/textarea",
                                                )
                                            )
                                        )
                                    except TimeoutException:
                                        dados[43][
                                            index
                                        ] = "Caixa de comentario não encontrada"
                                        dados[42][index] = "1"
                                        dados.to_csv(
                                            "./arquivos/dados" + number + ".csv",
                                            header=None,
                                            sep=",",
                                            index=False,
                                        )
                                        driver.get(
                                            "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                        )
                                        continue
                                    driver.find_element_by_xpath(
                                        "/html/body/qa-tasks/paper-header-panel/div/div[1]/paper-drawer-panel/iron-selector/div[1]/div[1]/qa-task-details/paper-drawer-panel/iron-selector/div[1]/div[1]/div/div[2]/qa-link[3]/dialog-comentar/form/paper-textarea/paper-input-container/div[1]/div/iron-autogrow-textarea/div[2]/textarea"
                                    ).send_keys("For Brokers - 3P Supply")
                                    driver.find_element_by_xpath(
                                        "/html/body/qa-tasks/paper-header-panel/div/div[1]/paper-drawer-panel/iron-selector/div[1]/div[1]/qa-task-details/paper-drawer-panel/iron-selector/div[1]/div[1]/div/div[2]/qa-link[3]/dialog-comentar/div/paper-button[2]"
                                    ).click()
                                    driver.close()
                                    driver.switch_to.window(driver.window_handles[0])
                                    driver.get(
                                        "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                    )
                                except TimeoutException:
                                    dados[43][
                                        index
                                    ] = "Botão de cancelamento de tarefa não encontrado"
                                    dados.to_csv(
                                        "./arquivos/dados" + number + ".csv",
                                        header=None,
                                        sep=",",
                                        index=False,
                                    )
                                    driver.get(
                                        "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                    )
                                    continue
                            except TimeoutException:
                                dados[43][index] = "Barra de pesquisa não encontrada"
                                dados.to_csv(
                                    "./arquivos/dados" + number + ".csv",
                                    header=None,
                                    sep=",",
                                    index=False,
                                )
                                driver.get(
                                    "https://owner-conversion.quintoandar.com.br/register/new/owner"
                                )
                                continue
                        except TimeoutException:
                            dados[43][index] = "Erro na confirmação"
                            dados[42][index] = "1"
                            dados.to_csv(
                                "./arquivos/dados" + number + ".csv",
                                header=None,
                                sep=",",
                                index=False,
                            )
                            driver.get(
                                "https://owner-conversion.quintoandar.com.br/register/new/owner"
                            )
                            continue
                    except TimeoutException:
                        dados[43][index] = "Erro cadastro proprietário"
                        dados[42][index] = "1"
                        dados.to_csv(
                            "./arquivos/dados" + number + ".csv",
                            header=None,
                            sep=",",
                            index=False,
                        )
                        driver.get(
                            "https://owner-conversion.quintoandar.com.br/register/new/owner"
                        )
                except TimeoutException:
                    dados[43][index] = "Pagina de proprietario não carregou"
                    dados[42][index] = "1"
                    dados.to_csv(
                        "./arquivos/dados" + number + ".csv",
                        header=None,
                        sep=",",
                        index=False,
                    )
                    driver.get(
                        "https://owner-conversion.quintoandar.com.br/register/new/owner"
                    )
