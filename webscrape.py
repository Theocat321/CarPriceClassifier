#---------------------------------------------------------------------#
# File: c:\Adam\Coding\CarPriceClassifier\webscrape.py
# Project: c:\Adam\Coding\CarPriceClassifier
# Created Date: Friday, February 11th 2022, 11:55:38 am
# Description: 
# Author: Adam O'Neill
# Copyright (c) 2022 Adam O'Neill
# -----
# Last Modified: Sun Mar 06 2022
# Modified By: Adam O'Neill
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
# 2022-03-06	AO	Added getting infomaion about each car. This can be optimised using an array and checking if data taken in matches what is expected. Often a part of the array is missing which messes up the data. This might be okay in a large sample size, unsure
#---------------------------------------------------------------------#
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


def getData():

    # open a client link

    uClient = uReq("https://www.autotrader.co.uk/car-search?postcode=AL55RE&make=Audi&model=A1&include-delivery-option=on&advertising-location=at_cars&page=1")

    html_page = uClient.read()

    # Creates a soup data type
    page_soup = soup(html_page,"html.parser")

    # Creates an array of all the seach results div with info in
    search_results = page_soup.find_all("div",{"class":"product-card-content"})
    
    # opens csv file in write mode
    CarDataCsv = open("A1Data.csv","w")

    # Initalise headings
    Headers = "Make / Model, Price, Year, Type, Miles, Engine Size, BHP, Transmittion type, Fuel type"
    CarDataCsv.write(Headers)

    for x in range(len(search_results)-1): 
        
        # get the price of the car (Label)
        cPrice = search_results[x].section.div.div.text.replace(",","").strip()

        # Gets all the details of the car
        cCarDetailsArray = search_results[x].find_all("section") # [1]
        
        # Make and model
        cMakeModel = cCarDetailsArray[1].h3.text.strip()
        
        #
        cCarDetailsLi = cCarDetailsArray[1].ul.find_all("li")

        # Year registered
        cYear = cCarDetailsLi[0].text[0:4].strip()

        # Car type
        cType = cCarDetailsLi[1].text.strip()

        # Miles
        cMiles = cCarDetailsLi[2].text.replace(",","").strip()

        # Engine size
        cEngSize = cCarDetailsLi[3].text.strip()

        #BHP
        cBHP = cCarDetailsLi[4].text.strip()

        # transmition type
        cTrans = cCarDetailsLi[5].text.strip()

        # Fuel type
        cFuel = cCarDetailsLi[6].text.strip()


        #check if data is correct or not
        for x in range(9):


        # Add to csv
        CarDataCsv.write("\n"+cMakeModel+","+cPrice+","+cYear+","+cType+","+cMiles+","+cEngSize+","+cBHP+","+cTrans+","+cFuel)

    CarDataCsv.close()




def main():
    getData()

main()


## PLAN
# Get all the data from auto trader and store in csv (Audi A1)
# Open the csv and clean data and create classification model - in jupyter notebook
# Take user inputs and output expected price for car