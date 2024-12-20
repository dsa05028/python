# 웹스크래핑

from bs4 import BeautifulSoup
import requests


# html_str = """
# <html>
#     <body>
#         <div id="content">
#             <ul class="industry">
#                 <li>인공지능</li>
#                 <li>빅데이터</li>
#                 <li>신재생에너지</li>
#             </ul>
#             <ul class="comlang">
#                 <li>Python</li>
#                 <li>C++</li>
#                 <li>Javascript</li>
#             </ul>
#         </div>
#     </body>
# </html>
# """

# soup = BeautifulSoup(html_str, "html.parser")
#print(soup)
# first_ul = soup.find('ul')
# print(first_ul)
# print(first_ul.text) # 태그없이 텍스트 출력

# all_ul = soup.find_all('ul')
# print(all_ul[1])
# print(all_ul[1].text)

# class_ul = soup.find('ul', attrs={'class': "comlang"} )
# print(class_ul)
# print(class_ul.text)

# first_ul = soup.select_one("ul.industry")
# print(first_ul)
# print(first_ul.text)

# all_ul = soup.select("#content > ul")
# print(all_ul)

# 서울시청
# html_url = "https://www.seoul.go.kr/main/index.jsp"
# res = requests.get(html_url)
# # print(res.text)
# soup = BeautifulSoup(res.text, 'html.parser')
# all_nav = soup.select("nav > ul > li > a")
# # print(all_nav[1].text)
# for i in all_nav:
#     print(i.text)

# 실습.국립중앙 박물관 
# html_url = "https://www.museum.go.kr/site/main/home"
# res = requests.get(html_url)
# # print(res.text)
# soup = BeautifulSoup(res.text, "html.parser")

# infos = soup.select("ul.main-info-area > li")

# for i in infos:
#     print(i.text)

# #관람시간
# times = soup.select(".info-time > ul > li")
# #print(times)
# for i in times:
#     print("이용시간: ", i.text.strip())
# print()
# pay = soup.select(".info-admission > ul > li")
# for i in pay:
#     print("관람료: ", i.text.strip())


# html_url = "https://news.kbs.co.kr/news/pc/view/view.do?ncd=8118420"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')
# #print(soup)
# title = soup.select_one(".headline-title")
# print("제목: ", title.text)

# contents = soup.select_one(".detail-body")
# print("내용: ", contents.text.strip())

# with open("news.txt", "w", encoding="utf-8") as file:
#     file.write(contents.text.strip())


# 실습. 뉴스 크롤링
# html_url = "https://www.mk.co.kr/news/sports/11183644"
# res = requests.get(html_url)
# soup = BeautifulSoup(res.text, 'html.parser')
# #print(soup)
# title = soup.select_one(".news_ttl")
# print("제목: ", title.text.strip())
# time = soup.select_one(".registration:first-child > dd")
# print("발행시간: ", time.text.strip())
# content = soup.select_one(".news_cnt_detail_wrap")
# print("기사: ", content.text.strip())


'''html_url = "https://quotes.toscrape.com/page/2"
res = requests.get(html_url)
soup = BeautifulSoup(res.text, 'html.parser')
quote = soup.select(".quote > .text")
#print(len(quote))

# for i in quote:
#     print(i.text.strip())
text = [ i.text.strip() for i in quote]
#print(text)
speak = soup.select(".author")
author = [ i.text.strip() for i in speak]
# print(author)
zipped = list(zip(text, author))
#print(zipped)

for text, speak in zipped:
    print(f"말한사람: {speak} \n내용: {text}")
    print()'''

#실습.전자 신문 메인 기사 크롤링 강사님
import requests
from bs4 import BeautifulSoup

html_url="https://finance.naver.com/marketindex/"
res=requests.get(html_url)
soup=BeautifulSoup(res.text,"html.parser")
exchange=soup.select(".data>.data_|st>.on")

for i in exchange:
     print(i.text.strip())


