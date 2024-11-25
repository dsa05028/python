#print함수

'''print("안녕하세요")
print("Hello","python")
print("Hello","python", sep="|") #sep은 단어 사이에 문자 넣기
print("안녕하세요",end="/")
print("저는 조효정입니다.") #""안은 문자열(숫자를 넣어도 문자열로 인식), ""없이 숫자 입력 시 숫자로 인식
print(1111111)'''
# 여러줄 주석은 """코드""" 혹은 '''코드''' 사용

#input 함수
'''singer = input("좋아하는가수는? ") # 숫자 입력해도 문자열로 입력
print("좋아하는 가수는", singer, "입니다")'''

# #은 한 줄 주석에 사용, 코드 뒤에서도 사용가능

#변수 값 할당, 메모리 주소 확인 방법
'''x = 10
print("before x", id(x))
y, z = 3.14, "안녕하세요"
print("y", y)
print("z", z)
x = "반갑습니다"
print("after x", id(x)) # x값을 재할당
x = 10
print("after x", id(x)) # id()는 메모리 주소 확인 함수, 메모리 위치가 다름'''

'''a=[1,2,3] #리스트 : 여러개의 변수를 설정할 때 사용, 매서드를 써도 메모리 주소가 바뀌지 않음
print("before a", a, id(a)) 
a.append(4)
print("after a", a, id(a))'''


#키워드
'''import keyword
print(keyword.kwlist)'''

#산술연산자
'''x=48/2(9+3) #2와 (9+3)사이에 곱하기 연산자가 없음
print(x)'''

'''a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)'''
#연산순서와 괄호

'''x=100-2/7+9*3 
print(x) #126.71428571428571
x=(100-2)/7+9*3
print(x) #41.0'''

#대입연산자와 복합대입연산자
'''num=5
# += 5 ===> num = num+5 
num += 5 
print("+=",num)
num -= 2 #num=num-2
print("=+",num)
num *= 6 #num=num*6
print("*=",num)
num/=2 #num=num/2
print("/=",num) 
num//=5 #num=num//5
print("//=",num)
num%=3#num=num%3
print("%=",num)
num=4
num **=4 #num=num**4
print("**=", num)'''

#비교연산자
'''num1=10
num2=20
num3="10"
print(num1>num2)
print(num1<num2)
print(num1==num3) 
print(num1>=10)
print(num2<=19)
print(num1!=num3)'''

#논리연산자
'''a=2>1 #True
b=3<2 #False
c=1==1 #True
d=3>=4 #False
print(a and c) #True
print(a and d) #False
print(b or c) #True
print(b or d) #False
print(not a) #False
print(not d) #True'''

#in 연산자
'''a="Hello World"
print("H" in a) # T
print('h' in a) # F
print('a' not in a) #T
print('w' not in a) #F'''

#연산자 실습
'''x=int(input("숫자를 입력하세요:"))
x%=2
print("True면 짝수, False는 홀수",x==0)'''

#강사님
'''num=31
a=num%2==0
print("True면 짝수, False는 홀수", a)'''

x=5
y=x%2==0
print("True면 짝수, False면 홀수:",y)
