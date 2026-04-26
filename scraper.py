from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.bcentral.cl/inicio"


def obtener_dolar():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 30)

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        elemento = driver.find_element(
            By.CSS_SELECTOR,
            "#_BcentralIndicadoresViewer_INSTANCE_pLcePZ0Eybi8_myTooltipDelegate > div > div > div.fin-indicators-col1 > div > div > div:nth-child(6) > div > p.basic-text.fs-2.f-opensans-bold.text-center.c-blue-nb-2"
        )

        valor = elemento.text

        print("VALOR SCRAPED:", valor)

        valor = valor.replace("$", "").strip()
        valor = valor.replace(".", "")
        valor = valor.replace(",", ".")

        return float(valor)

    finally:
        driver.quit()
        