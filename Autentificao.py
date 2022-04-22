from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from credenciais import USER, PASSWORD, KEY
from datetime import datetime
import pyotp
import time


class Autentificao:
    def autentificar(driver):
        try:
            WebDriverWait(driver, 60).until(
                ec.visibility_of_element_located(
                    (By.XPATH, "/html/body/div/div[2]/div/div/div[1]/div[2]/ul/li/a",)
                )
            )
        except TimeoutException:
            driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
        driver.find_element_by_xpath(
            "/html/body/div/div[2]/div/div/div[1]/div[2]/ul/li/a"
        ).click()
        try:
            WebDriverWait(driver, 60).until(
                ec.visibility_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input",
                    )
                )
            )
        except TimeoutException:
            driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
        ).send_keys(USER)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button"
        ).click()
        try:
            WebDriverWait(driver, 60).until(
                ec.visibility_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input",
                    )
                )
            )
        except TimeoutException:
            driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
        ).send_keys(PASSWORD)
        time.sleep(2)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button"
        ).click()
        try:
            WebDriverWait(driver, 60).until(
                ec.visibility_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button",
                    )
                )
            )
            time.sleep(1)
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button"
            ).click()
        except TimeoutException:
            driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
        try:
            WebDriverWait(driver, 60).until(
                ec.visibility_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/ul/li[3]",
                    )
                )
            )
            time.sleep(1)
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/ul/li[3]"
            ).click()
        except TimeoutException:
            driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
        totp = pyotp.TOTP(KEY)
        token = totp.now()
        try:
            WebDriverWait(driver, 60).until(
                ec.visibility_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input",
                    )
                )
            )
            driver.find_element_by_xpath(
                "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[1]/div/div[1]/input"
            ).send_keys(token)
        except TimeoutException:
            driver.get("https://owner-conversion.quintoandar.com.br/register/new/owner")
        time.sleep(2)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button"
        ).click()
