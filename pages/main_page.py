#Главная старница (вопросы, кнопки заказа)
import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step("Клик по вопросу в разделе FAQ")
    def click_faq_question(self, question_id):
        self.scroll_to_element(MainPageLocators.FAQ_HEADER)
        self.click_element(MainPageLocators.faq_question(question_id))

    @allure.step("Получение текста ответа на вопрос")
    def get_faq_answer_text(self, question_id):
        element_text = self.get_text_on_element(MainPageLocators.faq_answer(question_id))
        return element_text
    
    @allure.step("Клик по кнопке 'Заказать' вверху страницы")
    def click_order_button_on_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Клик по кнопке 'Заказать' внизу страницы")
    def click_order_button_middle(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
        self.click_element(MainPageLocators.ORDER_BUTTON_MIDDLE)


       
    @allure.step("Принять куки, если есть")
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_ACCEPT_BUTTON, 3)
        except:
            pass    