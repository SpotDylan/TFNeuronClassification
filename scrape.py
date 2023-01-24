#This module will use the URLs that were collected from the module scrapeURLs.py to actually collect training/testing data from individual neurons
#Specifically, we'll use Selenium to open each URL and collect/record data to a CSV file

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
            for i in it:
                currentURL = 'https://neuromorpho.org/neuron_info.jsp?neuron_name=' + i.text
                driver.get(currentURL)
                neuron = driver.find_elements(By.XPATH,
                                            '/html/body/div/table/tbody/tr[3]/td/table[1]/tbody/tr/td[2]/table/tbody/tr/td/div/center/div/div/div/table[4]/tbody/tr/td/table/tbody/tr/td/table/tbody')
                file = open("trainingdatasetDUMB.csv", "w")
                writer = csv.writer(file)
                writer.writerow(["Soma Surface", "Number of Stems", "Number of Bifurcations", "Number of Branches",
                                 "Overall Width", "Overall Height", "Overall Depth", "Average Diameter", "Total Length",
                                 "Total Surface", "Total Volume", "Max Euclidean Distance", "Max Path Distance",
                                 "Max Branch Order", "Average Contraction", "Total Fragmentation",
                                 "Partition Asymmetry",
                                 "Average Rall's Ratio", "Average Bifurcation Angle Local",
                                 "Average Bifurcation Angle Remote", "Fractal Dimension"])

                # Define the mapping between the data name and the column index
                column_mapping = {
                    "Soma Surface": 1,
                    "Number of Stems": 2,
                    "Number of Bifurcations": 3,
                    "Number of Branches": 4,
                    "Overall Width": 5,
                    "Overall Height": 6,
                    "Overall Depth": 7,
                    "Average Diameter": 8,
                    "Total Length": 9,
                    "Total Surface": 10,
                    "Total Volume": 11,
                    "Max Euclidean Distance": 12,
                    "Max Path Distance": 13,
                    "Max Branch Order": 14,
                    "Average Contraction": 15,
                    "Total Fragmentation": 16,
                    "Partition Asymmetry": 17,
                    "Average Rall's Ratio": 18,
                    "Average Bifurcation Angle Local": 19,
                    "Average Bifurcation Angle Remote": 20,
                    "Fractal Dimension": 21
                }

                # Create an empty list to store the values
                values = [None] * 21

                neuron_data = neuron[0].text.split('\n')
                for data in neuron_data:
                    data = data.split(':')
                    name = data[0].strip()
                    value = data[1].strip().replace(" μm", "").replace("°", "")
                    column = column_mapping.get(name)
                    values[column - 1] = value

                # Write the values to the CSV file
                writer.writerow(values)
                file.close()
                driver.quit()

ls = startScrape()
ls.scrape()
