from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def obtener_dolar_dia():
    """Extrae el valor del dólar desde bcentral.cl usando Selenium."""
    options = Options()
    options.add_argument("--headless")  # Esto evita que se abra la ventana del navegador
    
    # Configura el driver automáticamente
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # Navega al sitio oficial solicitado
        driver.get("https://www.bcentral.cl/inicio")
        
        # Busca el valor del dólar en la tabla de indicadores principales
        xpath_dolar = '//*[@id="_bcentralindicadoreseconomicos_WAR_bcentralindicadoreseconomicosportlet_column-1"]/div/div/div/div/table/tbody/tr[1]/td[2]/span'
        elemento = driver.find_element(By.XPATH, xpath_dolar)
        
        # Limpia el texto para que sea un número (ej: 950,50 -> 950.50)
        valor_texto = elemento.text.replace('.', '').replace(',', '.')
        return float(valor_texto)
    finally:
        driver.quit()
        