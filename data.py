from locators import Locators


class Data:
    QUESTION_DATA = [
        {"question_locator": Locators.QUESTION_0, "answer_locator": Locators.ANSWER_0,
        "expected_text": "Сутки — 400 рублей."},
        {"question_locator": Locators.QUESTION_1, "answer_locator": Locators.ANSWER_1,
         "expected_text": "Пока что у нас так"},
        {"question_locator": Locators.QUESTION_2, "answer_locator": Locators.ANSWER_2,
        "expected_text": "вы оформляете заказ"},
        {"question_locator": Locators.QUESTION_3, "answer_locator": Locators.ANSWER_3,
         "expected_text": "начиная с завтрашнего дня"},
        {"question_locator": Locators.QUESTION_4, "answer_locator": Locators.ANSWER_4, "expected_text": "Пока что нет"},
        {"question_locator": Locators.QUESTION_5, "answer_locator": Locators.ANSWER_5,
        "expected_text": "Самокат приезжает к вам"},
        {"question_locator": Locators.QUESTION_6, "answer_locator": Locators.ANSWER_6,
        "expected_text": "пока самокат не привезли"},
    ]


    # Данные для первого заказа
    FIRST_ORDER = {
        "name": "Лиля",
        "surname": "Брикс",
        "address": "Москва, Покровскакая 4",
        "number": "89001001020",
        "comment": "Я вас очень жду"
    }

    # Данные для второго заказа
    SECOND_ORDER = {
        "name": "Игорь",
        "surname": "Ильин",
        "address": "Москва, Центральная 5",
        "number": "89525556060",
        "comment": "Мороженое оставьте себе"
    }