import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/index.html"

# 發送 GET 請求取得網頁內容
response = requests.get(url)
html = response.text

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, "html.parser")

# 找出 class 為 "title" 的所有 div 元素
div_elements = soup.find_all("div", class_="title")
author = soup.find_all("div", class_="author")

# 逐一處理每個 div 元素，並取得 a 標籤的文字
# for div_element in div_elements:
#     a_element = div_element.find("a")
#     if a_element is not None:
#         print(a_element.string)
#         print('https://www.ptt.cc' + a_element.get("href"))

for index, value in enumerate(div_elements):
    a_element = value.find("a")
    if a_element is not None:
        print(a_element.string)
        print('https://www.ptt.cc' + a_element.get("href"))
        print(author[index].string)