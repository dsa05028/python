#전역변수 : 상수쓸때 많이 사용
'''quantity=10

def get_price(price):
    price=price*quantity
    return price

print(f"{quantity}개의 가격은 {get_price(5000)}입니다")'''

#지역변수
'''def oneUp():
    x=0 #매개변수도 전역변수
    x+=1 
    return x

print(oneUp())'''

#유효범위
'''quantity=10

def price_sum(price):
    quantity=7 #전역변수=지역변수, 우선순위:지역변수>전역변수
    return price*quantity

print(price_sum(2000)) #14000

quantity=10

def price_sum(price):
    return price*quantity

print(price_sum(2000)) #20000'''

#global 키워드
'''x=0

def oneUp():
    x +=1 #전역변수를 함수 내부에서 변경 시도
    return x
print(oneUp()) #UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
print(oneUp())
print(oneUp()) 
'''
'''
def oneUp():
    global x
    x += 1
    return x
print(oneUp())
print(oneUp()) 
print(oneUp())
print(x)
'''
'''def oneUp():
    global x
    x = 1
    return x
print(oneUp())
print(oneUp()) 
print(oneUp())
print(x)
'''
#기본 매개변수
'''def pr_str(txt="안녕하세요",count=1):
    for _ in range(count):
        print(txt)

pr_str() #안녕하세요
pr_str("hello",5)
pr_str("hi")
pr_str(5) # 순서대로 txt에 5가 들어감, count만 바꿀수는 없음
'''

#함수 호출 키워드
'''def intro(name, age, city):
    print(f"이름은 {name}이고 나이는 {age}이고 사는 곳은 {city}입니다.")

intro("홍길동",23,"서울") #이름 나이 사는 곳 순서대로 값을 전달
intro(city="서울",name="임꺽정",age=25) #함수 호출 키워드를 사용하면 순서에 상관없이 값을 전달할 수 있다
intro("홍길동",city="부산",age=25) #키워드와 혼합 사용 시 키워드 사용 안하는 순서대로 해야함
intro(city="부산",age=25,"홍길동") #SyntaxError: positional argument follows keyword argument
'''

#가변 위치 매개변수
'''def calc_avg(*args):
    print(args) #튜플 형태로 반환
    total=0
    for i in args:
        total+=i
    avg=total/len(args)
    return avg

print(calc_avg(1,2,3,4,5,6,7,8))
'''

'''def text_def(a, b, *args): #가변함수를 먼저 쓸수없다. 
    print("text:",a)
    print("b:",b)
    print("args:",args)

text_def("hi",1,2,3,4,5) # 순서대로 고정되고 나머지가 가변 매개변수에 전달됨
'''

#가변 키워드 매개변수
'''def intro(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
intro(name="홍길동",age=20,city="서울",gender="남자")
'''

#내장함수
#abs(정수)=절댓값을 구하는 내장함수
'''def my_abs(x):
    if x<0:
        return -x
    else:
        return x

print(my_abs(-10))
print(my_abs(5))
print(abs(-10))'''

##거듭제곱
'''print(pow(2, 3)) #pow(a,b):a를 b번 곱한다

def my_pow(x,y):
    num=1
    for i in range(y):
        print(f"i={i},{num*x}={num}*{x}")
        num*=x
    return num

print(my_pow(3,4))
'''

##map()
'''def square(x):
    return x**3

numbers=[2,4,6,8]

squared=list(map(square,numbers))
print(squared) #[8, 64, 216, 512]
squared=map(square,numbers)
print(squared) #메모리 주소값 반환, <map object at 0x0000019739C0B7F0>
'''

##filter()
'''def even_number(x):
    return x%2==0

numbers=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(even_number,numbers))) #[2, 4, 6, 8, 10]'''

#여러 개 한꺼번에 반환
'''def get_return():
    arr=["사과","바나나"]
    dic={
        "name":"홍길동",
        "age":20
    }
    num=30
    return arr, dic, num
arrs,dits,nums=get_return() #return 뒤에 있는 변수 순서대로 받는 변수도 순서를 맞춰야한다.
print(arrs)
print(dits)
print(nums)'''

#실습4. 함수만들기

'''def multi_number(x,y):
    return x%y==0
            
numbers=[
    1,2,3,4,5,6,7,8,9,10,
    11,12,13,14,15,16,17,18,19,20,
    21,22,23,24,25,26,27,28,29,30 
]

multi_numbers=list(filter(multi_number,numbers))
print(multi_numbers)
print(f"3의 배수의 개수: {len(multi_numbers)}")'''

##챗gpt
'''def find_multiples_and_count(n, start=1, end=30):

    multiples = [i for i in range(start, end + 1) if i % n == 0]
    
    print(list(map(str, multiples)))
    print(f"{n}의 배수의 개수: {len(multiples)}")

find_multiples_and_count(3)'''

## 실습4. 강사님1
'''def count(num):
    lists=[i for i in range(1,31) if i%num==0 ] #리스트 내포 사용
    counts=len(lists)
    return lists, counts

num=2
lists, counts=count(num)
print(f"{num}의 배수:{lists}")
print(f"{num}의 개수는: {counts}")'''

