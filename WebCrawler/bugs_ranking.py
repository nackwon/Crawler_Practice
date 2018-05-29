import requests
from bs4 import BeautifulSoup


def melon_ranking():
    melonList = []
    url ="https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01"
    html = requests.get(url).content

    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"class": "byChart"})
    title = table.find_all("p", {"class": "title"})
    artist = table.find_all("p", {"class": "artist"})
    album = table.find_all("a", {"class": "album"})

    for idx, song in enumerate(title):
        print(idx+1, song.a.get_text())

melon_ranking()