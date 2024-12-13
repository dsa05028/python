#seaborn

import seaborn as sns
# print(sns.get_dataset_names())

import matplotlib.pyplot as plt

#예제데이터
# tips=sns.load_dataset('tips')
# print(tips.head())

# sns.scatterplot(
#     x="total_bill",
#     y="tip",
#     hue="sex",
#     style="time",
#     size="size",
#     data=tips
# )

# sns.scatterplot(x="total_bill",y="tip",hue="sex",palette="deep",style="time",size="size",data=tips)

# sns.stripplot(x="day",y="total_bill",data=tips,jitter=True,hue="size",dodge=True)
# sns.swarmplot(x="day",y="total_bill",data=tips,hue="size",dodge=True)
# sns.relplot(x="total_bill",y="tip",data=tips,style="time",hue="sex")
# sns.catplot(x="day",y="total_bill",data=tips,hue="sex",kind="point")
# sns.displot(tips["total_bill"],bins=30,kde=True)

# import numpy as np

# data=np.random.rand(10,10)
# sns.heatmap(data,annot=True,fmt=".2f",cmap="coolwarm")

# sns.pairplot(tips,hue="sex")
# sns.regplot(x="total_bill",y="tip",data=tips)

# plt.show()

#실습1. 데이터 분석 후 그래프 그리기
# penguins=sns.load_dataset('penguins')
# print(penguins.head())

#펭귄의 종별 평균 몸무게를 막대그래프로 시각화
# penguins=sns.load_dataset('penguins')
# plt.bar(x="species",height="body_mass_g",data=penguins)
# plt.title("Average weight of penguin species")
# plt.xlabel("species")
# plt.ylabel("body mass(g)")
# plt.show()

#부리길이와 부리 깊이의 관계를 산점도로 시각화, 종별로 색상을 다르게 표시
# sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=penguins,hue="species")
# plt.show()

# #펭귄의 섬에 따라 몸무게의 분포(violinplot)
# sns.violinplot(x="island",y="body_mass_g",data=penguins)
# plt.show()

# flights=sns.load_dataset('flights')
# print(flights.head())

#연도별 승객수의 평균을 꺽은선 그래프로 나타내시오.

# flights=sns.load_dataset('flights')
# avgpassenger=flights.groupby(by="year").mean()
# print(avgpassenger)
# sns.lineplot(x="year",y="passengers",data=avgpassenger)
# plt.show()

#연도와 월별 승객 수를 히트맵으로 시각화하세요.
# flights=sns.load_dataset('flights').pivot(index="year",columns="month",values="passengers")
# sns.heatmap(flights,annot=True,fmt=".1f",annot_kws={"size":7})
# plt.show()

#특정연도(예:1958)의 월별 승객 수를 막대 그래프로 나타내세요.
# flights=sns.load_dataset('flights')
# passengers_1958=flights.loc[flights["year"]==1958]
# # print(passengers_1958.head())
# plt.bar(data=passengers_1958,x="month",height="passengers")
# plt.title("Monthly passenger numbers in 1958")
# plt.xlabel("month")
# plt.ylabel("passengers")
# plt.show()

#titanic
# titanic=sns.load_dataset("titanic")
# print(titanic.head())

# #탑승 클래스와 생존 여부 간의 관계를 catplot으로 시각화
# sns.catplot(x="class",y="survived",data=titanic,kind="bar")
# plt.show()