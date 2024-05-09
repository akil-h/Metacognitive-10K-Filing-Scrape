import time
import selenium

# Import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# Import TimeoutException
from selenium.common.exceptions import TimeoutException

# Import Action utilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Add options
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# Create webdriver object
driver = webdriver.Chrome(options=chrome_options)

# Get yahoo finance
link = 'https://finance.yahoo.com/lookup'
driver.get(link)
time.sleep(1)

# Let's scrape for conversations on big tech stocks from yahoo finance

tickers = ['MSFT'] # 'AAPL', 'NVDA'


for ticker in tickers:
    SearchBar = driver.find_element(By.ID, "ybar-sbq")
    SearchBar.send_keys(ticker)
    SearchBar.send_keys(Keys.ENTER)
    time.sleep(5)

    Table = driver.find_elements(By.XPATH, '//td[contains(@class, "C($primaryColor) W(51%)") or contains(@class, "Ta(end) Fw(600) Lh(14px)")]')
    TableList =[]

    #Collect all Names and Values
    for value in Table:
        TableList.append(value.text)
        print (value.text)

    time.sleep(10)