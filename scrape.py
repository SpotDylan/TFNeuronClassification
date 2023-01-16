#This file is meant to collect data from the website https://neuromorpho.org/byspecies.jsp#top for our training and testing data sets.
#Sepcifically we are looking for human data sets

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



class startScrape:
    def scrape(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)
        driver.get('https://neuromorpho.org/byspecies.jsp#top')
        humanSection = driver.find_elements(By.XPATH, '/html/body/div[1]/table/tbody/tr[3]/td/table[1]/tbody/tr/td[2]/table/tbody/tr/td/div/form/table/tbody/tr/td[1]/table/tbody/tr[2]/td/div/ul/li[43]')
        #WIP
ls = startScrape()
ls.scrape()
