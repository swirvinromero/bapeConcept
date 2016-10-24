import requests
from bs4 import BeautifulSoup
import userData as ui
from selenium import webdriver
import time



def commands():

	print "Hello" + ui.myName
	#search
	print '\n\n' + "Searching....."
	findLink( ui.wordSearch, ui.colorSearch)

	#execute
	print '\n\n' +"Executing...."
	navigateTo(ui.gold)
	#confirm


def findLink(word, color):

	categories = ["men", "collaboration", "men/FOOTWEAR", "frontpage"]
	master_url = ""
	while master_url == "":
		
		for cat in categories:
			if master_url !="":
				break
			page = 1
			max_pages = 5
			while page <= max_pages:
				url = 'http://us.bape.com/collections/' + cat + '?page=' + str(page)
				print '\n\n' + url
				source_code = requests.get(url)
				plain_text = source_code.text
				soup = BeautifulSoup(plain_text, "html.parser")
				for link in soup.find_all('a', class_="EachThumb"):
					print link.get("title")
					if ( color in link.get("title") and word in link.get("title")):
						print "Found!!! http://us.bape.com" + link.get("href")
						print link.get("title")
						page = max_pages +1
						master_url = "http://us.bape.com" + link.get("href")
						break
				x = soup.find_all('li', class_="next disabled")
				if (x):
					print "Null"
					break
				else:
					page +=1

	ui.gold = master_url



def navigateTo(master_url):
	print "url: " + master_url

	driver = webdriver.Firefox()
	driver.get(master_url)
	grabItem(driver, ui.cwSize)

def grabItem(driver, itemSize):
	selectSize = driver.find_element_by_id("product-select")
	for option in selectSize.find_elements_by_tag_name("option"):
		if(option.text == itemSize):
			option.click()
			break
	toCart = driver.find_element_by_xpath("//input[@value='Add to Cart']")
	toCart.click()
	print "1sec"
	time.sleep(1)
	checkItOut = driver.find_element_by_xpath("//input[@value='Proceed to Checkout']")
	checkItOut.click()






commands()

#driver.Firefox()
#driver.get("http://us.bape.com/collections/frontpage")




