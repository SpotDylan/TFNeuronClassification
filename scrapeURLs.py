#This file is meant to scrape URLs from Neuromorpho for the nearly 11000 different types of Neurons
#The URLs from this scraper will be used in our main scraping module, where the data of each will be recorded to a CSV
#and that CSV file will be used to train/test our model

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


class startScrape:
    def scrape(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options = chrome_options)
        driver.get('https://neuromorpho.org/byspecies.jsp#top')
        humanSection = driver.find_elements(By.CSS_SELECTOR, 'li.menugreen a.species[name="human"]')
        humanSection[0].click()

        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'screenshot')))
        finally:
            neuronName = driver.find_elements(By.CLASS_NAME, 'screenshot')
            it = iter(neuronName)
            #Create our text file where we'll write our URLs too. These URLs and this text file will later be accessed to record
            #our training and testing data to a CSV file
            with open('neuromorphoURLs.txt', 'w') as file:
                for i in it:
                    currentURL = 'https://neuromorpho.org/neuron_info.jsp?neuron_name=' + i.text
                    file.write(currentURL + '\n')
