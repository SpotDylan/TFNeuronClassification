from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

class startScrape:
    def scrape(self):
        counter = 0
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        file = open("trainingdatasetDUMB.csv", "w")
        writer = csv.writer(file)
        writer.writerow(["Soma Surface", "Number of Stems", "Number of Bifurcations", "Number of Branches",
                         "Overall Width", "Overall Height", "Overall Depth", "Average Diameter", "Total Length",
                         "Total Surface", "Total Volume", "Max Euclidean Distance", "Max Path Distance",
                         "Max Branch Order", "Average Contraction", "Total Fragmentation",
                         "Partition Asymmetry",
                         "Average Rall's Ratio", "Average Bifurcation Angle Local",
                         "Average Bifurcation Angle Remote", "Fractal Dimension"])
        with open("neuromorphoURLs.txt", "r") as file:
            for line in file:
                driver.get(line)
                # create a list to hold the numerical values
                values = []
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'bord')))
                finally:
                    neuron = driver.find_elements(By.CLASS_NAME, 'bord')

                # iterate through the elements in neuron[2].text
                for element in neuron[2].text.split("\n"):
                    if element != "Measurements":
                        # remove the unit from the element and append the numerical value to the list
                        value = element.split(":")[1].strip().replace(" μm", "").replace("°", "")
                        try:
                            values.append(float(value))
                        except ValueError:
                            if value == "N/A":
                                values.append(value)
                            else:
                                raise ValueError("Unexpected value found: {}".format(value))
                # write the list of numerical values to the CSV file
                writer.writerow(values)
                print(counter)
                counter += 1

ls = startScrape()
ls.scrape()
