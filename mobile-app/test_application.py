from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time


def test_enter_value(appium_driver):
    driver = appium_driver
    my_text = 'Hello'

    wait = WebDriverWait(driver, 25, poll_frequency=1,
                        ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                            NoSuchElementException])

    button = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/EnterValue'))
    button.click()

    edit_text = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText'))
    edit_text.send_keys(my_text)

    button = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Btn1'))
    button.click()

    text_view = wait.until(lambda x: x.find_element(AppiumBy.XPATH,
                                                    '//android.widget.TextView[@resource-id="com.code2lead.kwad:id/Tv1"]'))
    assert text_view.text == my_text

    time.sleep(3)

def test_form(appium_driver):
    driver = appium_driver
    wait = WebDriverWait(driver, 25, poll_frequency=1,
                        ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                            NoSuchElementException])
    button = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/ContactUs'))
    button.click()

    counter = 0
    edit_texts = wait.until(lambda x: x.find_elements(AppiumBy.CLASS_NAME, 'android.widget.EditText'))
    for el in edit_texts:
        counter += 1
        el.send_keys(f'Value {counter}')

    button = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Btn2'))
    button.click()

    time.sleep(3)

def test_scrollview(appium_driver):
    driver = appium_driver
    wait = WebDriverWait(driver, 25, poll_frequency=1,
                        ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                            NoSuchElementException])
    button = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/ScrollView'))
    button.click()

    button = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON2"]'))
    button.click()

    button = wait.until(lambda x: x.find_element(AppiumBy.ID, 'android:id/button2'))
    button.click()

    button = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="BUTTON6"]'))
    button.click()

    button = wait.until(lambda x: x.find_element(AppiumBy.ID, 'android:id/button1'))
    button.click()

    time.sleep(3)