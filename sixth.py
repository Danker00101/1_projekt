import requests
from html.parser import HTMLParser
from urllib.parse import urljoin


def download_url_and_get_all_hrefs(url):
    """
    Stahne webovou stranku a vrati seznam vsech odkazu z tagu <a href="...">.
    """
    hrefs = []

    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == "a":
                for name, value in attrs:
                    if name == "href" and value is not None:
                        hrefs.append(urljoin(url, value))

    response = requests.get(url, timeout=15)
    if response.status_code != 200:
        raise ValueError(f"Stranka vratila HTTP kod {response.status_code}")

    parser = LinkParser()
    parser.feed(response.text)
    return hrefs


if __name__ == "__main__":
    try:
        print(download_url_and_get_all_hrefs("https://www.jcu.cz"))
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
