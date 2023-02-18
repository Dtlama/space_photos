from urllib.parse import urlparse
import requests
import os


def get_file_extension(url):
    parsed_url = urlparse(url)
    split_text = os.path.splitext(parsed_url.path)
    return split_text[1]

def download_image(url, file_path):
    response = requests.get(url)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)

def fetch_spacex():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    for number, link in enumerate(links):
        file_name = f'spacex_photo{number}.jpg'
        file_path = os.path.join('images', file_name)
        download_image(link, file_path)

fetch_spacex()
get_file_extension('https://apod.nasa.gov/apod/image/2302/JWSTMIRI_ngc1365_1024.png')

os.makedirs('images', exist_ok=True)
