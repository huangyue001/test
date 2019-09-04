import requests,time
from pymongo import MongoClient
from bs4 import BeautifulSoup

urls = [
    "http://www.cnzhuitao.cn/Ajitongjiling/list_3_1.html",
    "http://www.cnzhuitao.cn/Ajitongjiling/list_3_2.html",
    "http://www.cnzhuitao.cn/Ajitongjiling/list_3_3.html",
    "http://www.cnzhuitao.cn/Ajitongjiling/list_3_4.html",
    "http://www.cnzhuitao.cn/Ajitongjiling/list_3_5.html",
    "http://www.cnzhuitao.cn/Ajitongjiling/list_3_6.html",
    "http://www.cnzhuitao.cn/Ajitongjiling/list_3_7.html",
    "http://www.cnzhuitao.cn/Ajitongjiling/list_3_8.html",
    "http://www.cnzhuitao.cn/Ajitongjiling/list_3_9.html",
    "http://www.cnzhuitao.cn/Ajitongjiling/list_3_10.html",

    "http://www.cnzhuitao.cn/Bjitongjiling/list_4_1.html",
    "http://www.cnzhuitao.cn/Bjitongjiling/list_4_2.html",
    "http://www.cnzhuitao.cn/Bjitongjiling/list_4_3.html",
    "http://www.cnzhuitao.cn/Bjitongjiling/list_4_4.html",
    "http://www.cnzhuitao.cn/Bjitongjiling/list_4_5.html",
    "http://www.cnzhuitao.cn/Bjitongjiling/list_4_6.html",
    "http://www.cnzhuitao.cn/Bjitongjiling/list_4_7.html",

    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_1.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_2.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_3.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_4.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_5.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_6.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_7.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_8.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_9.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_10.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_11.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_12.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_13.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_14.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_15.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_16.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_17.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_18.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_19.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_20.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_21.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_22.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_23.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_24.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_25.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_26.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_27.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_28.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_29.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_30.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_31.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_32.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_33.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_34.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_35.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_36.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_37.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_38.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_39.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_40.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_41.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_42.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_43.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_44.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_45.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_46.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_47.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_48.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_49.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_50.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_51.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_52.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_53.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_54.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_55.html",
    "http://www.cnzhuitao.cn/zaitaorenyuan/list_8_56.html"

]

client = MongoClient("mongodb://127.0.0.1:27017/?authSource=admin")
db = client["cnzhutiao"]
collection = db["text"]

re_url = ["http://www.cnzhuitao.cn/Ajitongjiling/780.html"]

base_url = "http://www.cnzhuitao.cn"


for url in urls:
    print(url)

    res = requests.get(url)
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text,"html.parser")

    lis = soup.select("li.list_title")

    for li in lis:
        new_url = li.select("a")[0].get("href")
        if new_url in re_url:
            continue
        public_time = li.select("span") [0].text
        name = li.select("a")[0].text

        res = requests.get(base_url + new_url)
        res.encoding = "utf-8"
        # print(res.text)
        soup = BeautifulSoup(res.text, "html.parser")
        text = soup.select("#textbody")[0].text
        try:
            collection.insert_one({
                "name":name,
                "text":text,
                "public_time":public_time,
                "crawler_time":time.time(),
                "url":base_url + new_url
            })
        except:
            print("重复")