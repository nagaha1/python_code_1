import re
import requests
from bs4 import BeautifulSoup 


load_url = "https://daidata.goraggio.com/100156/unit_list?model=P%E5%A4%A7%E5%B7%A5%E3%81%AE%E6%BA%90%E3%81%95%E3%82%93%E8%B6%85%E9%9F%8B%E9%A7%84%E5%A4%A9YTA&ballPrice=4.00&f=1"
html = requests.get(load_url)

soup = BeautifulSoup(html.text,"html.parser")

# print(soup)
# print("hello world")

# print(type(soup))

# タグの中を取得するを取得する
# chap2 = soup.find_all("tbody")
# chap2 = soup.find_all("td")

chap2 = soup.select("tbody")

# textを指定するにはforで回す必要があるみたい
for elem in chap2:
    test = elem.text.split() 
    # print(test[0])
    

# 9ごとに行を変える必要があります。
# 単純にこれでいいや
i = 1
for tes in test:
    if i % 9 == 0:
        print(str(tes) + "＝＝＝" + str(i) + "==9の倍数ですたい")
    i += 1

# 確認用
print("#########" + str(i))





print("##########でそのタグから##########")
# unit=3~~を基準にデータをぶっこ抜きたい

# "tbody"タグの中から、aタグの中だけを取得する
# for element in chap2.find_all("td"):
#     print("test")

# print(type(chap2))

# test = chap2.get("td")
# print(test)
