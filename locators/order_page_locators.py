# Локаторы станицы заказа
from selenium.webdriver.common.by import By

class OrderPageLocators:
    #Первая форма "Для кого самокат"
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_SELECTED = (By.XPATH, "//div[@class='select-search__select']//button[1]") # Выбор первого варианта в списке
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая форма "Про аренду"
    DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR_MONTH = (By.XPATH, "//div[@class='react-datepicker__month']")  # Календарь
    CALENDAR_DAY = (By.XPATH, "//div[@class='react-datepicker__day' and not(contains(@class, 'outside'))]")  # Доступные дни
    RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_PERIOD_DAY = (By.XPATH, "//div[text()='сутки']")
    RENTAL_PERIOD_TWO_DAYS = (By.XPATH, "//div[text()='двое суток']")
    RENTAL_PERIOD_THREE_DAYS = (By.XPATH, "//div[text()='трое суток']")
    RENTAL_PERIOD_FOUR_DAYS = (By.XPATH, "//div[text()='четверо суток']")
    RENTAL_PERIOD_FIVE_DAYS = (By.XPATH, "//div[text()='пятеро суток']")
    RENTAL_PERIOD_SIX_DAYS = (By.XPATH, "//div[text()='шестеро суток']")
    RENTAL_PERIOD_SEVEN_DAYS = (By.XPATH, "//div[text()='семеро суток']")

    # Цвета самоката
    BLACK_COLOR = (By.ID, "black")
    GREY_COLOR = (By.ID, "grey")
    
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Заказать']")
    
    # Подтверждение заказа
    CONFIRM_POPUP = (By.XPATH, "//div[contains(@class, 'Order_Modal') and contains(text(), 'Хотите оформить заказ')]")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    NO_BUTTON = (By.XPATH, "//button[text()='Нет']")

    # Результат заказа
    ORDER_SUCCESS_POPUP = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ')]")
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]")

     # Логотипы
    SAMOKAT_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")