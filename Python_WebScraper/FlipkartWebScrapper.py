# Requirements
from time import sleep
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import StaleElementReferenceException,NoSuchElementException, TimeoutException, WebDriverException


# CHROME driver installation
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


# lists of links
sub_cat_1 = []
sub_cat_2 = []
Products_list = []

def BaseFunc():
    # launch URL
    driver.get('https://www.flipkart.com/')
    # identify Element
    close_login_page = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="_2KpZ6l _2doB4z"]'))).click()
    HoverOnCategory()

# funtion to create hover action 
def HoverOnCategory():
    explore_cat = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH,'//a[@class= "_21ljIi"]')))
    # Get url of above element
    link = explore_cat.get_attribute('href')
    driver.get(link)
    # identify Element
    super_cat = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class= "_1kidPb"]/span')))
    for cat in range(len(super_cat)):
        print(super_cat[cat].text)
        #object of ActionChains
        a = ActionChains(driver)
        #hover over element
        a.move_to_element(super_cat[cat]).perform()
        # calling function 
        Level1SubCategory()

def Level1SubCategory():
    # identify Element
    sub_Cat = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class = "_3QN6WI _1MMnri _32YDvl"]')))
    for cat in range(len(sub_Cat)):
        # Get url of above element
        link = sub_Cat[cat].get_attribute('href')
        # store link in list
        sub_cat_1.append(link)
        print("     ",sub_Cat[cat].text)
    Level2SubCategory()   

def Level2SubCategory():
    # identify element
    sub_cats = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.XPATH,'//a[@class = "_3QN6WI"]')))
    for cat in range(len(sub_cats)):
        # store links in list 
        link = sub_cats[cat].get_attribute('href')
        sub_cat_2.append(link)
        print("         ",sub_cats[cat].text)  


# calling base function first to create list of level-2 subcategory 
BaseFunc()
   
def Products():
    # import pdb;pdb.set_trace()
    for i in range(len(sub_cat_2)):
        cat = sub_cat_2[i]
        # open sub category in new tab 
        driver.execute_script('window.open("{}","_blank");'.format(cat))
        # switch window to last opened 
        driver.switch_to.window(driver.window_handles[-1])
        try:
            # check those products which matches the below attribute value (using Or operator)
            page = WebDriverWait(driver,50).until(EC.presence_of_element_located((By.XPATH,'//div[@class = "_2MImiq"]/span[1]'))).text
            a = page.index('of')
            s = page[a+3:]
            # get total number of pages 
            total_pages = int(s)
            i=1
            for i in range(total_pages):
                # print current page number
                print("########## page : ",i+1," ############")
                cmplt_url = cat +"&page="+str(i+1)
                driver.get(cmplt_url)
                # check product element exists or not
                try:
                    product1 = WebDriverWait(driver, 20).until(lambda x: (x.find_elements(By.XPATH,'//div[@class = "_4rR01T"]'), x.find_elements(By.XPATH,'//a[@class ="s1Q9rs"]')))
                    for pro in product1:
                        # store products in the list 
                        for i in pro:
                            Products_list.append(i.text)
                            print("        ",i.text)
                except:
                    pass
        except:
            product1 = WebDriverWait(driver, 20).until(lambda x: (x.find_elements(By.XPATH,'//div[@class = "_4rR01T"]'), x.find_elements(By.XPATH,'//a[@class ="s1Q9rs"]')))
            for pro in product1:
                # store products in the list 
                for i in pro:
                    Products_list.append(i.text)
                    print("        ",i.text)     
        # after fetching products from above links switch active window to previous one.  
        driver.switch_to.window(driver.window_handles[0])
Products()  
print(Products_list)
# after executing whole code quit driver .
driver.quit()

################################# Convert list of products into xlsx formate #############################
with xlsxwriter.Workbook('Myntra_Data.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, data in enumerate(Products_list):
        worksheet.write_row(row_num, 0, data)

