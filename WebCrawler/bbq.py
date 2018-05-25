import requests
import pandas as pd
from bs4 import BeautifulSoup
from itertools import count


def bbqStroe():
    bStoreList = []
    for pagenumber in count(start=140):
        url ="http://changup.bbq.co.kr/findstore/findstore_ajax.asp?page=%s" % pagenumber
        # print(url)

        html = requests.get(url).content
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody")
        tr_tags = tbody.find_all("tr")

        if len(tr_tags) <= 1:
            break

        for idx, tag in enumerate(tr_tags):
            if idx != 0:
                storeDate = list(tag.strings)
                name = storeDate[1]
                tel = storeDate[5]
                address = storeDate[3]

                # print(name, tel, address)
                bStoreList.append([name, tel, address])
                # print(bStoreList)
    table = pd.DataFrame(bStoreList, columns=["name", "tel", "address"])
    table.to_csv("D:/fb/bbq_table.csv", encoding="utf-8-sig", mode="w", index=True)
    return bStoreList


result = bbqStroe()
print(result)