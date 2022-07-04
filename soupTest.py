from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
# import urllib.request as urllib2
#import re
import time

def get_Text():
	# options = webdriver.ChromeOptions()

	# options.add_argument('--ignore-certificate-errors')
	option = webdriver.ChromeOptions()
	option.add_argument('--ignore-certificate-errors')
	option.add_argument('--incognito')
	#ption.add_argument('--headless')
	driver = webdriver.Chrome(executable_path="/home/clark/Downloads/chromedriver_linux64/chromedriver", options=option)
	driver.get(
		'https://www.usaswimming.org/times/otherorganizations/ncaa-division-i')
	time.sleep(5)
	button = driver.find_element(By.ID, 'Content_LegacyFeature_Index_Div-2-Link')
	button.click()
	time.sleep(10)
	driver.switch_to.frame(3)
	s = driver.page_source
	soup = BeautifulSoup(s, 'lxml')
	print(soup.prettify())

	subBut = driver.find_element(By.CSS_SELECTOR, "input[type='submit'")
	time.sleep(5)
	subBut.click()
	time.sleep(8)
	page_source = driver.page_source

	'''soup = BeautifulSoup(page_source, 'lxml')
	namelist = soup.find_all('a', href=re.compile("swimm"))
	timelist = soup.find_all('a', href=re.compile("time"))'''

	'''pairlist = []
	for a in range(50):
		pairlist.append((namelist[a].string, timelist[a].string))
	print(pairlist)'''

