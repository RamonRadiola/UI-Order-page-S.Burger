from pages.home_page import HomePage
from pages.order_page import OrderPage
from constants import Constants
from data import Data
import allure

@allure.story("Кликает на плашку вопроса, проверяет текст выпадающего ответа")
class TestOrderPage:
    @allure.title("Первый сценарий через кнопку сверху")
    def test_positive_order_first(self, home_page_order):
        order_page = OrderPage(home_page_order.driver)
        home_page_order.click_button_order_up()
        order_page.input_name(Data.FIRST_ORDER["name"])
        order_page.input_surname(Data.FIRST_ORDER["surname"])
        order_page.input_addres(Data.FIRST_ORDER["address"])
        order_page.input_number(Data.FIRST_ORDER["number"])
        order_page.click_metro_holder()
        order_page.choose_station_first_var()
        order_page.button_next()
        order_page.click_data_first_var()
        order_page.click_rental_one_day()
        order_page.choose_color_black()
        order_page.comment_for_courier(Data.FIRST_ORDER["comment"])
        order_page.click_button_order_down_2()
        order_page.click_button_yes()
        order_page.check_button_status()
        order_page.check_current_status()

    @allure.title("Второй сценарий через кнопку снизу")
    def test_positive_order_second(self, home_page_order):
        order_page = OrderPage(home_page_order.driver)
        home_page_order.click_button_order_down()
        order_page.input_name(Data.SECOND_ORDER["name"])
        order_page.input_surname(Data.SECOND_ORDER["surname"])
        order_page.input_addres(Data.SECOND_ORDER["address"])
        order_page.input_number(Data.SECOND_ORDER["number"])
        order_page.click_metro_holder()
        order_page.choose_station_second_var()
        order_page.button_next()
        order_page.click_data_second_var()
        order_page.click_rental_five_days()
        order_page.choose_color_grey()
        order_page.comment_for_courier(Data.SECOND_ORDER["comment"])
        order_page.click_button_order_down_2()
        order_page.click_button_yes()
        order_page.check_button_status()
        order_page.check_current_status()

    @allure.title("Переход по логотипу 'самокат'")
    def test_click_scooter(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site(driver)
        home_page.click_button_order_up()
        home_page.click_logo_scooter()
        assert home_page.check_current_url() == Constants.URL

    @allure.title("Переход по логотипу 'Яндекс'")
    def test_click_ya(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site(driver)
        home_page.click_logo_ya()
        home_page.wait_for_number_of_windows_to_be(2)
        home_page.switch_new_window()
        home_page.wait_for_url_to_be(Constants.URL_DZEN)
        assert home_page.check_current_url() == Constants.URL_DZEN