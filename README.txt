------------------------------------------------------------------------------------------
Disk Scraper
------------------------------------------------------------------------------------------

AUTHOR:
agile-flight

PURPOSE:
Search for names of freshmen present present on my schools online daily blog.

MODULES USED:
Excel files with entire freshman roster and list of webpages are processed 
using Pandas. Text is gathered from all webpages using Beautiful Soup.

DATE OF CREATION:
2022

HOW TO ACCESS:
After downloading files

1. Make sure you have python 3, pandas and beautiful soup installed on your system.

2. Place excel files with freshman roster at the same path as main.py. The excel file
should be titled "freshman_roster.xlsx" and should have 1 collumn with all full names of 
freshmen, titled, "Full Name".

3. Place excel file with all blog urls at the same path as main.py. The excel file should 
be titled "digest_webpages.xlsx" and should have 1 collumn with all URLs of all blogposts
you would like check for freshman names.

4. IN WINDOWS, open command prompt and navigate to the path of main.py . Then run main.py
using the "python" keyword.

IN LINUX/MACOS, open terminal and navigate to the path of main.py . Then run main.py
using the "python3" keyword.
