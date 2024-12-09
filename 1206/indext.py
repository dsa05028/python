#pandas

#리스트 형식으로 Series 생성
import pandas as pd

'''data=[10,20,30,40]
# series=pd.Series(data)
series=pd.Series(data,index=["a","b","c","d"]) #인덱스 변경
print(series)'''

#딕셔너리 형식으로 생성
'''data={
    "a":10,
    "b":True,
    "c":3.14,
    "d":"python"
}

series=pd.Series(data,name="딕셔너리")
print(series) 
print(series.index)
print(series.values)
print(series.shape) # 몇 개의 딕셔너리로 구성되어있는가를 출력'''

'''data=("민지","여",False)
member=pd.Series(data,index=["이름","성별","결혼여부"])
# print(member)
# print(member["이름"])
print(member[["성별","결혼여부"]]) #일부분만 출력하려면 이차원리스트로 작성
'''
'''data=[10,20,30,40,50]
series=pd.Series(data,index=["a","b","c","d","e"])
# print(series[0])
print(series[series>20])
series["c"]=100
print(series)
'''

#실습. 시리즈 만들기

'''#리스트
data=["4 cups","1 cup","2 large","1 can"]
series=pd.Series(data, index=["밀가루","우유","계란","참치캔"], name="Dinner")
print(series)

#튜플
data=("4 cups","1 cup","2 large","1 can")
series=pd.Series(data, index=["밀가루","우유","계란","참치캔"], name="Dinner")
print(series)

#딕셔너리
data={
    "밀가루":"4 cups",
    "우유":"1 cup",
    "계란":"2 large",
    "참치캔":"1 can"
}
series=pd.Series(data, name="Dinner")
print(series)

#강사님
data=["4 cups","1 cup","2 large","1 can"]
index=["밀가루","우유","계란","참치캔"]
series=pd.Series(data, index=index, name="Dinner")
print(series)'''

#dataframe
'''data={
    'name':["홍길동","임꺽정","성춘향"],
    "age":[25,30,27],
    "city":["서울","부산","인천"]
}

df=pd.DataFrame(data)
print(df)'''

#인덱스값이 같을 때
'''index=["2020","2021","2022","2023","2024","2025"]

yeonghee=pd.Series([140,150,160,170,180,190], index=index)
cheolsu=pd.Series([200,210,220,230,240,250],index=index)

result=pd.DataFrame({
    '영희':yeonghee,
    "철수":cheolsu
})

#print(result)
# print(result.head())
# print(result.tail())
# print(result.shape)
# print(result.info())
# print(result.columns)
# print(result.values)
# print(result.index)
# print(result.dtypes)
# print(result["철수"])
# print(result[["철수"]])'''

#데이터프레임 필터링
'''data={
    'Name':["홍길동","임꺽정","성춘향"],
    "Age":[25,30,27],
    "city":["서울","부산","인천"]
}

df=pd.DataFrame(data,index=["a","b","c"])
# print(df)
# print(df.loc["b"])
# print(df.loc["b","age"])
# print(df.loc["a":"c","Name":"Age"])
# # print(df.loc[df['Age']>=30])
# print(df.loc[:,"Name"]) #:은 전체를 의미=>
# print(df.loc["a",:]) #a행에 있는 모든 열을 출력

# print(df.iloc[1])
# print(df.iloc[1,1])
# print(df.iloc[0:2,0:2])#끝값포함안됨
# print(df.iloc[[0,2],[1,2]])
# print(df.iloc[:,0])
print(df.iloc[0,:])'''

'''data={
    'Name':["홍길동","임꺽정","성춘향"],
    "Age":[25,30,27],
    "City":["서울","부산","인천"]
}

df=pd.DataFrame(data)
#행추가
new_data={"Name":"이몽룡","Age":31,"City":"포항"}
result=pd.concat([df,pd.DataFrame([new_data])],ignore_index=True)
# print(result)

#열추가
result["직업"]=["엔지니어","개발자","디자이너","기획자"]
# print(result)

#요소 값 수정
result.at[1,"City"]="천안"
result.loc[result["Name"]=="임꺽정","Age"]=32
# print(result)

#column 변경
result.rename(columns={"Name":"이름","Age":"나이"},inplace=True)
# print(result)

#데이터 정렬(내림차순)
result.sort_values(by="나이",inplace=True,ascending=False)
# print(result)

#column 삭제
result.drop(columns=["City"],inplace=True)
# print(result)
'''

#실습. 데이터프레임 만들기
'''data={
    "이름":["홍길동","임꺽정","성춘향"],
    "수학":[85,90,78],
    "영어":[88,76,92],
    "과학":[95,89,84]
}

df=pd.DataFrame(data)
print(df)
new_row={"이름":"이몽룡","수학":88,"영어":85,"과학":90}
result=pd.concat([df,pd.DataFrame([new_row])],ignore_index=True)
# print(result)
result.loc[result["영어"]==76,"영어"]=80
# print(result)
result["Total"]=result["수학"]+result["영어"]+result["과학"]
# print(result)
result.rename(columns={"수학":"Math"},inplace=True)
print(result)'''








