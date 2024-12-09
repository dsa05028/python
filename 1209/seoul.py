import pandas as pd

file_name="./1209/서울특별시_공원 내 운동기구 설치 현황_20201231.csv"
df=pd.read_csv(file_name,encoding="cp949")
# print(df.head())
# print(df.info())
# print(df.isnull().sum()) #결측값 확인

#공원별 총 운동기구
df.columns=df.columns.str.strip() #문자열 공백 제거1
print(df.columns)
df["구분"]=df["구분"].str.strip() #문자열 공백 제거2
df["운동기구 기종명"]=df["운동기구 기종명"].str.strip()

'''
park_counts=df.groupby("구분")["운동기구 수량"].sum()
print(park_counts)

with open("./1209/park_counts.txt","w",encoding="utf-8") as file:
    file.write("공원별 총 운동기구 설치 수\n")
    file.write(park_counts.to_string())
'''
#운동기구 종류별 설치 개수=>빈도수
'''equipment_counts=df["운동기구 기종명"].value_counts()
print(equipment_counts)

with open("./1209/equipment_counts.txt","w",encoding="utf-8") as file:
    file.write("운동기구 종류별 설치 개수\n")
    file.write(equipment_counts.to_string())'''

#관리기관별 총 운동기구 개수
'''manage_count=df.groupby("관리기관")["운동기구 수량"].value_counts()
print(manage_count)

with open("./1209/manage_count.txt","w",encoding="utf-8") as file:
    file.write("관리기관별 총 운동기구 개수\n")
    file.write(manage_count.to_string())'''

#특정공원 운동기구 개수=>필터
'''filter_park=df[df['구분']=="남산공원(회현)"]
print(filter_park)

with open("./1209/filter_park.txt","w",encoding="utf-8") as file:
    file.write("남산공원(회현) 운동기구 설치 수\n")
    file.write(filter_park.to_string())
'''
#스텝사이클 설치 수
'''filter_equipment=df[df['운동기구 기종명']=="스텝사이클"]
print(filter_equipment)

with open("./1209/filter_equipment.txt","w",encoding="utf-8") as file:
    file.write("스텝사이클 설치 수\n")
    file.write(filter_equipment.to_string())'''

#운동기구 수량 내림차순 정렬
'''sort_df=df.sort_values(by="운동기구 수량",ascending=False)
print(sort_df)

with open("./1209/sort_df.txt","w",encoding="utf-8") as file:
    file.write("운동기구 수량 내림차순 정렬\n")
    file.write(sort_df.to_string())'''

