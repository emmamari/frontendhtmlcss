from xml.etree.ElementTree import Element

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

appium_service = AppiumService()
appium_service.start()

my_text = 'Hello'

desired_caps = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "platformVersion": "10",
    "deviceName": "Pixel 5.5 API 30",
    "udid": "emulator-5554",
    "app": r"C:\Users\mshin\qa_15_appium\pythonProject\Android_Demo_App_V2.apk",
    "appPackage": "com.google.android.apps.nexuslauncher",
    "appActivity": "com.google.android.apps.nexuslauncher.NexusLauncherActivity",
}

options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723', options=options, direct_connection=True)

wait = WebDriverWait(driver, 25, poll_frequency=1,
                    ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

button = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/ContactUs'))
button.click()

counter = 0
edit_texts = wait.until(lambda x: x.find_elements(AppiumBy.CLASS_NAME, 'android.widget.EditText'))
for el in edit_texts:
    counter += 1
    el.send_keys(f'Value {counter}')

button = wait.until(lambda x: x.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Btn2'))
button.click()

time.sleep(5)
driver.quit()

appium_service.stop()