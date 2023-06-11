import allure
from demoqa_tests.pages.registration_page_form import RegistrationPage


def test_form_demo():
    with allure.step('Открываем главную страницу'):
        registration_page = RegistrationPage()
        registration_page.open()

    with allure.step('Заполняеи фамилию и имя'):
        registration_page.type_first_name('Alexander')
        registration_page.type_last_name('Pupkin')

    with allure.step('Заполняем почту, пол, номер телефона и дату рождения'):
        registration_page.type_user_email('Pupkin@gmail.com')
        registration_page.select_user_gender('Female')
        registration_page.type_user_phone_number('79067777777')
        registration_page.click_input_birthday('1990', 'November', '10')

    with allure.step('Заполняем предменты и хобби'):
        registration_page.type_subjects('Computer Science', 'English')
        registration_page.select_hobbies('sport')

    with allure.step('Выбираем изображение'):
        registration_page.chose_file('pocita.jpg')

    with allure.step('Скролим страницу'):
        registration_page.scroll_page()

    with allure.step('Заполняем адрес'):
        registration_page.type_current_adress('914751, Оренбургская область, город Волоколамск, проезд Сталина, 09')
        registration_page.type_state_and_press_enter('Haryana')
        registration_page.type_city_and_press_enter('Karnal')

    with allure.step('Проходим регистрацию'):
        registration_page.press_enter_by_confirm_registration()

    with allure.step('Проверяем данные на корректность'):
        registration_page.assert_user_info(
            'Student Name Alexander Pupkin',
            'Student Email Pupkin@gmail.com',
            'Gender Female',
            'Mobile 7906777777',
            'Date of Birth 10 November,1990',
            'Subjects Computer Science,' ' English',
            'Hobbies Sports',
            'Picture pocita.jpg',
            'Address 914751, Оренбургская область, город Волоколамск, проезд Сталина, 09',
            'State and City Haryana Karnal'
        )

