import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager

import os
  # 경로에 파일이 있으면 True, 없으면 False

path='C:\\Users\\HYOJEONG\\AppData\\Local\\Microsoft\\Windows\\Fonts\\AppleSDGothicNeoL.ttf'
font=font_manager.FontProperties(fname=path).get_name()
plt.rc("font",family=font)

file_name="./1211/202411_202411_연령별인구현황_월간 (2).csv"
data=pd.read_csv(file_name,encoding="EUC-KR")


region_name=input("검색하고 싶은 지역명을 입력하세요:")
data=data.rename(columns={"행정구역":"지역명"})
male_columns = [col for col in data.columns if "남" in col and "세" in col]
female_columns = [col for col in data.columns if "여" in col and "세" in col]
print(female_columns)
#숫자변환
for col in male_columns + female_columns:
    data[col] = data[col].astype(str).str.replace(",", "").astype(int)
#필터링
#contains():문자열 데이터 필터링할때 혹은 특정 패턴을 찾을때 사용
#na:NaN(결측값)을 포함할지 결정, 기본값이 true
#case:영문의 대소문자 구분, 기본값이 true

region_data=data[data["지역명"].str.contains(region_name,na=False)]
print(region_data)

if region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")

#2024년 11월 계 80~89세[2024년11월, 80~89세]
#데이터 추출
male_groups=[col.split("_남_")[1] for col in male_columns]
male_population = region_data[male_columns].iloc[0].values
female_groups=[col.split("_여_")[1] for col in female_columns]
female_population = region_data[female_columns].iloc[0].values

#그래프 그리기
plt.plot(male_groups, male_population, marker="o", label=f"{region_name} 남성 인구")
plt.plot(female_groups, female_population, marker="o", label=f"{region_name} 여성 인구")
plt.title(f"{region_name} 연령별 남성 및 여성 인구 비교",fontsize=16,pad=10)
plt.xlabel("연령")
plt.ylabel("인구수")
plt.grid(True,linestyle="--",alpha=0.6)
plt.xticks(rotation=45)
plt.legend()
plt.show()