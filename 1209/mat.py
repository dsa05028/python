#matplotlib

import matplotlib.pyplot as plt
from matplotlib import font_manager

#폰트경로 찾기
'''font_list=font_manager.findSystemFonts(fontpaths=None,fontext="ttf")
print(font_list)'''

'''path='C:\\Users\\HYOJEONG\\AppData\\Local\\Microsoft\\Windows\\Fonts\\AppleSDGothicNeoH.ttf'
font=font_manager.FontProperties(fname=path).get_name()
plt.rc("font",family=font)'''

'''x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.plot(x,y,marker="*",markersize=30,markerfacecolor="red",markeredgecolor="green")
# plt.plot(x,y, color="red",linestyle="--",linewidth=3,label="samplegraph")
# plt.show()

font={
    "size":20,
    "color":"white",
    "backgroundcolor":"black",
    "weight":"bold"
}

# plt.title("matplotlib",pad=30,fontsize=20,color="#ff0000",backgroundcolor="green")
plt.title("matplotlib",pad=10,fontdict=font)
plt.xlabel("x",fontdict=font,labelpad=20)
plt.ylabel("y",fontdict=font)
plt.grid(True,axis="both",linestyle="--",color="blue",alpha=0.1)
# plt.legend(title="legend name",fontsize=13,loc="lower center")

# plt.xlim([0,10])
# plt.ylim([0,15])
# plt.axis("equal")
# plt.axis("scaled")
# plt.axis("tight")
# plt.axis("auto")
plt.axis([0,10,0,15])
plt.show()
'''

#------------
#그래프 선 여러개
'''x=[1,2,3,4]
y1=[1,2,3,4]
y2=[2,4,6,8]
y3=[3,6,9,12]
y4=[4,8,12,16]
plt.plot(x,y1,label="y=x",color="red",marker="o")
plt.plot(x,y2,label="y=2x",color="orange",marker="*")
plt.plot(x,y3,label="y=3x",color="green",marker=">")
plt.plot(x,y4,label="y=4x",color="blue",marker="<")

plt.legend(loc="upper center",title="four practice",ncol=4)
plt.title("graph practice")
plt.xlabel("x")
plt.ylabel("y")
plt.show()'''

#------------
#그래프 여러개
'''x=[1,2,3,4]
y1=[1,2,3,4]
y2=[2,4,6,8]
y3=[3,6,9,12]
y4=[4,8,12,16]

plt.subplot(2,2,1)
plt.plot(x,y1)
plt.title("y=x")

plt.subplot(2,2,2)
plt.plot(x,y2)
plt.title("y=2x")

plt.subplot(2,2,3)
plt.plot(x,y3)
plt.title("y=3x")

plt.subplot(2,2,4)
plt.plot(x,y2)
plt.title("y=4x")

plt.suptitle("graph practice")
plt.tight_layout()
plt.show()'''

#------------
#막대그래프
'''categories=["A","B","C"]
values=[10,15,7]

# plt.bar(categories,values,width=0.3,color=["r","g","b"],alpha=0.5,edgecolor="black",linewidth=1.5)
bars=plt.bar(categories,values,color="orange",label="bar sample")
for bar in bars:
    plt.text(bar.get_x()+bar.get_width()/2, #x좌표, 막대의 중심
             bar.get_height()+0.5,          #y좌표
             str(bar.get_height()),
             ha="center",va="top",color="black")
plt.xticks(categories,["2023","2024","2025"])
plt.title("bar graph practice",pad=20)
plt.xlabel("categories")
plt.ylabel("values")
plt.show()'''

#------------
#수평그래프
categories=["A","B","C"]
values=[10,15,7]

bars=plt.barh(categories,values,color="skyblue",edgecolor="red")
for bar in bars:
    plt.text(bar.get_width()+0.5, #x좌표
             bar.get_y()+bar.get_height()/2,
             str(bar.get_width()),
             ha="right",va="center",color="green"         
            ) 
plt.legend(bars,["A:2023","B:2024","C:2025"],ncol=3)
plt.axvline(x=values[2],linestyle="--") #기준선
plt.title("bar graph practice",pad=20)
plt.xlabel("categories")
plt.ylabel("values")
# plt.show() #창띄우기
plt.savefig("./1209/graph.jpg",format="jpg") #저장