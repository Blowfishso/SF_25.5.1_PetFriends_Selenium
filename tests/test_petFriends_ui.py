import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_all_pets_are_present(go_to_my_pets):

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    # Сохраняем в statistic информацию о количестве питомцев
    statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    # Сохраняем в переменную pets элементы карточек питомцев
    pets = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    # Получаем количество питомцев из статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Получаем количество карточек питомцев
    number_of_pets = len(pets)

    assert number == number_of_pets

def test_pet_photo(go_to_my_pets):

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
    # Сохраняем в statistic информацию о количестве питомцев
    statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")

    # Сохраняем в переменную images элементы с атрибутом img
    images = pytest.driver.find_elements_by_css_selector('.table.table-hover img')

    # Получаем количество питомцев из статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Находим половину от количества питомцев
    half = number // 2

    # Находим количество питомцев с фотографией
    number_а_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_а_photos += 1

    # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
    assert number_а_photos >= half

def test_all_pets_have_name_age_type(go_to_my_pets):

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    # Сохраняем в переменную pets элементы карточек питомцев
    pets = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    string = pytest.driver.find_elements_by_xpath('//table[@class ="table table-hover"]/tbody/tr')
    name = pytest.driver.find_elements_by_xpath("//tr/td[1]")
    animal_type = pytest.driver.find_elements_by_xpath('//tr/td[2]')
    age = pytest.driver.find_elements_by_xpath('//tr/td[3]')
    for i in range(len(string)):
        assert name[i].text and animal_type[i].text and age[i].text != ''
        count_name = len(name)
        count_type = len(animal_type)
        count_age = len(age)
        assert count_type == count_name
        assert count_name == count_age

def test_pets_have_different_names(go_to_my_pets):

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    # Сохраняем в переменную pets элементы карточек питомцев
    pets = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    pets_name = []
    for i in range(len(pets)):
        data_pet = pets[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    assert r == 0
    print(r)
    print(pets_name)

def test_no_duplicate_pets(go_to_my_pets):

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    # Сохраняем в переменную pets элементы карточек питомцев
    pets = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    list_data = []
    for i in range(len(pets)):
        data_pet = pets[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)

    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '

    list_line = line.split(' ')

    set_list_line = set(list_line)

    a = len(list_line)
    b = len(set_list_line)

    result = a - b

    assert result == 0