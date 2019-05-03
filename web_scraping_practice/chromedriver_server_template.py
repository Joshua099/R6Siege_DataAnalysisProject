import time
from selenium import webdriver
import selenium.webdriver.chrome.service as service

# This template uses ChromeDriverService, allowing you to start/stop ChromeDriver servers yourself with .quit()
# This template saves significant amount of time for large test suites where a ChromeDriver instance is created per test

service = service.Service('C:/Users/joshua/Downloads/chromedriver_win32/chromedriver_72.exe')
service.start()

capabilities = {'chrome.binary': 'C:/Users/joshua/Downloads/chromedriver_win32'}

driver = webdriver.Remote(service.service_url, capabilities)

# Open to a specific url
driver.get('http://inventwithpython.com');

# Any additional commands here




# Close remote-in browser
time.sleep(5) # So that you can see the process take place
driver.quit()

# I don't think this is necessary, but running scratch files without this command showed that there was a separate
# background process (4mb/process) for each time chromedriver.exe was called in service.start() However, driver.quit()
# already quits the remote in service. Not sure what exactly caused it though.
# Just to be safe...
service.stop()