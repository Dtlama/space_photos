from urllib.parse import urlparse
from dotenv import load_dotenv
import requests
import os
import pprint


load_dotenv()

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

def fetch_nasa_apod(key):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": key, "count": 30}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    links = response.json()
    pprint.pprint(links)
    for number, image in enumerate(links):
        if image["media_type"] != "image":
            continue
        file_name = f'nasa_apod{number}.{get_file_extension(image["url"])}'
        file_path = os.path.join('images', file_name)
        download_image(image["url"], file_path)

def fetch_epic_photos(key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    photos = response.json()
    pprint.pprint(photos)

os.makedirs('images', exist_ok=True)
#fetch_spacex()
get_file_extension('https://apod.nasa.gov/apod/image/2302/JWSTMIRI_ngc1365_1024.png')

key = os.environ["API_KEY"]
#fetch_nasa_apod(key)
fetch_epic_photos(key)
