import requests, os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid(url):
    return bool(urlparse(url).netloc) and bool(urlparse(url).scheme)

def get_all_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return {urljoin(url, a['href']) for a in soup.find_all('a', href=True) if is_valid(urljoin(url, a['href']))}
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return set()

def download_page(url, session):
    try:
        response = session.get(url)
        if response.status_code == 404:
            print(f"リンク切れ: {url}")
        else:
            path = os.path.join("downloads", urlparse(url).netloc, urlparse(url).path.strip("/"))
            if not os.path.splitext(path)[1]:
                path = os.path.join(path, "index.html")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as f:
                f.write(response.content)
            print(f"ダウンロード: {url}")
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")

def main(start_url):
    session = requests.Session()
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    os.makedirs("downloads", exist_ok=True)

    for link in get_all_links(start_url):
        download_page(link, session)

if __name__ == "__main__":
    start_url = input("URLを入力してください: ")
    main(start_url)

