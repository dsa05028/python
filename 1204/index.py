#실습3. 환율 정보 크롤링 강사님
from bs4 import BeautifulSoup
import requests

'''html_url="https://finance.naver.com/marketindex/"
res=requests.get(html_url)
soup=BeautifulSoup(res.text,"html.parser")
# print(soup)
usd=soup.select_one("#exchangeList .usd .value")
print("USD:",usd.text)
jpy=soup.select_one("#exchangeList .jpy .value")
print("JPY:",jpy.text)
eur=soup.select_one("#exchangeList .eur .value")
print("EUR:",eur.text)
cny=soup.select_one("#exchangeList .cny .value")
print("CNY:",cny.text)'''

#실습4. 주식 정보 크롤링
'''html_url="https://finance.naver.com/item/main.naver?code=035720"
res=requests.get(html_url)
soup=BeautifulSoup(res.text,"html.parser")
#print(soup)
company=soup.select_one(".wrap_company>h2>a")
print("회사명:",company.text.strip())
price=soup.select_one(".today>.no_today .blind")
print("가격:",price.text.strip())
aprice=soup.select_one(".today>.no_exday .blind")
print("전일대비가격:",aprice.text.strip())
aprice=soup.select(".today>.no_exday .blind")
print("전일대비가격:",aprice[0].text.strip())'''

#주식 정보 크롤링 함수
'''def stock(code):
    html_url=f"https://finance.naver.com/item/main.naver?code={code}"
    res=requests.get(html_url)
    soup=BeautifulSoup(res.text,"html.parser")
    #print(soup)

    company=soup.select_one(".wrap_company>h2>a")
    print("회사명:",company.text.strip())
    price=soup.select_one(".today>.no_today .blind")
    print("가격:",price.text.strip())
    aprice=soup.select_one(".today>.no_exday .blind")
    print("전일대비가격:",aprice.text.strip())
    # aprice=soup.select(".today>.no_exday .blind")
    # print("전일대비가격:",aprice[0].text.strip())

stock("035720")
stock("005930")'''


#기사제목 크롤링
'''html_url="https://n.news.naver.com/mnews/article/241/0003399408"
res=requests.get(html_url)
soup=BeautifulSoup(res.text,"html.parser")
# print(soup)
title=soup.select_one(".media_end_head_title>h2")
print("기사제목:",title.text)'''

html_url="https://www.e-himart.co.kr/app/search/totalSearch?query=%EB%85%B8%ED%8A%B8%EB%B6%81&optChk=&FROM=WEBTOP&cateFilterYn=Y"
res=requests.get(html_url)
print(res.text)
soup=BeautifulSoup(res.text,"html.parser")
name=soup.select_one(".brndname" )
print(name)