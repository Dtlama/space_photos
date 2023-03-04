from dotenv import load_dotenv
from main import download_image
import requests
import datetime
import os


def fetch_epic_photos(key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    photos = response.json()
    for photo in photos:
        image_name = photo['image']
        image_date = photo['date']
        image_date = datetime.datetime.fromisoformat(image_date)
        image_date=image_date.strftime('%Y/%m/%d')
        image_link = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png?api_key={key}'
        file_path = os.path.join('images', f'{image_name}.png')
        download_image(image_link, file_path, payload=payload)


if __name__ == '__main__':
    load_dotenv()
    key = os.environ["API_KEY"]
    os.makedirs('images', exist_ok=True)
    fetch_epic_photos(key)