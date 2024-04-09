import time
import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

base_url = 'https://www.avito.ru/avito-care/eco-impact'

def open_eco(): #Метод открытия базовой страницы со счетчиками
    service = Service(executable_path='./chromedriver.exe') #Выбрали путь до драйвера
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(base_url) #Открыли страницу
    driver.maximize_window()
    time.sleep(50) #Дали пользователю время авторизоваться вручную!
    return driver

class EcoPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    counters = '(//div[@class="desktop-label-EIkG9"])[3]' #XPath

    # Getters
    def get_counters(self): #Получаем элемент с счетчиками
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, self.counters)))

    # Actions
    def screen(self, number_test): #Метод для скриншота
        now_date = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        self.driver.save_screenshot('./output/screenshot_test_#_' +str(number_test) + '_'+ str(now_date) + '.png')

"""Внимание! Во всех тестах требуется ручной ввод пользовательской информации!"""

def test_null_user():  # В этом тесте необходимо зайти пользователем с нулевым эко-вкладом
    print('Первый тест - вход пользователем с нулевым вкладом!')
    driver = open_eco()
    page = EcoPage(driver)
    action = ActionChains(driver)
    action.move_to_element((page.get_counters())).perform()
    scroll_value = 100
    driver.execute_script(f'window.scrollBy(0, {scroll_value});')
    time.sleep(5)
    page.screen(1)
    driver.quit()

def test_litres_kw():  # В этом тесте необходимо зайти пользователем с вкладом в литрах и кВт
    print('Ворой тест - вход пользователем с вкладом в литрах и кВт!')
    driver = open_eco()
    page = EcoPage(driver)
    action = ActionChains(driver)
    action.move_to_element((page.get_counters())).perform()
    scroll_value = 100
    driver.execute_script(f'window.scrollBy(0, {scroll_value});')
    time.sleep(5)
    page.screen(2)
    driver.quit()

def test_m_kw():  # В этом тесте необходимо зайти пользователем с вкладом в м3 и кВт
    print('Ворой тест - вход пользователем с вкладом в м3 и кВт!')
    driver = open_eco()
    page = EcoPage(driver)
    action = ActionChains(driver)
    action.move_to_element((page.get_counters())).perform()
    scroll_value = 100
    driver.execute_script(f'window.scrollBy(0, {scroll_value});')
    time.sleep(5)
    page.screen(3)
    driver.quit()

def test_litres_w():  # В этом тесте необходимо зайти пользователем с вкладом в литрах и вт
    print('Ворой тест - вход пользователем с вкладом в литрах и Вт!')
    driver = open_eco()
    page = EcoPage(driver)
    action = ActionChains(driver)
    action.move_to_element((page.get_counters())).perform()
    scroll_value = 100
    driver.execute_script(f'window.scrollBy(0, {scroll_value});')
    time.sleep(5)
    page.screen(4)
    driver.quit()