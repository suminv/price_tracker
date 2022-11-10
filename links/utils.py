from bs4 import BeautifulSoup
import requests


def get_link_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                      'Version/16.1 Safari/605.1.15',
        'Accept-Language': 'en-GB,en;q=0.9',
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.select_one(selector='#entity > div > div.entityHeader.edition > header > h1 > a').getText().strip()
    price = soup.find('div', class_='shops').find('a').get_text().replace('€', '').replace('-', '').\
        replace('.', '').replace(',', '.').strip()
    photo_url = soup.find('div', class_='imageCarousel').find('a').get('href').strip()

    return name, float(price), photo_url
