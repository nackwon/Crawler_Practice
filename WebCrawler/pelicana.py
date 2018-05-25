import requests
from itertools import count
from bs4 import BeautifulSoup

def pelicanaStore():
    pStoreList = []

    for pagenumber in range(1, 117):
        url = "http://pelicana.co.kr/store/stroe_search.html?page=%s" % pagenumber
        html = requests.get(url).content # text / content 똑같은 것이고 글자가 깨지는 경우가 있으니 적절하게 사용하면 된다.

        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", {"class": "table mt20"}) # 테이블은 하나있기 때문에 find를 사용
        tbody = table.find("tbody")
        tr_tags = tbody.find_all("tr")

        for idx, tag in enumerate(tr_tags):
            storeData = list(tag.strings)
            name = storeData[1]
            tel = storeData[5].strip()
            address = storeData[3]

            # print(name, tel, address)
            pStoreList.append([name, tel, address])
    return pStoreList

result = pelicanaStore()

print(result)