import requests
from bs4 import BeautifulSoup
from digest_list import site_url_list, freshman_roster

if len(freshman_roster) == 0:
	print("you cannot access the freshman roster for security reasons".upper())

def date(site):

	month = g_text(site, True)[45]
	day = g_text(site, True)[46]
	year = g_text(site, True)[47]

	return month + " " + day + " " + year[:4]

def g_text(site, strip):

	web_data = requests.get(site).content
	soup = BeautifulSoup(web_data, "html.parser")
	return soup.get_text(strip = strip).split(" ")

	g_text(site)

if __name__ == "__main__": 
	
	names = []

	for site in site_url_list:
		for name in freshman_roster:
			if name in g_text(site, False):
				names.append(name)

		names = ", ".join(names)

		if len(names) != 0:
			print(f"\nURL: {site}\nDate: {date(site)}\nContains name(s): {names}")

		names = []

	print()
