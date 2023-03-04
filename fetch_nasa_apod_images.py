from dotenv import load_dotenv
from image_tools import download_image
from image_tools import get_file_extension
import requests
import os


def fetch_nasa_apod(key):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": key, "count": 30}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    links = response.json()
    for number, image in enumerate(links):
        if image["media_type"] != "image":
            continue
        file_name = f'nasa_apod{number}.{get_file_extension(image["url"])}'
        file_path = os.path.join('images', file_name)
        download_image(image["url"], file_path)


if __name__ == '__main__':
    load_dotenv()
    key = os.environ["API_KEY"]
    os.makedirs('images', exist_ok=True)
    fetch_nasa_apod(key)
