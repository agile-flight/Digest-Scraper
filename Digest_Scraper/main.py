import requests
from bs4 import BeautifulSoup
from digest_list import digest_webpages, freshman_roster

def date(site): # Returns date of passed website #

	text = g_text(site, False).split()

	month = text[54]
	day = text[55]
	year = text[56]

	return month + " " + day + " " + year[:4]

def g_text(site, strip):                    # Returns all the text of passed website as a string #

	web_data = requests.get(site).content
	soup = BeautifulSoup(web_data, "html.parser")
	return soup.get_text(strip = strip)


if __name__ == "__main__": 

	f = open("results.txt", "w")

	names = []
	names_complete = set()

	for site in digest_webpages:            # Iterate though list of daily digest webpage URLs to checkk all webpages#

		text = g_text(site, True)

		for name in freshman_roster:        # Iterate though all names on the freshman roster to check webpages for those names#
			if name in text: 
				names.append(name)          # Add Name to list that shows the names found on one site so we may store it later #
				names_complete.add(name)    # Add Name to list of total names found on all webpages so we may store it later #

		names = ", ".join(names) 

		if names:
			f.write(f"\nURL: {site}\nDate: {date(site)}\nContains name(s): {names}\n")
		
		names = []                          # Clear list of names found on one site to prepare list of names found on next site#

		print(f"- - - Scanning Digest {digest_webpages.index(site) + 1} of {len(digest_webpages)} - - -\033[F") # Progress Report that is sent on Console#

	names_complete = ", ".join(names_complete) 

	f.write(f"\n\nName(s) Mentioned on Digests:\n{names_complete}") 

	print("Program Completed                          ")
	f.close()

	
