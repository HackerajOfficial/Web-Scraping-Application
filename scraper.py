import requests
from bs4 import BeautifulSoup
import csv
import logging

# Configure logging
logging.basicConfig(filename='scraping_errors.log', level=logging.ERROR)

def scrape_and_store_books(url, csv_file):
    """
    Scrape Book's title, price, and rating from the given books website URL and store it in a CSV file.

    Parameters:
    - url (str): The URL of the Book page containing books and prices. e.g http://books.toscrape.com/
    - csv_file (str): The filename of the CSV file to store the data.

    Returns:
    None

    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-200 status codes
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all book containers
        book_containers = soup.find_all("article", class_="product_pod")

        # Open the CSV file in write mode
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)

            # Write header row
            writer.writerow(['Title', 'Price', 'Rating'])

            # Loop through each book container and extract title, price, and rating
            for book in book_containers:
                # Extract the title
                title = book.h3.a.get_text(strip=True)

                # Extract the price
                price = book.find("p", class_="price_color").get_text(strip=True)

                # Extract the rating
                rating_class = book.find("p", class_="star-rating")
                rating = rating_class['class'][1]

                # Write data row to CSV file
                writer.writerow([title, price, rating])

        print("Data has been written to the CSV file")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data from {url}: {e}")
        print("log error")
    except Exception as e:
        logging.error(f"Error processing data: {e}")
        print(f"second log error {e}")

# Test the function with Amazon's top sale products URL and CSV file
if __name__ == "__main__":
    book_site_url = 'http://books.toscrape.com/'
    csv_file = 'books.csv'

    scrape_and_store_books(book_site_url, csv_file)
