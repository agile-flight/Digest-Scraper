import requests
from bs4 import BeautifulSoup
from digest_list import site_url_list, freshman_roster

def date(site):

	text = g_text(site, False).split()

	month = text[54]
	day = text[55]
	year = text[56]

	return month + " " + day + " " + year[:4]

def g_text(site, strip):

	web_data = requests.get(site).content
	soup = BeautifulSoup(web_data, "html.parser")
	return soup.get_text(strip = strip)

if __name__ == "__main__": 

	f = open("results.txt", "w")

	names = set()
	names_complete = set()

	for site in site_url_list:

		text = g_text(site, True)

		for name in freshman_roster:
			if name in text:
				names.add(name)
				names_complete.add(name)

		names = ", ".join(names)

		if len(names) != 0:
			f.write(f"\nURL: {site}\nDate: {date(site)}\nContains name(s): {names}\n")
		
		names = set()

		print(f" Scanning Digest {site_url_list.index(site) + 1} of {len(site_url_list)}\033[F")

	names_complete = ", ".join(names_complete)
	f.write(f"\n\nName(s) Mentioned on Digests:\n{names_complete}")

	print("Program Completed          ")
	f.close()

	
