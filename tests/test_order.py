#Проверка позитивного сценария заказа самоката
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from curl import main_site
from data import OrderTestOne
from data import OrderTestTwo


class TestOrder:
    @allure.title("Оформление заказа через верхнюю кнопку 'Заказать с первым набором данных'")
    def test_order_button_top(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button_on_top()
        order_page = OrderPage(driver)
        #Заполняем первую форму заказа
        order_page.fill_first_order_form(
            OrderTestOne.name_one, 
            OrderTestOne.surname_one,
            OrderTestOne.address_one,
            OrderTestOne.metro_station_one,
            OrderTestOne.phone_one
        )
        
        #Заполняем вторую форму заказа
        order_page.fill_second_order_form(
            OrderTestOne.date_one,
            OrderTestOne.comment_one
        )

        #Нажимаем кнопку 'Заказать'
        order_page.click_order_button()

        #Подтверждаем заказ
        order_page.confirm_order()
                      
        #Проверяем успешность создания заказа
        assert order_page.successfull_order()


    @allure.title("Оформление заказа через нижнюю кнопку 'Заказать со вторым набором данных'")
    def test_order_button_middle(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button_middle()
        order_page = OrderPage(driver)
        #Заполняем первую форму заказа
        order_page.fill_first_order_form(
            OrderTestTwo.name_two, 
            OrderTestTwo.surname_two,
            OrderTestTwo.address_two,
            OrderTestTwo.metro_station_two,
            OrderTestTwo.phone_two
        )
        
        #Заполняем вторую форму заказа
        order_page.fill_second_order_form(
            OrderTestTwo.date_two,
            OrderTestTwo.comment_two
        )

        #Нажимаем кнопку 'Заказать'
        order_page.click_order_button()

        #Подтверждаем заказ
        order_page.confirm_order()
                      
        #Проверяем успешность создания заказа
        assert order_page.successfull_order()
    
    @allure.title("Клик по логотипу Самоката ведет на главную")
    def test_samokat_logo_redirects_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button_on_top()#Переходим на страницу заказа по клику на кнопку "Заказать" вверху страницы 
        order_page = OrderPage(driver)
        order_page.click_samokat_logo() #Кликаем по логотипу Самоката
        assert order_page.current_url() == main_site #Проверяем, что находимся на главной странице
            
            
    @allure.title("Клик по логотипу Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button_on_top()#Переходим на страницу заказа по клику на кнопку "Заказать" вверху страницы 
        order_page = OrderPage(driver)  
        order_page.click_yandex_logo() # Кликаем по логотипу Яндекса
        order_page.switch_to_window()
        # Проверяем, что открылся Дзен
        assert "dzen.ru" in order_page.current_url()


   