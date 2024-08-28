Product Scraper

This tool is a simple web scraping application for extracting product information from a website. It scrapes the name and price of products from a specific webpage and saves the data to a CSV file.

CAUTION: If changing the website URL, ensure you have permission to scrape data from that site.

Requirements

* Python 3.11.4
* requests library (install via pip install requests)
* BeautifulSoup library (install via pip install beautifulsoup4)
* csv library (included with Python)

How to Use the Tool

* Run the Python Script
* Execute the script in any Python environment or IDE of your choice (e.g., PyCharm, VS Code, IDLE, etc.).

Scraping Products

* The script fetches data from the website "https://books.toscrape.com/".
* It extracts the name and price of each product listed on the page.

Saving Data

* The product information is saved in a CSV file named products.csv.
* The CSV file will be created in the same directory as the script.

Example Use Case

After running the script, products.csv will be created.
This CSV file will contain a list of products with their names and prices.

Notes

* Ensure you have an active internet connection to fetch data from the specified URL.
* The requests and BeautifulSoup libraries need to be installed using pip if not already available.
* The CSV file will be overwritten each time the script is run.

Enjoy scraping product data with this simple and effective tool!
