import time
# import pandas as pd
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException,NoSuchElementException, NoSuchWindowException ,TimeoutException

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get('https://www.vancaraccessories.com.au/')

################################# It will store the Href links of pages #############################
Numberofpages = []
def pages():
    try:
        page = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="Content"]/div/div[1]/div/div/div/div/div[3]/div/div/a')))
        for page in page:
            href = page.get_attribute('href')
            Numberofpages.append(href)
            # print(href)   
    except:
        Numberofpages.clear()
        # print(len(Numberofpages))
      
################################# Function to scrape products from the websites #############################
listofproducts = []
def products():
    try:
        products = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="Content"]/div/div[1]/div/div/div/div/div[2]/ul/li/div[2]/h4/a')))
        for pro in range(len(products)):
            listofproducts.append([products[pro].text])
            print(products[pro].text)
    except:
        pass
    pages()
    if len(Numberofpages) != 0:
        for page in range(len(Numberofpages)):
            driver.get(Numberofpages[page])
            products = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="Content"]/div/div[1]/div/div/div/div/div[2]/ul/li/div[2]/h4/a')))
            for pro in range(len(products)):
                listofproducts.append([products[pro].text])
                print(products[pro].text)
            products = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="Content"]/div/div[1]/div/div/div/div/div[2]/ul/li/div[2]/h4/a')))

################################# Function to scrape data of all child categories #############################

def Child_cat():
    # import pdb;pdb.set_trace()
    try:
        child_cat = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="woocommerce_product_categories-3"]/ul/li/ul/li/a')))
        for a in range(len(child_cat)):
            print('------------------------------------Child Category----------------------------------')
            print(child_cat[a].text)
            href = child_cat[a].get_attribute('href')
            driver.get(href)
            products()
            driver.back()
            child_cat = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="woocommerce_product_categories-3"]/ul/li/ul/li/a')))
    except:
        pass
# ################################# Scrape products by category  #############################
def ScrappingData():
    
    # click on "view all services" button
    view_all_categories = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="Content"]/div/div/div/div[1]/div/div/div[6]/div/div/div/div/a'))).click()
    # import pdb;pdb.set_trace()
    try:
        
        # fetch links of all category and looping through it
        parent_cat = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="woocommerce_product_categories-3"]/ul/li/a')))
        for url in range(len(parent_cat)):
            href = parent_cat[url].get_attribute('href')
            print(parent_cat[url].text," Link :- ",href )
            driver.get(href)
           # calling above mentioned function(products) to get products
            products()
            Child_cat()
          # click on back to  fetch  next category 
            driver.back() 
            parent_cat = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="woocommerce_product_categories-3"]/ul/li/a')))
    except StaleElementReferenceException:
        parent_cat = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="woocommerce_product_categories-3"]/ul/li/a')))
    except TimeoutException:
        print('Products not found')
            
ScrappingData()
print(listofproducts)
driver.implicitly_wait(30)
driver.quit()

################################# Convert list of products into xlsx formate #############################
with xlsxwriter.Workbook('Vancaraccessories_Data.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(listofproducts):
        worksheet.write_row(row_num, 0, data)

