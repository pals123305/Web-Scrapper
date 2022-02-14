from re import escape
from selenium import webdriver
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import xlsxwriter
import time
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException,NoSuchElementException, NoSuchWindowException ,TimeoutException

from Ner import ScrappingData

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get('https://www.newcastleprosound.com.au/')
# driver.get('https://www.newcastleprosound.com.au/product-category/car-audio-visual/')

list_of_main_category = []
first_category_url = []
second_category_url = []
third_category_url = []
number_of_pages_of_second_cat = []
number_of_pages_of_third_cat = []


def FirstCat():
    parent_cat = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="elementor-column-wrap elementor-element-populated"]/div/div[2]/div/h2/a')))
    # import pdb;pdb.set_trace()
    try:
        print("***** First Category ****** \n ")
        for url in range(len(parent_cat)):
            href = parent_cat[url].get_attribute('href')
            first_category_url.append(href)
            print(parent_cat[url].text)
            driver.get(href)
            SecondCategory()
            driver.back()
            parent_cat = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="elementor-column-wrap elementor-element-populated"]/div/div[2]/div/h2/a')))
        print(" \n ***** End First Category ****** ")
    except StaleElementReferenceException:
        parent_cat = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//div[@class="elementor-column-wrap elementor-element-populated"]/div/div[2]/div/h2/a')))
    except TimeoutException:
        print('Products not found')

def SecondCategory():
    print("***** Second Category ****** \n ")
    # import pdb;pdb.set_trace()
    try :
        sec_cat =WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//ul[@class="products elementor-grid columns-3"]/li/a/h2'))) 
        sec_cat_url =WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//ul[@class="products elementor-grid columns-3"]/li/a')))
        for cat in range(len(sec_cat)):
            print("       ",sec_cat[cat].text)
            href = sec_cat_url[cat].get_attribute('href')
            second_category_url.append(href)      
    except:
        pass
def ThirdCategory():
    # import pdb;pdb.set_trace()
    for i in range(len(second_category_url)):
        print(second_category_url[i])
        driver.get(second_category_url[i])
        try:
            third_Cat = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//ul[@class="products elementor-grid columns-3"]/li/a/h2')))
            for cat in range(len(third_Cat)):
                print("             ",third_Cat[cat].text)
            while True:
                WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//a[@class = "next page-numbers"]'))).click()
                third_Cat = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//ul[@class="products elementor-grid columns-3"]/li/a/h2')))
                for cat in range(len(third_Cat)):
                    print("             ",third_Cat[cat].text)
        except:
            pass

FirstCat()
print(first_category_url)
print(second_category_url)
ThirdCategory()
driver.quit()

