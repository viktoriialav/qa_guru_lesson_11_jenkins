from datetime import date

import allure
from selene import browser, have, command
from selenium.webdriver.common.keys import Keys


@allure.title('Successful fill form')
def test_demoqa_student_registration_form(setup_browser):
    first_name = 'Viktoriia'
    last_name = 'Lav'
    user_email = 'newuser@gmail.com'
    user_gender = 'Female'
    user_number = '8800222334'
    date_of_birth = date(1993, 5, 17)
    user_subjects = 'Chemistry'
    user_hobbies = 'Sports'
    # user_picture='photo.png'
    user_current_address = '144 Broadway, suit 12'
    user_state = 'NCR'
    user_city = 'Gurgaon'


    with allure.step('Open registration form'):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.element('.practice-form-wrapper').should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step('Fill form'):
        browser.element('#firstName').type(first_name)
        browser.element('#lastName').type(last_name)
        browser.element('#userEmail').type(user_email)
        browser.all('[name=gender]').element_by(have.value(user_gender)).element('..').click()
        browser.element('#userNumber').type(user_number)

        browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type(
            date_of_birth.strftime('%m.%d.%Y')).press_enter()

        browser.element('#subjectsInput').type(user_subjects).click().press_enter()
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(user_hobbies)).click()
        # browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Reading')).click()

        browser.element('#currentAddress').set_value(user_current_address)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user_state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(user_city)).click()

        # browser.element('#uploadPicture').send_keys(os.path.abspath(
        #     os.path.join(os.path.dirname(tests.__file__), 'resources/photo.png')
        # ))

        browser.element('#submit').click()

    with allure.step('Check form results'):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
        # browser.element('.table').all('td').even.should(have.exact_texts('Viktoriia Lav',
        #                                                                  'newuser@gmail.com',
        #                                                                  'Female',
        #                                                                  '8800222334',
        #                                                                  '17 May,1993',
        #                                                                  'Chemistry',
        #                                                                  'Sports',
        #                                                                  'photo.png',
        #                                                                  '144 Broadway, suit 12',
        #                                                                  'NCR Gurgaon'))