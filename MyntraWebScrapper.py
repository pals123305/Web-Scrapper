# Requirements
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, WebDriverException


# CHROME driver installation
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


# lists of links
sub_cat_1 = []
sub_cat_2 = []

def BaseFunc():
    # launch URL
    driver.get('https://www.flipkart.com/')
    # identify Element
    close_login_page = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="_2KpZ6l _2doB4z"]'))).click()
    MainCategory()

def MainCategory():
    import pdb;pdb.set_trace()
    explore_cat = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//a[@class= "_21ljIi"]')))
    # Get url of above element
    link = explore_cat.get_attribute('href')
    driver.get(link)
    super_cat = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class= "_1kidPb"]/span')))
    for cat in range(len(super_cat)):
        print(super_cat[cat].text)
        #object of ActionChains
        a = ActionChains(driver)
        #hover over element
        a.move_to_element(super_cat[cat]).perform()
        sub_Cat = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class = "_3QN6WI _1MMnri _32YDvl"]')))
        for cat in range(len(sub_Cat)):
            sub_cat_1.append(sub_Cat[cat].text)
            print("     ",sub_Cat[cat].text)
            sub_Cat_2 = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class = "_3QN6WI"]')))
            for cat in range(len(sub_Cat_2)):
                print(sub_Cat_2[cat].text)

# def SubCategory1():
#     sub_Cat = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class = "_3QN6WI _1MMnri _32YDvl"]')))
#     for cat in range(len(sub_Cat)):
#         sub_cat_1.append(sub_Cat[cat].text)
#         print("     ",sub_Cat[cat].text)
#         SubCategory2()

# def SubCategory2():
#     import pdb;pdb.set_trace()
#     # launch URL
#     # driver.get('https://www.flipkart.com/plus')
#     sub_Cat = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class = "_3QN6WI"]')))
#     for cat in range(len(sub_Cat)):
#         print(sub_Cat[cat].text)



BaseFunc()
# SubCategory2()
driver.quit()