## 실습4. 강사님2
'''def count(num):
    #중첩 함수-이 함수 내에서만 사용가능
    def check(x):#=>람다식으로 표현가능
        return x%num==0
    lists=list(filter(check,range(1,31)))
    return lists, len(lists)

num=5
lists, counts=count(num)
print(f"{num}의 배수:{lists}")
print(f"{num}의 개수는: {counts}")'''

#재귀함수
'''def sos(i):
    print("help me!",i)
    if i==1:
        return ""
    else:
        return sos(i-1)

sos(10)'''

##팩토리얼
'''def factorial(n):
    print("n의 값",n)
    if n==1:
        return 1
    else :
        return n*factorial(n-1)

print(factorial(3))'''

#실습5. 피보나치 수열 만들기(코딩테스트 빈출 문제)

'''def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
    
print(fibonacci(3))'''


'''n=int(input("숫자를 입력하세요"))
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    a=0
    b=1
    for _ in range(n):
        a,b= b, a+b
    print(a)
'''

#실습5. 피보나치 수열 만들기(코딩테스트 빈출 문제) 강사님
'''def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        print(f"{fibonacci(n-1)}+{fibonacci(n-2)}")
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(3))'''
#=>알고리즘적으로 좋은 코드는 아님

#람다식
'''##일반함수 
def add(x,y):
    return x+y
print(add(3,4))
##람다식
add=lambda x,y:x+y
print(add(4,5))'''

#매개변수 1개 람다식
'''oneup=lambda x: x+1
print(oneup(1))
print((lambda x: x+1)(2))

square=lambda x:x**2
print(square(4))
print((lambda x:x**2)(5))
'''
#매개변수 2개 람다식
'''minus=lambda x,y:x-y
print(minus(10,2))
print((lambda x,y:x-y)(7,4))'''

#람다함수를 매개변수로 전달
'''def call(func):
    for _ in range(10):
        func()

def hello():
    print("안녕하세요")

hello2=lambda :print("반갑습니다") #한줄 출력이면 람다 함수가 더 적합
call(hello2)'''

'''numbers=[2,4,6,8]
squared=map(lambda x:x**3,numbers)
print(list(squared))

numbers=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2==0,numbers)))'''

##filter()
'''def even_number(x):
    return x%2==0

numbers=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(even_number,numbers))) #[2, 4, 6, 8, 10]'''

#실습4.람다식 사용
'''def count(num):
    lists=list(filter(lambda x:x%num==0,range(1,31)))
    return lists, len(lists)

num=5
lists, counts=count(num)
print(f"{num}의 배수:{lists}")
print(f"{num}의 개수는: {counts}")'''

#실습. 함수 종합 프로그래밍

weather_data=[
    ["2024-11-20","서울",15.2,0.0],
    ["2024-11-20","부산",18.4,0.0],
    ["2024-11-21","서울",10.5,2.3],
    ["2024-11-21","부산",14.6,1.2],
    ["2024-11-22","서울",8.3,0.0],
    ["2024-11-22","부산",12.0,0.0]
]

def calc_avg_tem(city):
    #n=input("도시를 입력하세요. ")
    temperatures = [record[2] for record in weather_data if record[1] == city]
    if temperatures:
        avg = sum(temperatures) / len(temperatures)
        print(f"{city}의 평균기온: {avg:.2f}°C")
    else:
        print("없는 도시입니다.")

def max_min(city):
    temperatures = [record[2] for record in weather_data if record[1] == city]
    if temperatures:
        max_tem = max(temperatures)
        min_tem = min(temperatures)
        print(f"{city}의 최고 기온: {max_tem}°C, 최저 기온: {min_tem}°C")
    else:
        print("없는 도시입니다.")

def precipitation (city):
    precipitation = [record[3] for record in weather_data if record[1] == city]
    if precipitation:
        total_rain = sum(precipitation)
        print(f"{city}의 총 강수량: {total_rain:.2f}mm")
    else:
        print("없는 도시입니다.")
    
def add_weater_data():
    global weather_data
    if x==4 or x=="날씨 데이터 추가":
        date=input("날짜를 입력하세요(YYYY-MM-DD):")
        city=input("도시를 입력하세요")
        temperature=float(input("기온을 입력하세요"))
        precipitation=float(input("강수량을 입력하세요"))
        weather_data.append([date,city,temperature,precipitation])
        return weather_data
    else:
        print("잘못된 입력입니다.")


def printdata():
    return weather_data

x=int(input("원하는 기능의 번호를 입력하세요:"))
while True:
    if x==1:
        city=input("도시 이름을 입력하세요:")
        calc_avg_tem(city)
    elif x==2:
        city=input("도시 이름을 입력하세요:")
        max_min(city)
    elif x==3:
        city=input("도시 이름을 입력하세요:")
        precipitation(city)
    elif x==4:
        city=input("도시 이름을 입력하세요:")
        add_weater_data()
    elif x==5:
        print(printdata())
    elif x==6:
        print("종료")
    else:
        print("번호를 다시 입력해주세요")


#실습 hint:도시 필터링
'''city="서울"
x=[
    ["서울",10],
    ["서울",20],
    ["부산",30]
]

a=filter(lambda x:x[0]==city,x)
print(list(map(lambda x:x[1],a)))'''

