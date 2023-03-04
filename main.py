from urllib.parse import urlparse
from dotenv import load_dotenv
import requests
import os
import datetime


def get_file_extension(url):
    parsed_url = urlparse(url)
    split_text = os.path.splitext(parsed_url.path)
    return split_text[1]

def download_image(url, file_path, payload=None):
    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    load_dotenv()
    os.makedirs('images', exist_ok=True)
    get_file_extension('https://apod.nasa.gov/apod/image/2302/JWSTMIRI_ngc1365_1024.png')

    key = os.environ["API_KEY"]
