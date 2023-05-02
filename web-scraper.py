# The user will be prompted to enter the site URL,
# and the tag that they want to scrape
# The script will then send the request to the URL,
# extract all the isntances of said tag using bs4,
# and print the scraped tags.

# Install dependencies:
# pip install requests
# pip install beautifulsoup4

# To run:
# python3 web_scraper.py


import requests
from bs4 import BeautifulSoup

# Prompt the user for the website URL and the HTML tag to scrape
url = input("Enter website URL: ")
tag = input("Enter HTML tag to scrape: ")

# Send a request to the specified URL and extract the specified HTML tag
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.find_all(tag)

# Print out the scraped items
for item in items:
    print(item)
