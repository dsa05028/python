
import seaborn as sns
import matplotlib.pyplot as plt

# 실습1. 데이터 분석 후 그래프 그리기 강사님 ver
# penguins=sns.load_dataset('penguins')
# print(penguins.head())

# 펭귄의 종별 평균 몸무게를 막대그래프로 시각화 강사님 ver
# sns.barplot(x="species",y="body_mass_g",data=penguins)
# plt.show()

# 부리길이와 부리 깊이의 관계를 산점도로 시각화, 종별로 색상을 다르게 표시 강사님 ver
# sns.scatterplot(x="bill_length_mm",y="bill_depth_mm",data=penguins,hue="species")
# plt.show()

#펭귄의 섬에 따라 몸무게의 분포(violinplot) 강사님 ver
# sns.violinplot(x="island",y="body_mass_g",data=penguins)
# plt.show()


flights=sns.load_dataset('flights')

#연도별 승객수의 평균을 꺽은선 그래프로 나타내시오.강사님 ver
# avgpassenger=flights.groupby("year")["passengers"].mean().reset_index()
# #reset_index():index를 초기화, 기존 인덱스를 데이터프레임의 열로 변환해준다.
# print(avgpassenger)
# plt.plot(avgpassenger["year"],avgpassenger["passengers"])
# plt.grid(True)
# plt.show()

#연도와 월별 승객 수를 히트맵으로 시각화하세요.강사님 ver
pivot=flights.pivot(index="month",columns="year",values="passengers")
print(pivot)
# sns.heatmap(pivot,annot=True,fmt="d",annot_kws={"size":7})
# plt.show()

#특정연도(예:1958)의 월별 승객 수를 막대 그래프로 나타내세요.강사님 ver
# passengers_1958=flights[flights["year"]==1958]
# print(passengers_1958)
# sns.barplot(data=passengers_1958,x="month",y="passengers")
# plt.show()

# titanic
# titanic=sns.load_dataset("titanic")
# print(titanic.head())

# #탑승 클래스와 생존 여부 간의 관계를 catplot으로 시각화.강사님 ver
# sns.catplot(x="class",hue="survived",data=titanic,kind="count")
# plt.show()

#나이의 분포를 생존여부에 따라 kdeplot으로 시각화하세요. 강사님 ver
# sns.kdeplot(data=titanic,x="age",hue="survived",fill=True)
# plt.show()

