from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtener_dolar_dia():
    options = Options()
    options.add_argument("--headless")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.bcentral.cl/inicio")

        wait = WebDriverWait(driver, 10)

        elemento = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//td[contains(text(),'Dólar')]//following-sibling::td//span")
            )
        )

        valor_texto = elemento.text.replace('.', '').replace(',', '.')
        return float(valor_texto)

    finally:
        driver.quit()
        