#Базовый класс с общими методами (wait, click, text)
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 10

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Возвращает текущий URL страницы")
    def current_url(self):
        return self.driver.current_url

    
    @allure.step("Поиск элемента с ожиданием присутствия")
    def find_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    @allure.step("Подождать видимости элемента")
    def wait_for_element_visible(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
      
    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator, timeout=TIMEOUT):
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element
    
    @allure.step("Подождать кликабельности элемента")
    def wait_for_element_clickable(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    
    @allure.step("Кликнуть на элемент")
    def click_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()
      
    @allure.step("Подождать и проверить, что атрибут элемента содержит текст")
    def wait_for_attribute(self, locator, attribute, value, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_attribute(locator, attribute, value))
    
    @allure.step("Получить текст элемента")
    def get_text_on_element(self, locator, timeout=TIMEOUT):
        element = self.wait_for_element_visible(locator, timeout)
        return element.text
    
    @allure.step("Переход на другую вкладку")
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])