import requests
from bs4 import BeautifulSoup # 태그를 작살내는 모듈

def naver_movie():

    url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    html = requests.get(url).text #요청 온것 중에 text만 받기

    soup = BeautifulSoup(html, "html.parser") # parser 태그에 대해 이해하고 분석
    tags = soup.find_all("div", {"class": "tit3"}) # 해당하는 것을 모두 찾아서 list로 가져온다. class 이름이 tit3인 것을 모두 가져와라

    for idx, tag in enumerate(tags): # 앞에 숫자를 붙여준다 0부터 시작
        tag.a.get_text() # tag.a.text 똑같음
        print(idx+1, tag.a.get_text())

naver_movie()