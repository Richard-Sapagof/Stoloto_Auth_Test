import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://www.stoloto.ru/')
    yield browser
    browser.quit()

def auth(browser):
    browser.find_element_by_xpath('//span[text()="Войти"]').click()
    browser.find_element_by_xpath('//*[@id="auth_login"]').send_keys("***")
    browser.find_element_by_xpath('//*[@id="auth_password"]').send_keys('***')
    WebDriverWait(browser, 15).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@class="submit_button_container"]'))).click()

@pytest.mark.skip()
def test_check_ticket(browser):
    auth(browser)
    """вызываю функцию авторизации"""
    browser.find_element_by_xpath('//*[@href="/check-ticket"]').click()
    browser.find_element_by_xpath('//*[@class="game_select_popup_opener with_icon popup_positioner"]').click()
    browser.find_element_by_xpath('//*[@href="/check-ticket/ruslotto"]').click()
    browser.find_element_by_xpath('//*[@id="check_drawing_number"]').send_keys(1369)
    browser.find_element_by_xpath('//*[@id="check_ticket_number"]').send_keys(999684854823)
    WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[text()="Проверить"]'))).click()
    victory = browser.find_element_by_xpath('//*[@class="h1_prize"]').text

    assert victory == "100 ₽"


@pytest.mark.skip()
def test_sending_sms(browser):
    auth(browser)
    browser.find_element_by_xpath('//*[@href="/mobile-applications?bls=prilogenia_stoloto&int=podval"]').click()
    browser.find_element_by_xpath('//form[@class="send_form"]/input[@name="phone"]').send_keys(89653800019)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='submit']/button"))).click()

@pytest.mark.skip()
def test_buy_ticket_of_wallet(browser):
    auth(browser)
    browser.find_element_by_xpath('//a[@href="/7x49/game?from=regular"]').click()
    browser.find_elements_by_xpath('//span[@title="Случайно"][1]')[1].click()
    browser.find_element_by_xpath('//button[@class="pretty_button type_wallet btn_m   scaller"]').click()
