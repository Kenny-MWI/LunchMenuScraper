# Lunch Menu Scraper

[![Pylint](https://github.com/Kenny-MWI/LunchMenuScraper/actions/workflows/pylint.yml/badge.svg)](https://github.com/Kenny-MWI/LunchMenuScraper/actions/workflows/pylint.yml)

This script scrapes the lunch menu PDF file from the Joplin Schools Nutrition Services website and downloads it to your local machine. This site uses a CDN which attempts to prevent automated scraping which may break this script. Some tweaks may be required to make it work.

## Installation

1. Clone the repository to your local machine.
2. Install the required Python packages using pip: `pip install -r requirements.txt`
3. Maybe download and install the Chrome web driver from https://sites.google.com/a/chromium.org/chromedriver/downloads
4. Maybe update the `CHROME_DRIVER_PATH` variable in `LunchMenuScraper.py` to point to the location of the Chrome web driver on your machine.

## Usage

1. Make any changes you need to the script. By default it is looking for very specific menus on the site.
2. Run the script: `python LunchMenuScraper.py` or `python3 LunchMenuScraper.py`.
3. The script will open a headless Chrome browser and navigate to the Joplin Schools Nutrition Services website.
4. The script will find the link to the lunch menu PDF file and download it to your local machine.