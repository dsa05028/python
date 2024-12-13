from pydataset import data
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# print(data())

#자동차의 실린더 수(cyl)에 따른 평균 연비(mpg)를 계산 후 막대그래프로 시각화
# mtcars=data('mtcars')
# # print(mtcars)
# avg_cyl=mtcars.groupby("cyl")["mpg"].mean().reset_index()
# sns.barplot(x="cyl",y="mpg",data=avg_cyl)


#자동차의 변속기 유형(am)별 평균 마력(hp)를 계산한 후 막대그래프로 시각화\
mtcars=data('mtcars')
avg_am=mtcars.groupby("am")["hp"].mean().reset_index()
sns.barplot(x="am",y="hp",data=avg_am)


#cyl(실린더 수)을 기준으로 gear(기어 수)에 따른 평균 연비를 계산하는 표를 재생성한 후 히트맵으로 시각화
# mtcars=data('mtcars')
# cyl_gear_4=mtcars[mtcars["cyl"]==4]
# cyl_gear_6=mtcars[mtcars["cyl"]==6]
# cyl_gear_8=mtcars[mtcars["cyl"]==8]
# avg_mpg1=cyl_gear_4.groupby("gear")["mpg"].mean()
# print(avg_mpg1)
# sns.heatmap(x="gear",y="mpg")



plt.show()