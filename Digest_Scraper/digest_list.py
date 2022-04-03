import os.path
import pandas as pd

if os.path.exists('freshman_roster.xlsx') and os.path.exists('digest_webpages.xlsx'):             #If these files exist on the path
	names_df = pd.read_excel('freshman_roster.xlsx')		                          #Read xlsx files
	webpages_df = pd.read_excel('digest_webpages.xlsx') 
	
	freshman_roster = names_df['Full Name'].to_list()				          #Make a list out of one of the collumns
	digest_webpages = webpages_df['URL'].to_list()

else:
	print("You are missing one or both excel sheets required to run the program")
	quit()


