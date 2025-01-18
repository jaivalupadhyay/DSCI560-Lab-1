import os, time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import FirefoxOptions

u = "https://www.cnbc.com/world/?region=world"
output_path = "../data/raw_data"
file = "web_data.html"

# Setting up the Firefox WebDriver
service = Service("/snap/bin/firefox.geckodriver", log_path = 'geckodriver.log')
driver = webdriver.Firefox(service=service)

print("Connected driver")
# Open a webpage
res = driver.get(u)

# Wait for all elems to get loaded
time.sleep(10)
file_path = os.path.join(output_path, file)
with open(file_path, "w") as f:
    f.write(driver.page_source)
print("File Saved!")

# Closing browser
driver.quit()

