# Локаторы главной страницы
from selenium.webdriver.common.by import By

class MainPageLocators:
    
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")  # Верхняя кнопка
    ORDER_BUTTON_MIDDLE = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")  # Нижняя кнопка
    
    # Заголовок секции вопросов о важном (для скролла)
    FAQ_HEADER = (By.XPATH, "//div[text()='Вопросы о важном']")
    
    @staticmethod
    def faq_question(question_id):
        return By.ID, f"accordion__heading-{question_id}"
    
    @staticmethod
    def faq_answer(question_id):
        return By.XPATH, f"//div[@id='accordion__panel-{question_id}']/p"
    
 
       
    #Cookie-уведомление
    COOKIE_ACCEPT_BUTTON = (By.ID, "rcc-confirm-button")