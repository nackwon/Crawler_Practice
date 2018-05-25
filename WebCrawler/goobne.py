import time
import pandas as pd
from itertools import count
from selenium import webdriver
from bs4 import BeautifulSoup



def goobneStore():
    gStoreList = []
    wd = webdriver.Chrome("D:\dev\chromedriver.exe")
    wd.get("https://www.goobne.co.kr/store/search_store.jsp")

    for page in count(start=102):

        wd.execute_script("store.getList(%s)" % page)
        time.sleep(5)

        html = wd.page_source
        soup = BeautifulSoup(html, "html.parser")
        tbody = soup.find("tbody", {"id" : "store_list"})
        tr_tags = tbody.find_all("tr")

        if tr_tags[0].get("class") is None:
            break

        for idx, tag in enumerate(tr_tags):
            tagData = list(tag.strings)
            name = tagData[1]
            tel = tagData[4]
            address = tagData[5] if tagData[4] == ' ' else tagData[6]
            gStoreList.append([name, tel, address])

    # table = pd.DataFram(gStoreList, columns=["name", "tel", "address"])
    # table.to_csv("D:/fb/goobne.csv", encoding="utf-8-sig", mode="w", index=True)
    return gStoreList

print(goobneStore())