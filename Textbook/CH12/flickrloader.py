import os, requests
from bs4 import BeautifulSoup

SEARCH_KEYWORD = 'cat'
IMAGES_TO_DOWNLOAD = 5
FLICKR_SEARCH_URL = f'https://www.flickr.com/search/?text={SEARCH_KEYWORD}'
DOWNLOAD_DIR = 'download'

def download_image(url, path):
    with requests.get(url, stream=True) as r:
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)

def search_and_download_images():
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    soup = BeautifulSoup(requests.get(FLICKR_SEARCH_URL).text, 'html.parser')
    images = soup.find_all('img', limit=IMAGES_TO_DOWNLOAD)
    for i, img in enumerate(images):
        img_url = img['src']
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        if '_m.' in img_url:
            img_url = img_url.replace('_m.', '_b.')
        download_image(img_url, os.path.join(DOWNLOAD_DIR, f"image_{i+1}.jpg"))
        print(f"download image {img_url}")

if __name__ == '__main__':
    search_and_download_images()
    print("download image success.")

