from main import download_image
import requests
import os


def fetch_spacex():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    for number, link in enumerate(links):
        file_name = f'spacex_photo{number}.jpg'
        file_path = os.path.join('images', file_name)
        download_image(link, file_path)


if __name__ == '__main__':
    os.makedirs('images', exist_ok=True)
    fetch_spacex()
