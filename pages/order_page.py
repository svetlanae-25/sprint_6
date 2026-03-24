#Страница заказа
import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    @allure.step("Заполнение первой формы 'Для кого самокат'")
    def fill_first_order_form(self, first_name, surname, address, metro_station, phone):
        self.find_element(OrderPageLocators.FIRST_NAME).send_keys(first_name)
        self.find_element(OrderPageLocators.LAST_NAME).send_keys(surname)
        self.find_element(OrderPageLocators.ADDRESS).send_keys(address)
        self.find_element(OrderPageLocators.METRO_STATION).send_keys(metro_station)
        self.click_element(OrderPageLocators.METRO_STATION_SELECTED)
        self.find_element(OrderPageLocators.PHONE).send_keys(phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнение второй формы 'Про аренду'")
    def fill_second_order_form(self, date, comment):
        date_input = self.find_element(OrderPageLocators.DELIVERY_DATE)
        date_input.send_keys(date)
        date_input.send_keys("\n")
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_TWO_DAYS)
        self.click_element(OrderPageLocators.BLACK_COLOR)
        self.find_element(OrderPageLocators.COMMENT).send_keys(comment) 
        

    @allure.step("Клик по кнопке 'Заказать'во второй форме")
    def click_order_button(self):
        order_button = self.scroll_to_element(OrderPageLocators.ORDER_BUTTON)
        order_button.click()
        
        
    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.wait_for_element_visible(OrderPageLocators.CONFIRM_POPUP, 10)
        self.click_element(OrderPageLocators.YES_BUTTON)

    @allure.step("Проверка успешности заказа")
    def successfull_order(self):
        return self.wait_for_element_visible(OrderPageLocators.ORDER_SUCCESS_POPUP, 10)
    

    @allure.step("Клик по логу 'Самокат'")
    def click_samokat_logo(self):
        self.click_element(OrderPageLocators.SAMOKAT_LOGO)

    @allure.step("Клик по логу 'Яндекс'")
    def click_yandex_logo(self):
        self.click_element(OrderPageLocators.YANDEX_LOGO)

   