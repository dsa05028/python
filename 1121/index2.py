#리스트 기초
'''number=[1,2,3,"Hello","Python"]
print(number[3]) # number의 3번째 인덱싱값(Hello)를 출력

text="Hello, Python"
text=list(text) #리스트 아닌 것을 리스트로 변환
print(text) '''

#리스트 슬라이싱
'''shop=["반팔","청바지","이어폰",["무선키보드","기계식키보드"]] #리스트 안에 리스트 넣는것도 가능
print(shop[:2]) # 0<=shop<2
print(shop[3])
print(shop[-2])
shop[0]="긴팔" # 리스트 내 값 수정
print(shop)
#shop[100]="신발" #리스트는 순서가 중요해서 모든 인덱스가 다 채워져있어야한다.
#print(shop)
del shop[1]
print(shop)
del shop[2:]
print(shop)'''

#리스트 연산
'''a=[1,2,3]
b=["안녕하세요","반갑습니다"]
print(a+b) #중요
print(b*3)'''

#정렬함수 sorted()
'''num=[3,1,5,2]
num_asc=sorted(num)
print(num_asc) #[1, 2, 3, 5], 오름차순
num_dasc=sorted(num,reverse=True)
print(num_dasc) #[5, 3, 2, 1], 내림차순
print(num) #[3, 1, 5, 2], 원본은 유지
'''

#정렬 메서드 .sort()
'''num=[3,1,5,2]
num.sort()
print(num) #[1, 2, 3, 5], sorted함수와 달리 원본이 바뀜

korean=["강","이","박","최","김"]
korean.sort(reverse=True) #['최', '이', '박', '김', '강']
print(korean)'''

#정렬 메서드 .reverse()
'''alphabet=['b','c','a','d']
alphabet.reverse()
print(alphabet)'''

#위치찾기 메서드
'''alphabet=['b','c','a','d']
alphabet.reverse() #['d', 'a', 'c', 'b']
print(alphabet.index('c')) #2
print(alphabet.index('w')) #ValueError: 'w' is not in list
'''

#추가/삭제 메서드 매우중요!!!!
'''a=['a','b','c','안녕','Hi']
a.append("Good") #['a', 'b', 'c', '안녕', 'Hi', 'Good']
print(a)
a.pop() #['a', 'b', 'c', '안녕', 'Hi']
print(a)
a.pop() #['a', 'b', 'c', '안녕']
print(a) 
a.pop(2) #['a', 'b', '안녕']
print(a)
a.remove("안녕") #['a', 'b']
print(a)
a.insert(2,"잘가") #['a', 'b', '잘가']
print(a)
a.clear() #[]
print(a)'''

#개수 세기 메서드
'''x=['q','w','e','r','w'] #2 같은 이름 가진 요소 개수 세기
print(x.count('w'))'''

#실습.리스트 연습문제
'''rainbow=['red','orange','yellow','green','blue','indigo','purple']
print(rainbow[2])
rainbow.sort()
print(rainbow)
rainbow.append('navy')
print(rainbow)
del rainbow[3:7]
print(rainbow)'''

#실습.리스트 연습문제 강사님
'''rainbow=['red','orange','yellow','green','blue','indigo','purple']
print(rainbow[2])
sorted_rainbow=sorted(rainbow)
print(sorted_rainbow)
rainbow.append('pink')
print(rainbow)
del rainbow[3:7]
print(rainbow)'''

#이차원 리스트 
'''matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[2][0]) #7
#요소 추가
matrix[1]=matrix[1]+[99] #행을 지정해야함
print(matrix)
#행 추가
matrix=matrix+[[10,11,12]] #[[1, 2, 3], [4, 5, 6, 99], [7, 8, 9], [10, 11, 12]]
print(matrix)
#matrix=matrix+[10,11,12] #[[1, 2, 3], [4, 5, 6, 99], [7, 8, 9], [10, 11, 12], 10, 11, 12]
#print(matrix)
#요소 수정
matrix[0][0]=100
matrix[1][1]=500
print(matrix) #[[100, 2, 3], [4, 500, 6, 99], [7, 8, 9], [10, 11, 12]]
#행 삭제
del matrix[2]
print(matrix) #[[100, 2, 3], [4, 500, 6, 99], [10, 11, 12]]
#행의 개수
rows=len(matrix)
print(rows) #3
#열의 개수
cols=len(matrix[0])
print(cols) #3'''

#이차원 메서드
'''matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#요소 추가
matrix[0].append(10) #[[1, 2, 3, 10], [4, 5, 6], [7, 8, 9]]
print(matrix) 
#행 추가
matrix.append([10,11,12])
print(matrix) #[[1, 2, 3, 10], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#특정 위치에 삽입
matrix[1].insert(1,100)
print(matrix) #[[1, 2, 3, 10], [4, 100, 5, 6], [7, 8, 9], [10, 11, 12]]
#insert로 행 추가
matrix.insert(2,["안녕하세요","반갑습니다","어서오세요"]) #[[1, 2, 3, 10], [4, 100, 5, 6], ['안녕하세요', '반갑습니다', '어서오세요'], [7, 8, 9], [10, 11, 12]]
print(matrix) 
#extend(요소확장)
matrix[0].extend([11,12]) #[[1, 2, 3, 10, 11, 12], [4, 100, 5, 6], ['안녕하세요', '반갑습니다', '어서오세요'], [7, 8, 9], [10, 11, 12]]
print(matrix)'''

#튜플(tuple)
'''t1=(1,) #요소가 1개일 때 ','필수
t2=(1,2,3,4,5,3,3,3,3)
t3=1,2,3 #()없어도 튜플
t4=('a','b','c',("안녕","감사"))
print(t1[0])
print(t2.count(3))
print(t3.index(2))
print(t4[3][0])
print(len(t4))
print('d' in t4)
# t1.append(1) 튜플은 추가, 수정, 삭제 불가'''

#셋(set)
s1={1,1,1,1,1,1,1,2}
print(s1)
s2=['안녕','잘가','Hi','안녕']
print(set(s2))