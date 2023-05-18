import requests
from bs4 import BeautifulSoup
import re

# Send an HTTP GET request to the URL
url = "https://www.google.com/search?q=cybersecurity+trends"
response = requests.get(url)

# Get the HTML content of the page
html_content = response.text

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all the search results
results = soup.find_all("div", class_="g")

# Regular expressions patterns for title and link extraction
re_title = r'<h3.*?>(.*?)<\/h3>'
re_link = r'<a href="\/url\?q=(.*?)&amp;.*?"'

# Extract the titles and links of the search results using RegEx
for result in results:
    # Extract the title using RegEx
    title_match = re.search(re_title, str(result))
    if title_match:
        title = title_match.group(1)
    else:
        title = "N/A"
    
    # Extract the link using RegEx
    link_match = re.search(re_link, str(result))
    if link_match:
        link = link_match.group(1)
    else:
        link = "N/A"
    
    print("Title:", title)
    print("Link:", link)
    print("-" * 40)
