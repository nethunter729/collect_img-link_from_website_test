import requests
from bs4 import BeautifulSoup

try:
    # Prompt the user to enter the URL
    url = input("Enter the URL of the website you want to scrape:==> ")

    # Send an HTTP request to the specified URL
    page = requests.get(url)

    # Use BeautifulSoup to parse the HTML content of the page
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find all the links on the page
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))

    # Find all the images on the page
    images = soup.find_all('img')
    for image in images:
        print(image.get('src'))

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
