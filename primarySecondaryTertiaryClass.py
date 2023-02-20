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
        file = open("SecondaryPrimaryCellClass.csv", "w")
        writer = csv.writer(file)
        writer.writerow([    "NeuroMorpho.Org ID",    "Cell Name",    "Archive Name",    "Species Name",    "Strain",    "Structural Domains",    "Physical Integrity",
                             "Morphological Attributes",    "Min Age",    "Max Age",    "Gender",    "Min Weight",    "Max Weight",    "Development",    "Primary Brain Region",
                             "Secondary Brain Region",    "Tertiary Brain Region",    "Primary Cell Class",    "Secondary Cell Class",    "Tertiary Cell Class",    "Original Format",
                             "Experiment Protocol",    "Experimental Condition",    "Staining Method",    "Slicing Direction",    "Slice Thickness",    "Tissue Shrinkage",
                             "Objective Type",    "Magnification",    "Reconstruction Method",    "Date of Deposition",    "Date of Upload",    "Persistence Vector"])
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
                # for element in neuron[0].text.split("\n"):
                #     print(element)
                for element in neuron[0].text.split("\n"):
                    if element != "Details about selected cell":
                        # remove the unit from the element and append the numerical value to the list
                        value = element.split(":")[1].strip().replace(" μ", "")
                        try:
                            values.append(value)
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
