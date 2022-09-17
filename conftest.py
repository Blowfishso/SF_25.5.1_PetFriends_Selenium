import pytest
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('C:\drivers\chromedriver')
    pytest.driver.set_window_size(1920, 1080)
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield
    pytest.driver.quit()

@pytest.fixture
def go_to_my_pets():
    pytest.driver.set_window_size(1920, 1080)
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    # Вводим email
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'email')))
    pytest.driver.find_element_by_id('email').send_keys(valid_email)

    # Вводим пароль
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'pass')))
    pytest.driver.find_element_by_id('pass').send_keys(valid_password)

    # Нажимаем на кнопку входа в аккаунт
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    # Нажимаем на ссылку "Мои питомцы"
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Мои питомцы')))
    pytest.driver.find_element_by_link_text('Мои питомцы').click()
