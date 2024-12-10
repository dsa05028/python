#히스토그램

#matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

# path='C:\\Users\\HYOJEONG\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Pretendard-Black.otf'
# font=font_manager.FontProperties(fname=path).get_name()
# plt.rc("font",family=font)

# data=[1,2,2,3,3,3,4,5,5,5,5,5,6]
# plt.hist(data,bins=5,color="green",histtype="step")
# plt.title="히스토그램"
# plt.xlabel("값")
# plt.ylabel("빈도수")
# plt.show()

#여러개 데이터
# data1=[1,2,2,3,3,3,4]
# data2=[2,3,3,4,4,5,6]

# plt.hist([data1,data2],bins=5,color=["green","purple"],alpha=0.5,label=["data1","data2"])
# plt.title("여러개 히스토그램")
# plt.xlabel("값")
# plt.ylabel("빈도수")
# plt.legend()
# plt.show()

#산점도
# x=[1,2,3,4,5]
# y=[2,3,5,7,11]
# sizes=[20,50,80,100,200]
# colors=[10,20,30,40,50]

# plt.scatter(x,y,s=sizes,c=colors,cmap="viridis")
# plt.colorbar(label="color bar")
# plt.show()

# import numpy as np

# n=50
# x=np.random.rand(n) #0과 1 사이의 난수
# y=np.random.rand(n)

# area=(30*np.random.rand(n))**2 #0과 30 사이의 난수 생성>제곱하여 크기 생성
# colors=np.random.rand(n)

# plt.scatter(x,y,s=area, c=colors, cmap="Spectral",alpha=0.5)
# plt.show()

#파이차트
# sizes=[25,25,20,20]
# labels=['A','B','C','D']

#강조 파이차트
# sizes=[15,30,45,10]
# labels=['apple','banana','grape','cherry']
# explod=[0,0.1,0,0] #banana 강조

# plt.pie(sizes,labels=labels,explode=explod,autopct="%1.1f%%",shadow=True,startangle=140)

#색상,텍스트 스타일 지정 파이차트
# sizes=[10,20,30,40]
# labels=['A','B','C','D']
# colors=["gold","lightblue","lightgreen","pink"]
# plt.pie(
#     sizes, labels=labels, 
#     colors=colors, autopct="%1.1f%%",
#     textprops={"fontsize":20,"color":"darkblue"},
#     wedgeprops={"edgecolor":"black"})

#도넛
# sizes=[40,30,20,10]
# labels=['X','Y','Z','W']

# plt.pie(sizes,labels=labels,wedgeprops={"width":0.4})

# plt.show()

#실습.그래프 그리기

#기본 그래프
# months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# sales_2019=[100,120,140,110,130,150,160,170,180,200,190,210]
# sales_2020=[90,110,130,120,140,160,170,160,150,180,200,190]

# plt.plot(months,sales_2019,label=2019)
# plt.plot(months,sales_2020,label=2020)
# plt.title("Montly Sales Comparison(2019-2020)")
# plt.legend()
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.show()

#기본그래프 강사님 ver
# months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# sales_2019=[100,120,140,110,130,150,160,170,180,200,190,210]
# sales_2020=[90,110,130,120,140,160,170,160,150,180,200,190]

# plt.figure(figsize=(10,6)) #그래프 창 크기 조절
# plt.plot(months,sales_2019,label=2019,color="blue")
# plt.plot(months,sales_2020,label=2020,color="orange")
# plt.title("Montly Sales Comparison(2019-2020)",fontsize=15,pad=10)
# plt.legend()
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.show()

#막대그래프
# categories=["Category1","Category2","Category3","Category4","Category5"]
# data=[20,35,15,27,45]

# plt.bar(categories,data)
# plt.xlabel("Categoriese")
# plt.ylabel("Values")
# plt.title("Bar Chart")
# plt.ylim([0,50])
# plt.grid()
# plt.show()

#막대그래프 강사님 ver
# categories=["Category1","Category2","Category3","Category4","Category5"]
# data=[20,35,15,27,45]

# plt.figure(figsize=(8,10))
# plt.bar(categories,data,color="blue",alpha=0.7)
# plt.xlabel("Categoriese",fontsize=16)
# plt.ylabel("Values",fontsize=16)
# plt.title("Bar Chart",fontsize=20,pad=10)
# plt.xticks(rotation=45)
# plt.grid(True,axis="both",linestyle="--",alpha=0.6)
# plt.show()

#도넛 그래프
# sizes=[34,32,16,18]
# labels=["Apple","Banana","Melon","Grapes"]
# explode=[0.1,0.1,0.1,0.1]
# colors=["red","yellow","green","purple"]

# plt.pie(sizes,
#         labels=labels,
#         explode=explode,
#         colors=colors,
#         wedgeprops={"width":0.8,"edgecolor":"black"},
#         autopct="%1.1f%%",
#         textprops={"fontsize":10,"color":"black"}
#         )

# plt.show()

#도넛 그래프 강사님 ver
# sizes=[34,32,16,18]
# labels=["Apple","Banana","Melon","Grapes"]
# explode=[0,0.1,0,0.1]
# colors=["red","yellow","green","purple"]

# plt.pie(sizes,
#         labels=labels,
#         explode=explode,
#         colors=colors,
#         wedgeprops={"width":0.7,"edgecolor":"black"},
#         autopct="%1.1f%%"
#         )

# plt.show()

