import pandas as pd

#결측값
'''data={
    "Name":["홍길동","임꺽정","성춘향"],
    "Age":[25,None,20],
    "City":["Seoul","Busan",None]
}

df=pd.DataFrame(data)
print(df)
# print(df.isnull())
# print(df.isnull().sum())
# print(df.info())
# df_drop=df.dropna() # 행 삭제
# print(df_drop)
# df_drop_column=df.dropna(axis=1) # 열 삭제
# print(df_drop_column)
# df_fill=df.fillna(0)
# print(df_fill)
# df_fill_f=df.fillna(method="ffill") # 이전 값으로 결측값 채우기
# print(df_fill_f)
# df_fill_b=df.fillna(method="bfill") #다음 값으로 결측값 채우기
# print(df_fill_b)'''

#isin() 매서드
'''s=pd.Series(["홍길동","임꺽정","성춘향","이몽룡"])
result=s.isin(["홍길동","이몽룡"])
print(result)'''

'''data={
    "Name":["홍길동","임꺽정","성춘향","이몽룡"],
    "Age":[25,30,20,32]
}

df=pd.DataFrame(data)
# result=df.isin(["성춘향","홍길동",20]) #true/false 찾기
result=df[df["Name"].isin(["성춘향","홍길동",32])] #true값만 필터링
print(result)'''

'''s=pd.Series([1,2,None])
result=s.isin([None,2]) #결측값을 무시하기 때문에 false출력
print(result)'''

#value_counts() 매서드
'''s=pd.Series(["사과","바나나","사과","오렌지","바나나","사과"])
print(s.value_counts())'''

'''df=pd.DataFrame({
    "과일":["사과","바나나","사과","오렌지",None,"사과"],
    "수량":[1,2,3,4,5,6]
})
# print(df["과일"].value_counts())
# print(df["과일"].value_counts(normalize=True)) #빈도율 비율(%)
# print(df["과일"].value_counts(ascending=True)) #오름차순
print(df["과일"].value_counts(dropna=False))
'''

#agg() 메서드
'''s=pd.Series([1,2,3,4,5])
result=s.agg(["sum","mean","max"])
print(result)'''

'''df=pd.DataFrame({
    "A":[1,2,3],
    "B":[10,11,12]
})

# print(df.agg(["sum","mean"]))
print(df.agg({"A":"sum","B":"mean"}))'''

'''s1=pd.Series([10,20,30])
s2=pd.Series([5,15,25])

# print(s1+s2)
# print(s1-s2)
# print(s1*s2)
# print(s1/s2)
# print(s1>15)

#통계연산
# print(s1.sum())
# print(s1.mean())
# print(s1.max())
# print(s1.min())
# print(s1.std()) #표준편차
# print(s1.var()) #분산
# print(s1.median()) #중앙값
# print(s1.describe()) #통계지표'''

#그룹화
'''data={
    "group":["A","A","B","B","C"],
    "value":[10,20,30,40,50]
}

df=pd.DataFrame(data)
# result=df.groupby("group")["value"].sum() 
result=df.groupby("group")["value"].agg(["sum","mean","max"])
print(result)'''

data={
    "group":["A","A","B","B","C"],
    "value1":[10,20,30,40,50],
    "value2":[5,15,25,35,45]
}

df=pd.DataFrame(data)
# result=df.groupby("group").agg({
#     "value1":"sum",
#     "value2":"mean"
# })
# result=df.groupby("group").agg({
#     "value1":"sum",
#     "value2":["mean","sum"]
# })
result=df.groupby("group").filter(lambda x :x["value1"].sum()>30)
print(result)
