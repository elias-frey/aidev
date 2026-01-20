# A simple web scraper for real estate listings in Europe
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_real_estate(url):
    response = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0"
    })

    soup = BeautifulSoup(response.text, "html.parser")

    listings = []

    # Example HTML patterns (works for most EU listing pages)
    items = soup.select(".resultItem, article, .list-item, .card")  

    for item in items:
        title = item.select_one("h2, h3, .title")
        price = item.select_one(".price, .result-price, .ad-price")
        details = item.select_one(".details, .result-details, ul")

        listings.append({
            "title": title.get_text(strip=True) if title else None,
            "price": price.get_text(strip=True) if price else None,
            "details": details.get_text(strip=True) if details else None,
            "url": item.select_one("a")["href"] if item.select_one("a") else None
        })

    return listings


# TEST on a real page (replace with your target):
url = "https://www.immowelt.de/liste/berlin/wohnungen/mieten"
data = scrape_real_estate(url)

df = pd.DataFrame(data)
print(df)

# Dynamic scraping with Selenium (if needed)
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd

def scrape_real_estate_dynamic(url):
    driver = uc.Chrome()
    driver.get(url)
    time.sleep(5)  # wait for JS to load

    items = driver.find_elements(By.CSS_SELECTOR, "article, .resultItem, .card")

    listings = []

    for item in items:
        try:
            title = item.find_element(By.CSS_SELECTOR, "h2, h3").text
        except:
            title = None
        
        try:
            price = item.find_element(By.CSS_SELECTOR, ".price, .ad-price").text
        except:
            price = None
        
        try:
            link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        except:
            link = None

        listings.append({
            "title": title,
            "price": price,
            "url": link
        })

    driver.quit()
    return listings


# Example:
url = "https://www.immobilienscout24.de/Suche/de/berlin/wohnung-mieten"
df = pd.DataFrame(scrape_real_estate_dynamic(url))
print(df)

# Scrapping hidden JSON APIs
import requests
import pandas as pd

url = "https://www.immowelt.de/api/search/list?location=Berlin&estateType=flatRent"

data = requests.get(url).json()

df = pd.DataFrame(data["estates"])
print(df.head())

# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

import requests
from bs4 import BeautifulSoup
def scrape(): 
    url = 'https://www.example.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # Add your scraping logic here
    title = soup.select_one('h1').text
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href')
    print(title)
    print(text)
    print(link)
if __name__ == '__main__':
    scrape()

