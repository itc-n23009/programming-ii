import requests, os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_page(url, output_dir):
    response = requests.get(url)
    if response.status_code == 200:
        filename = os.path.join(output_dir, f"{url.split('/')[-1]}.html")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        for link in BeautifulSoup(response.text, 'html.parser').find_all('a', href=True):
            download_page(urljoin(url, link['href']), output_dir)
    else:
        print(f"Link broken: {url}")

if __name__ == "__main__":
    output_dir = 'downloaded_pages'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    download_page('https://example.com', output_dir)

