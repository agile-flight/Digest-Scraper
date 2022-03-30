import requests
from bs4 import BeautifulSoup
from digest_list import site_url_list, freshman_roster

def search_site(item, site):

	web_data = requests.get(site).content
	soup = BeautifulSoup(web_data, "html.parser")
	text_list = soup.get_text().split(" ")

	if item in text_list:
		return f"{site} includes name, {item}"
	else:
		return "\033[F"

if __name__ == "__main__": 
	for site in site_url_list:
		for name in freshman_roster:
			print(search_site(name, site))