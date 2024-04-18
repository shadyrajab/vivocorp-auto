import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from driver.webdriver import get_driver

URL = "https://vivocorp-parceiro.vivo.com.br/LoginCorp/captcha"


def get_captcha_id():
    with get_driver() as driver:
        driver.get(URL)
        captcha_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/pre"))
        )

        captcha_element_json = json.loads(captcha_element.text)
        return captcha_element_json["id"]
