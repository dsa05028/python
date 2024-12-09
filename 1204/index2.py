#selenium

'''from selenium import webdriver #파일명을 selenium으로하면 모듈로 인식

driver=webdriver.Chrome()
driver.get("https://www.naver.com/")
driver.title'''

#chrome으로 naver 불러오기
''''from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

driver.get("https://www.naver.com")'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window() #큰 창으로 열림

driver.get("https://www.naver.com")
