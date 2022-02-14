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

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get('https://www.sparesbox.com.au/')
# url1 = 'https://www.sparesbox.com.au/parts/engine-cooling-and-drivetrain/ignition-system/spark-plugs'
# driver.get(url1)

listofproducts = []

# Fetch data from multiple pages 
def Pagination():
    while True:
        try:
            products = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//h3[@class="d-block text-lh-15 text-norm mb-2 link-black font-size-0875"]')))
            prices = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="mrYXhWQ1NvGGf4FITjFfX"]')))
            for pro in range(len(products)):
                for price in range(pro,pro+1):
                    listofproducts.append([products[pro].text,prices[price].text])
                    print(products[pro].text,"  ",prices[price].text)
                    driver.implicitly_wait(1)
            
            # click on page until the last page reached
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[not(@class="disabled")]/div[contains(text(), "Next")]'))).click()
            products = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//h3[@class="d-block text-lh-15 text-norm mb-2 link-black font-size-0875"]')))
        except StaleElementReferenceException:
            products = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//h3[@class="d-block text-lh-15 text-norm mb-2 link-black font-size-0875"]')))
        
        # if page not found after reaching to last page it will break the loop and continue for the next category
        except TimeoutException:
            break
       
# scrape products info related to particular category
def ScrappingData():
    try:
        categories = WebDriverWait(driver,80).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="_2pTXRywXUaZ8eGlpjez8lJ"]')))
        for cat in range(len(categories)):
            print(categories[cat].text)

            # Get urls of all category 
            urls =WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class="u-url _1LGSLL1b9hC6jf9mbBwlG8 border-0 text-center d-block bg-white p-4 text-cnd h-100"]')))
            for url in range(cat,cat+1):
                my_href = urls[url].get_attribute('href')
                print(my_href)
                driver.get(my_href)
                Pagination()
                driver.back()           
    except StaleElementReferenceException:
        categories = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="_2pTXRywXUaZ8eGlpjez8lJ"]')))


ScrappingData()
# Pagination()
# driver.quit()

with xlsxwriter.Workbook('Spark_Club_Data.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(listofproducts):
        worksheet.write_row(row_num, 0, data)


