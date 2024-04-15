from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from constants import USERNAME, PASSWORD


def get_driver(is_headless):
    if is_headless:
        headless_option = Options()
        headless_option.add_argument("--headless")
        return webdriver.Chrome(options=headless_option)
    else:
        return webdriver.Chrome()


def open_url_with_chrome(url: str, is_headless: bool):
    driver = get_driver(is_headless)
    driver.get(url)
    return driver


def sign_in(driver):
    username = driver.find_element('id', 'username')
    username.send_keys(USERNAME)
    password = driver.find_element('id', 'password')
    password.send_keys(PASSWORD)
    signin = driver.find_element('id', 'loginbutton')
    signin.click()
    return True
