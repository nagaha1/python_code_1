import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp"
res = requests.get(url)

# print(res.text[:600])
# print(res.text)

# BeautifulSoup使って、パーサを使って情報を解析する必要がある

soup = BeautifulSoup(res.text,"html.parser")
# この方法で取得するとジャストで取得できる
ele = soup.select('#uamods-topics > div > div > div > ul > li.sc-esjQYD.cLTKuH > a')

print(ele[0].contents[0])
print(ele[0].attrs['href'])
# for test in ele:
#     print(test)


