# Web_Scrapper
## What is Web Scraping? Is Web Scraping Legal? <br/>
Web scraping is an automated method used to extract large amounts of data from websites. The data on the websites are unstructured. Web scraping helps collect these unstructured data and store it in a structured form. There are different ways to scrape websites such as online Services, APIs or writing your own code.<br/>
Let's say you find data from the web, and there is no direct way to download it, web scraping using Python is a skill you can use to extract the data into a useful form that can be imported. <br/>
![This is an image](https://miro.medium.com/max/700/1*iCfjkob5ZqXhGt-AAcmlGA.jpeg) <br/>
Talking about whether web scraping is legal or not, some websites allow web scraping and some don’t. To know whether a website allows web scraping or not, you can look at the website’s “robots.txt” file. You can find this file by appending “/robots.txt” to the URL that you want to scrape. For this example, I am scraping Flipkart website. So, to see the “robots.txt” file, the URL is www.flipkart.com/robots.txt.## Why Web Scraping? <br/>
Web scraping is used to collect large information from websites. But why does someone have to collect such large data from websites? To know about this, let’s look at the applications of web scraping: <br/>
***Price Comparison***: Services such as ParseHub use web scraping to collect data from online shopping websites and use it to compare the prices of products. <br/>
***Email address gathering***: Many companies that use email as a medium for marketing, use web scraping to collect email ID and then send bulk emails. <br/>
***Social Media Scraping***: Web scraping is used to collect data from Social Media websites such as Twitter to find out what’s trending. <br/>
***Research and Development***: Web scraping is used to collect a large set of data (Statistics, General Information, Temperature, etc.) from websites, which are analyzed and used to carry out Surveys or for R&D.<br/>
***Job listings***: Details regarding job openings, interviews are collected from different websites and then listed in one place so that it is easily accessible to the user.<br/>
## How does Web Scraping work? <br/>
When you run the code for web scraping, a request is sent to the URL that you have mentioned. As a response to the request, the server sends the data and allows you to read the HTML or XML page. The code then, parses the HTML or XML page, finds the data, and extracts it.
To extract data using web scraping with python, you need to follow these basic steps: <br/>
1. Find the URL that you want to scrape <br/>
2. Inspecting the Page <br/>
3. Find the data you want to extract <br/>
4. Write the code <br/>
5. Run the code and extract the data <br/>
6. Store the data in the required format <br/>
## Libraries used for Web Scraping <br/>
As we know, Python is used for various applications and there are different libraries for different purposes. In our further demonstration, we will be using the following libraries: <br/>
***Selenium***: Selenium is a web testing library. It is used to automate browser activities. <br/>
***WebDriver-Manager***: WebDriverManager is an API that allows users to automate the handling of driver executables like chromedriver.exe, geckodriver.exe etc. <br/>
***xlswriter***: XlsxWriter is a Python module that can be used to write text, numbers, formulas and hyperlinks to multiple worksheets in an Excel 2007+ XLSX file.
<hr style="border:2px solid gray"> </hr>



