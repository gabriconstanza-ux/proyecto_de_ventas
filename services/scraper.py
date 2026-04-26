from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def obtener_valor_dolar():
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.bcentral.cl")

        elemento = driver.find_element(By.XPATH, "//div[contains(text(),'Dólar')]")
        valor = elemento.text.split("$")[-1].strip().replace(".", "").replace(",", ".")

        return float(valor)

    except Exception:
        return 900.0  # fallback si falla scraping

    finally:
        driver.quit()
        