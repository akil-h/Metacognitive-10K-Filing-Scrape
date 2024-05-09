import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# import exeptions if element is not found
from selenium.common.exceptions import NoSuchElementException

Historical_data = pd.DataFrame()
Statistics_data = pd.DataFrame()

def GetStatistics(ticker):
    global Statistics_data
    Statistics = pd.DataFrame(np.empty(0, 61))
    StatisticsTab = driver.find_element(By.XPATH, '//li[@data-test="STATISTICS"]/a[contains(@href, "key-statistics")]/span[text()="Statistics"]')
    pass

def GetHistoricals(ticker):
    pass