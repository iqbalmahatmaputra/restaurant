from selenium import webdriver
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient
import certifi

password = 'iqbalmp'
cxn_str = f'mongodb+srv://iqbalmp:{password}@cluster0.ligsrx6.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(cxn_str, tlsCAFile=certifi.where())
db = client.dbsparta_plus_week3

driver = webdriver.Chrome('./chromedriver')

url = "https://www.yelp.com/search?cflt=restaurants&amp;find_loc=San+Francisco%2C+CA"

driver.get(url)
time.sleep(5)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
time.sleep(5)

req = driver.page_source
driver.quit()

soup = BeautifulSoup(req, 'html.parser')
restaurants = soup.select('div[class*="arrange-unit__"]')
for restaurant in restaurants:
    business_name = restaurant.select_one('div[class*="businessName__"]')
    if not business_name:
        continue
    name = business_name.text
    categories_price_location = restaurant.select_one(
        'div[class*="priceCategory__"]')
    spans = categories_price_location.select('span')
    categories = spans[0].text
    location = spans[-1].text
    print(name, ',', categories, ',', location)
