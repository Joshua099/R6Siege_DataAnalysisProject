import time
from selenium import webdriver
import selenium.webdriver.chrome.service as service


# This template uses ChromeDriverService, allowing you to start/stop ChromeDriver servers yourself with .quit()
# This template saves significant amount of time for large test suites where a ChromeDriver instance is created per test

#############################################################
service = service.Service('C:/Users/joshua/Downloads/chromedriver_win32/chromedriver_72.exe')
service.start()

capabilities = {'chrome.binary': 'C:/Users/joshua/Downloads/chromedriver_win32'}

# open browser variable from remote server
driver = webdriver.Remote(service.service_url, capabilities)
# driver.quit()
# service.quit()
##############################################################
print(type(driver))

# Open to a specific url
driver.get('http://inventwithpython.com');


# try:
#     elem = driver.find_element_by_id('navbarSupportedContent')
#     print('Found <%s> element with that name!' % (elem.tag_name))
# except:
#     print('Was not able to find an element with that name.')

linkElem = driver.find_element_by_link_text('Buy on Amazon')
print(type(linkElem))

linkElem.click()

# Filling out and submitting Forms
driver.get('https://mail.google.com')
email_elem = driver.find_element_by_id('identifierId')
print(type(email_elem))
email_elem.send_keys('email')
nextButton = driver.find_element_by_id('identifierNext')
time.sleep(2)
nextButton.click()

# PROBLEM: Google hides password element until username field is filled. The password element is not interactable until
# it is no longer hidden. Some suggestions for fixes were to use implicit/explicit waits so that the password element is unlocked
# but I cant get it to work. **SOLVED**
# driver.find_element_by_css_selector("input[type='password'] class='whs0nd zHQkBf'")

# *** SOLVED - just use time.sleep for a bit so that the element can appear :') ***
time.sleep(3)
password = driver.find_element_by_css_selector("input[type='password']")
password.send_keys("fake")

# Tried different methods...
# password = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password'] class='whs0nd zHQkBf'")))


# from selenium.common.exceptions import ElementNotVisibleException
# try:
#     password.send_keys('fake')
# except ElementNotVisibleException as Exception:
#     print("The element is not interactable... trying a new element.")
#     driver.find_element
#     password = driver.find_element_by_id('password')
#     password.send_keys('fake')



time.sleep(5) # So that you can see the process take place
driver.quit()
