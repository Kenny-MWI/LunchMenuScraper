"""
This script scrapes the lunch menu PDF file from the Joplin Schools Nutrition Services
website and downloads it to your local machine.
"""

import urllib
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up the Chrome driver with options to run headless
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# Send a GET request to the URL
driver.get('https://www.joplinschools.org/departments/nutrition_services/menus')
driver.implicitly_wait(10)

html = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML content of the page
soup = BeautifulSoup(html, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

print('Here are all the menu links on the page:')

# Loop through the links and find the one that contains the word you're looking for
for link in links:
    if 'Middle' in link.get('href') and '.pdf' in link.get('href') and \
        'Menu' in link.get('href') and ('2023' in link.get('href') or '2024' in link.get('href')):

        print(link)
        print('\n')

        # Get the URL of the PDF file
        pdf_url = link.get('href')

        # Replace the space character with %20
        pdf_url = pdf_url.replace(' ', '%20')
        # pdf_url = urljoin('https://www.joplinschools.org', pdf_url)
        pdf_url = urljoin('https://cdnsm5-ss11.sharpschool.com', pdf_url)

        print('PDF_URL: ' + pdf_url)
        print('\n')

        # Download the PDF file
        import os

        filename = os.path.basename(pdf_url)

        try:
            urllib.request.urlretrieve(pdf_url, filename)
        except urllib.error.HTTPError as e:
            print('Error downloading file: ' + str(e.code))
            print('Response text: ' + e.read().decode('utf-8'))
            sys.exit(1)

        # Exit the loop
        # break
