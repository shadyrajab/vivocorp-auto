import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from driver.webdriver import get_driver

BASE64 = "https://vivocorp-parceiro.vivo.com.br/LoginCorp/captcha?id={}"


def get_base64(captcha_id: str):
    with get_driver() as driver:
        driver.get(BASE64.format(captcha_id))
        base64_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/pre"))
        )

        base64_element_json = json.loads(base64_element.text)
        return base64_element_json["base64"]
