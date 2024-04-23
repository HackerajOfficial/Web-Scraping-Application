# Web Scraping Application

## Description:
web scraping to extract data from a website and stores it in a structured
format. This project aims to assess your proficiency in web scraping techniques, data
handling, error management.

## Technologies Used:
- **bs4 / BeautifulSoup:** Beautiful Soup is a Python library used for web scraping purposes. It provides tools for parsing HTML and XML documents and extracting useful information from them.

- **requests:** The requests library in Python is a powerful and user-friendly tool for making HTTP requests. 



## Usage:
1. Clone the repository to your local machine.
     ```
      git clone https://github.com/HackerajOfficial/Web-Scraping-Application.git
     ```
2. Active environment
     ```
       venv\Scripts\activate
     ```
3. Install the necessary dependencies
    ```
      pip install -r requirements.txt
    ```
4. Start the Django development server:
    ```
      python scraper
    ```

## Limitations:
- **Website Changes:** Web scraping relies on the structure of the website being consistent over time. If the website's structure changes, such as class names or HTML layout, the scraping code may break.