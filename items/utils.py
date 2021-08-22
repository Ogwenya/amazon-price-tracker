import requests
from bs4 import BeautifulSoup
import lxml

headers = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
	"Accept-Language": "en"
}

def get_data(url):
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.text, "lxml")

	name = soup.select_one(selector="#productTitle").getText().strip()
	price = float(soup.select_one(selector="#priceblock_ourprice").getText().strip()[1:])
	
	return name, price