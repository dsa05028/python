#질문
#메서드는 원본 데이터가 변하기 때문에 print()에 직접적으로 쓸수없음
'''x=['q','w','e','r','w']
print(sorted(x)) #['e', 'q', 'r', 'w', 'w']
print(x.sort()) #None
x.append('a')
print(x) #['e', 'q', 'r', 'w', 'w', 'a']
print(x.append('w')) #None
'''

#<set 메서드>
'''s1={1,2,3,3,4}
print(s1) #{1, 2, 3, 4}
s1.add(5)
print(s1) #{1, 2, 3, 4, 5}
s1.update([6,7,8,9,10])
print(s1) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s1.remove(3)
print(s1) #{1, 2, 4, 5, 6, 7, 8, 9, 10} 
s1.discard(9)
print(s1) #{1, 2, 4, 5, 6, 7, 8, 10}
#s1.remove(11)
#print(s1) #KeyError: 11
s1.discard(11)
print(s1) #{1, 2, 4, 5, 6, 7, 8, 10}
s1.clear()
print(s1) #set()
'''

#<set 연산>
#합집합
'''s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3=s1|s2 #합집합
print(s3) #{1, 2, 3, 4, 5, 6, 7, 8}
s4=s1.union(s2) #합집합
print(s4)
'''

#교집합
'''s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3=s1&s2
print(s3) #{4, 5}
s4=s1.intersection(s2)
print(s4)
'''

#차집합
'''s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3=s1-s2
print(s3) #{1, 2, 3}
s5=s1.difference(s2)
print(s5)
s4=s2-s1 #{1, 2, 3}
print(s4) #{8, 6, 7}
s6=s2.difference(s1)
print(s6) #{8, 6, 7}'''

#<딕셔너리(Dictionary)>
#생성
'''dict1={} 
dict1=dict() #딕셔너리 함수 사용
print(dict1) #{}'''

'''dict1={
    "name":"홍길동",
    "age":20,
    "city":"서울",
    "hobby":["런닝","등산","헬스"] #리스트도 가능
} #key값은 문자열 형태, 숫자로 해도 무관하나 키값은 변수로 사용하기 때문에 숫자로 하면 혼동될 수 있음
print(dict1) #{'name': '홍길동', 'age': 20, 'city': '서울', 'hobby': ['런닝', '등산', '헬스']}
dict2=dict(name="홍길동",age=20) #dict 함수를 이용하여 추가, 함수사용 지양
print(dict2) #{'name': '홍길동', 'age': 20}
print(dict1['name']) #홍길동, 키값을 이용해 벨류값 접근가능->키값은 중복x
print(dict1['hobby'][2]) #리스트 2번째 값(헬스) 접근
''' 
#값 수정

'''dict1={
    "name":"홍길동",
    "age":20,
    "city":"서울",
    "hobby":["런닝","등산","헬스"] #리스트도 가능
}
dict1["age"]=21
print(dict1) #{'name': '홍길동', 'age': 21, 'city': '서울', 'hobby': ['런닝', '등산', '헬스']}
''' 
#값 추가
'''dict1={
    "name":"홍길동",
    "age":20,
    "city":"서울",
    "hobby":["런닝","등산","헬스"] #리스트도 가능
}
dict1["birthday"]=20001011
print(dict1) #{'name': '홍길동', 'age': 20, 'city': '서울', 'hobby': ['런닝', '등산', '헬스'], 'birthday': 20001011}
dict1["hobby"]=['런닝', '등산', '헬스',"캠핑"]
print(dict1)  #{'name': '홍길동', 'age': 20, 'city': '서울', 'hobby': ['런닝', '등산', '헬스', '캠핑'], 'birthday': 20001011}
dict1["hobby"]="캠핑" #{'name': '홍길동', 'age': 20, 'city': '서울', 'hobby': '캠핑', 'birthday': 20001011
print(dict1)
del dict1["birthday"]
print(dict1) #{'name': '홍길동', 'age': 20, 'city': '서울', 'hobby': '캠핑'}
''' 

#딕셔너리 메서드
'''fruits={
    "apple":"사과",
    "banana":"바나나"
}
print(fruits.get('apple')) #사과
print(fruits.get('peach')) #None
print(fruits.get('peach','복숭아')) #복숭아
'''

#여러요소추가
'''fruits.update({
    'grape':"포도",
    'melon':'멜론'
})
print(fruits) #{'apple': '사과', 'banana': '바나나', 'grape': '포도', 'melon': '멜론'}
print(fruits.keys()) #dict_keys(['apple', 'banana', 'grape', 'melon'])
print(fruits.values()) #dict_values(['사과', '바나나', '포도', '멜론'])
print(fruits.items()) #dict_items([('apple', '사과'), ('banana', '바 나나'), ('grape', '포도'), ('melon', '멜론')])
fruits.clear()
print(fruits) #{}
'''

#실습.성적관리
'''dict1={
    'Alice':85,
    'Bob':90,
    'Charlie':95
}
print(dict1) #{'Alice': 85, 'Bob': 90, 'Charlie': 95}
dict1.update({
    'David':80
})
print(dict1) #{'Alice': 85, 'Bob': 90, 'Charlie': 95, 'David': 80}
dict1['Alice']=88
print(dict1) #{'Alice': 88, 'Bob': 90, 'Charlie': 95, 'David': 80}
del dict1['Bob']
print(dict1) #{'Alice': 88, 'Charlie': 95, 'David': 80} 
'''

#실습.성적관리 강사님.ver
'''students={}
students['Alice']=85
students['Bob']=90
students['Charlie']=95
students['David']=80
students['Alice']=88
del students['Bob']
print(students) #{'Alice': 88, 'Charlie': 95, 'David': 80} 
'''

#<내장함수>
#sum
'''numbers=[1,2,3,4,5]
print(sum(numbers)) #15

scores={'국어':90,'영어':80,'수학':85}
print(sum(scores.values())) #255'''

#zip
'''names=['Alice','Bob','Charlie','David']
scores=[85,90,88,95]
zipped=list(zip(names,scores)) #list()를 이용하여 변환, [('Alice', 85), ('Bob', 90), ('Charlie', 88), ('David', 95)] 튜플 형태
print(zipped) #zip만 썼을 때 : <zip object at 0x0000018AEF4BB800>
'''

