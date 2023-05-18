# Web-Scraping-With-RegEx
 
This Python script demonstrates web scraping using the BeautifulSoup library for HTML parsing and navigation, combined with regular expressions (RegEx) for extracting specific data from the HTML content. The script provides an example of scraping search results from a Google search page for the query "cybersecurity trends".

## Prerequisites
- Python 3.6: Ensure that Python 3.6 is installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

- BeautifulSoup library: Install the BeautifulSoup library using the following command:
```
pip install beautifulsoup4
```

- Requests library: Install the Requests library using the following command:
```
pip install requests
```

## Usage
1. Clone the repository or download the script file.

2. Install the required libraries using the provided prerequisites.

3. Open the script in a Python editor or IDE.

4. Modify the `url` variable to the desired webpage URL you want to scrape. For example:
```python
url = "https://www.google.com/search?q=cybersecurity+trends"
```

5. Run the script using the Python interpreter. For example:
```
python web_scraping.py
```

## Description
The script performs the following steps:

1. Sends an HTTP GET request to the specified URL using the Requests library.

2. Retrieves the HTML content of the page.

3. Creates a BeautifulSoup object from the HTML content, enabling easy parsing and navigation.

4. Finds all the search results on the page using BeautifulSoup's `find_all()` method.

5. Defines regular expression patterns (`re_title` and `re_link`) to match specific HTML patterns for extracting the title and link information from each search result.

6. Iterates over each search result and applies the regular expressions to extract the title and link information.

7. Prints the extracted title and link for each search result.

## Customization
- You can modify the `url` variable to specify a different webpage URL you want to scrape. Ensure that the URL is accessible and allows scraping.

- Adjust the regular expressions (`re_title` and `re_link`) to match the specific HTML patterns for extracting data on different websites or webpages. Regular expressions can be modified to suit the structure and format of the target webpage's HTML.

- Modify the printing or data processing logic to suit your specific needs. You can save the extracted data to a file, store it in a database, or perform further analysis as required.

Note: Web scraping should be used responsibly and in accordance with the website's terms of service. Always respect website policies, be mindful of the frequency of requests, and ensure your scraping activities comply with legal and ethical considerations.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). 

## Contact

e-mail     : ajithchandranr@protonmail.com 
 
linkedin  : https://www.linkedin.com/in/ajithchandranr/
