import requests
from bs4 import BeautifulSoup
import numpy as np

#url
url="https://www.koreabaseball.com/Record/TeamRank/TeamRank.aspx"

res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")

#데이터 추출
table=soup.find("table",attrs={"class":"tData"})
values=table.find_all("tr")[1:]

#데이터 정렬
lists=[]
for value in values:
    tds=value.find_all("td")
    tds=[i.text.strip() for i in tds]
    print(tds)
    lists.append(tds[0],tds[1],tds[3],tds[4],tds[5],tds[6])
    # tds[0],tds[1],tds[3],tds[4],tds[5],tds[6]


array=np.array(lists)
# print(array)

#파일 만들기
file_name="kbo_2024_ranking.txt"
header="순위\t팀\t승\t패\t무\t승률"

with open(file_name,'w',encoding="utf-8") as file:
    #해더쓰기
    file.write(header+"\n")
    for data in array:
        file.write("\t".join(data))

with open(file_name, 'r', encoding="utf-8") as file:
    print(file.read())
    