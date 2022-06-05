import requests
import os.path
import pandas as pd
from bs4 import BeautifulSoup

def date(site):                                                                                                   # Returns date of passed website #
	text = g_text(site, False).split()

	month = text[54]
	day = text[55]
	year = text[56]

	return month + " " + day + " " + year[:4]

def g_text(site, strip):                                                                                          # Returns all the text of passed website as a string #
	web_data = requests.get(site).content
	soup = BeautifulSoup(web_data, "html.parser")
	return soup.get_text(strip = strip)

if __name__ == "__main__": 

	if os.path.exists('freshman_roster.xlsx') and os.path.exists('digest_webpages.xlsx'):                        #If these files exist on the path
		names_df = pd.read_excel('freshman_roster.xlsx')								                         #Read xlsx files
		webpages_df = pd.read_excel('digest_webpages.xlsx') 

		freshman_roster = names_df['Full Name'].to_list()								                         # Make a list out of one of the collumns 
		digest_webpages = webpages_df['URL'].to_list()
	else:
		print("You are missing one or both excel sheets required to run the program")
		quit()
		
	f = open("results.txt", "w")
	names = []
	names_complete = set()

	for site in digest_webpages:            											                         # Iterate though list of daily digest webpage URLs to checkk all webpages #
		text = g_text(site, True)

		for name in freshman_roster:                                                                             # Iterate though all names on the freshman roster to check webpages for those names #
			if name in text: 
				names.append(name)                                                                               # Add Name to list that shows the names found on one site so we may store it later #
				names_complete.add(name)                                                                         # Add Name to list of total names found on all webpages so we may store it later #

		found_names = ", ".join(set(names)) 
		if names:
			f.write(f"URL: {site}\nDate: {date(site)}\nContains name(s): {found_names}")

			counter = [names.count(name) for name in names]                                                      # Make another list which's numbers correlate he number of occrances of a name of the same index #
			repetition = any(i > 1 for i in counter)															 # Check if a certain name occures more than one time in the list, names"

			if repetition:                                                                                       # Make a notice if there is any repetition in the list, names #
				f.write("\nNotice: ")

			for name in names:
				if names.count(name) > 1:
					f.write(f"{name} is mentioned {names.count(name)} times. ")

				for i in range(0, names.count(name)):
					names.remove(name)
			
			f.write("\n\n")


		
		names = []                                                                                               # Clear list of names found on one site to prepare list of names found on next site #
		print(f"- - - Scanning Digest {digest_webpages.index(site) + 1} of {len(digest_webpages)} - - -\033[F")  # Progress Report that is sent on Console #

	names_complete = ", ".join(names_complete) 
	f.write(f"\nName(s) Mentioned on Digests:\n{names_complete}") 

	print("Program Completed                          ")
	f.close()

	
