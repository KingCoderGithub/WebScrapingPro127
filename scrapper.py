from time import time
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

# URl
start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/amarshah/Desktop/WebScrappingPro127/chromedriver")
browser.get(start_url)
time.sleep(10)

headers = ["Name", "Distance", "Mass", "Radius"]
planetsData = []

def scrap() :
    for i in range (0, 201) :
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for tr_tag in soup.find_all("tr", attrs = {"class" : "expolanet"}):
            td_tags = tr_tag.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags) :
                if index == 0 :
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else :
                    try :
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
                        planetsData.append(temp_list)
  
scrap()
with open("Planets.csv", "W")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetsData)
