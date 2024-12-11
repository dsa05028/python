import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager


path='C:\\Users\\HYOJEONG\\AppData\\Local\\Microsoft\\Windows\\Fonts\\Pretendard-Black.otf'
font=font_manager.FontProperties(fname=path).get_name()
plt.rc("font",family=font)

file_name="./1211/연령별인구현황.csv"
data=pd.read_csv(file_name,encoding="EUC-KR")

region_name=input("검색하고 싶은 지역명을 입력하세요:")
data=data.rename(columns={"행정구역":"지역명"})
age_columns=[col for col in data.columns if "세" in col]

#숫자변환
for col in age_columns:
    data[col]=data[col].str.replace(",","").astype(int)

#필터링
#contains():문자열 데이터 필터링할때 혹은 특정 패턴을 찾을때 사용
#na:NaN(결측값)을 포함할지 결정, 기본값이 true
#case:영문의 대소문자 구분, 기본값이 true
region_data=data[data["지역명"].str.contains(region_name,na=False)]
print(region_data)
# if region_data.empty:
#     print(f"{region_name}의 지역은 존재하지 않습니다.")

# #2024년 11월 계 80~89세[2024년11월, 80~89세]
# #데이터 추출
# age_groups=[col.split("_계_")[1] for col in age_columns]
# result=region_data[age_columns].iloc[0].values

# #그래프 그리기
# plt.plot(age_groups,result,marker="o",label=region_name)
# plt.title(f"Number of populations by age at {region_name}",fontsize=16,pad=10)
# plt.xlabel("age")
# plt.ylabel("population number")
# plt.grid(True,linestyle="--",alpha=0.6)
# plt.xticks(rotation=45)
# plt.legend()
# plt.show()
# # print(age_groups)
# # print(result)