from urllib.parse import urlparse
import requests
import os


def get_file_extension(url):
    parsed_url = urlparse(url)
    split_text = os.path.splitext(parsed_url.path)
    return split_text[1]


def download_image(url, file_path, payload=None):
    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)
