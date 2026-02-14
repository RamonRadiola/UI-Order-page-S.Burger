from pages.base_page import BasePage
from locators import Locators
import allure



class OrderPage(BasePage):
    @allure.step("Проверка появления надписи 'Для кого самокат'")
    def check_visio_test(self):
        self.find_element_for_visio(locator=Locators.SIGNAL_ORDER_1)

    @allure.step("ввод имени")
    def input_name(self, name):
        self.find_element_for_visio(locator=Locators.PHOLD_NAME).send_keys(name)

    @allure.step("ввод фамилии")
    def input_surname(self, surname):
        self.find_element_for_visio(locator=Locators.PHOLD_SURNAME).send_keys(surname)

    @allure.step("ввод адреса")
    def input_addres(self, addres):
        self.find_element_for_visio(locator=Locators.PHOLD_ADDRES).send_keys(addres)

    @allure.step("Метод клика по полю для появления списка со станциями метро")
    def click_metro_holder(self):
        self.find_element_for_click(locator=Locators.PHOLD_METRO).click()

    @allure.step("Метод клика по элементу списка со станциями метро")
    def choose_station_first_var(self):
        self.find_element_for_click(locator=Locators.PHOLD_CHOSE_STATION_1).click()

    @allure.step("Метод клика по элементу списка со станциями метро")
    def choose_station_second_var(self):
        self.find_element_for_click(locator=Locators.PHOLD_CHOSE_STATION_2).click()

    @allure.step("ввод номера телефона")
    def input_number(self, number):
        self.find_element_for_visio(locator=Locators.PHOLD_NUMBER).send_keys(number)

    @allure.step("клик по кнопке 'далее'")
    def button_next(self):
        self.find_element_for_click(locator=Locators.BUTTON_NEXT).click()

    @allure.step("выбор даты доставки")
    def click_data_first_var(self):
        self.find_element_for_click(locator=Locators.PHOLD_DATA).click()
        self.find_element_for_click(locator=Locators.PHOLD_DATA_CHOOSE_1).click()

    @allure.step("выбор даты доставки")
    def click_data_second_var(self):
        self.find_element_for_click(locator=Locators.PHOLD_DATA).click()
        self.find_element_for_click(locator=Locators.PHOLD_DATA_CHOOSE_2).click()

    @allure.step("выбор срока аренды")
    def click_rental_one_day(self):
        self.find_element_for_click(locator=Locators.RENTAL_PERIOD).click()
        self.find_element_for_click(locator=Locators.RENTAL_1_DAYS).click()

    @allure.step("выбор срока аренды")
    def click_rental_five_days(self):
        self.find_element_for_click(locator=Locators.RENTAL_PERIOD).click()
        self.find_element_for_click(locator=Locators.RENTAL_5_DAYS).click()

    @allure.step("выбор черного самоката")
    def choose_color_black(self):
        self.find_element_for_click(locator=Locators.POINT_BLACK).click()

    @allure.step("выбор серого самоката")
    def choose_color_grey(self):
        self.find_element_for_click(locator=Locators.POINT_GREY).click()

    @allure.step("Метод оставления комментария курьеру")
    def comment_for_courier(self, comment):
        self.find_element_for_click(locator=Locators.PHOLD_COMMENT).send_keys(comment)

    @allure.step("Метод клика по кнопке 'заказать'")
    def click_button_order_down_2(self):
        self.find_element_for_click(locator=Locators.BUTTON_ORDER_DOWN_2).click()

    @allure.step("Метод клика по кнопке 'заказать'")
    def click_button_order_up_2(self):
        self.find_element_for_click(locator=Locators.BUTTON_ORDER_UP_2).click()

    @allure.step("Метод клика по кнопке 'ДА'")
    def click_button_yes(self):
        self.find_element_for_click(locator=Locators.BUTTON_YES).click()

    @allure.step("проверка статуса заказа")
    def check_button_status(self):
        self.find_element_for_click(locator=Locators.BUTTON_SEE_STATUS)

    @allure.step("Метод прокрутки страницы до кнопки 'заказать'")
    def scroll_to_order_button(self):
        return self.scroll_to_element_base(locator=Locators.BUTTON_ORDER_DOWN)

    @allure.step("поиск сообщения о готовности заказа")
    def check_current_status(self):
        assert 'Заказ оформлен' in self.find_element_for_visio(Locators.SIGNAL_ORDER_IS_READY).text