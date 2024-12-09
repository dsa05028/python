#<클래스>

#클래스 정의
'''class Car: #클래스 이름은 대문자로 시작
    model=""
    cc=0

#클래스 사용
car1=Car() #인스턴스 생성
car1.model="싼타페"
car1.cc=2000

print(f"모델명:{car1.model}")
print(f"배기량:{car1.cc}cc")'''

#클래스 함수(매서드)
'''class Car: #클래스 이름은 대문자로 시작
    model=""
    cc=0

    #함수추가
    def info(self):
        print(f"모델명:{self.model}, 배기량:{self.cc}cc") 

        car1=Car() #인스턴스 생성

car1=Car() #인스턴스 생성
car1.model="싼타페"
car1.cc=2000

car1.info()'''

#<특수 매서드>
#1. 생성자(constructor)가 존재할 때
'''class Car: #클래스 이름은 대문자로 시작
    def __init__(self,model,cc):
        self.model=model
        self.cc=cc

    def info(self):
        print(f"모델명:{self.model}, 배기량:{self.cc}cc") 


car1=Car("싼타페",2000) #인스턴스 생성
car2=Car("BMW",2000)
car1.info()
car2.info()'''

#2. def __str__+3. 객체 리스트
'''class Car: #클래스 이름은 대문자로 시작
    def __init__(self,model,cc):
        self.model=model
        self.cc=cc

    def __str__(self) -> str:
        return f"모델명:{self.model}, 배기량:{self.cc}cc"

car1=Car("싼타페",2000) #인스턴스 생성
car2=Car("BMW",2000)
print(car1)
print(car2)'''

'''print("===============승용차리스트===============")
cars=[
    Car("소나타",2000),
    Car("쏘렌토",3000),
    Car("아반떼",1600),
]
print(cars[0])
for car in cars:
    print(car)'''

#실습1. 사칙연산 클래스 만들기1
'''class Numerical_expression:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

    def add(self):
        print(f"{self.x}+{self.y}={self.x+self.y}")

    def sub(self):
        print(f"{self.x}-{self.y}={self.x-self.y}")

    def mul(self):
        print(f"{self.x}*{self.y}={self.x*self.y}")

    def div(self):
        print(f"{self.x}/{self.y}={(self.x/self.y):.2f}")

x1=Numerical_expression(5,4)
x1.add()
x1.sub()
x1.mul()
x1.div()'''

#실습1. 사칙연산 클래스 만들기2
'''class Numerical_expression:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

    def add(self):
        return self.x+self.y

    def sub(self):
        return self.x-self.y

    def mul(self):
        return self.x*self.y

    def div(self):
        return self.x/self.y

x1=Numerical_expression(5,4)
print(x1.add())
print(x1.sub())
print(x1.mul())
print(x1.div())'''

#실습1. 사칙연산 클래스 만들기 강사님
'''class Calculator:
    def __init__(self,num1,num2) -> None:
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1+self.num2
    
    def sub(self):
        return self.num1-self.num2
    
    def mul(self):
        return self.num1*self.num2
    
    def div(self):
        if self.num2==0: #함수, 매서드 정의 시 오류조건을 먼저 처리
            return "분모가 0이 될 수 없습니다." #num2==0일 때 "문자열"이 반환되므로 
        return self.num1/self.num2 #else를 굳이 쓰지 않아도 된다.
    
calc=Calculator(10,7)
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())'''

'''class Calculator:
    def __init__(self,num1,num2) -> None:
        self.num1=num1 #인스턴스 변수
        self.num2=num2
    
    def add(self,num):
        return self.num1+self.num2+num
    
    def sub(self):
        return self.num1-self.num2
    
    def mul(self):
        return self.num1*self.num2
    
    def div(self):
        if self.num2==0: #함수, 매서드 정의 시 오류조건을 먼저 처리
            return "분모가 0이 될 수 없습니다." #num2==0일 때 "문자열"이 반환되므로 
        return self.num1/self.num2 #else를 굳이 쓰지 않아도 된다.
    
calc=Calculator(10,7)
print(calc.add(5))
print(calc.sub())
print(calc.mul())
print(calc.div())'''

#클래스변수와 인스턴스변수
'''class Dog:
    kind="진돗개" #클래스 변수

    def __init__(self,name) -> None:
        self.name=name #인스턴스 변수

#1. 인스턴스변수 접근
dog1=Dog("백구")
dog2=Dog("초코")
print(dog1.name)
print(dog2.name)

#2.클래스변수 접근
# print(dog1.kind) #사용안함
# print(dog2.kind) #사용안함
print(Dog.kind)'''

#3.
'''class Example:
    shared="공유 변수" #클래스변수

    def __init__(self,name):
        self.name=name #인스턴스변수

e1=Example("A")
e2=Example("B")
Example.shared="변경된 공유 변수"
print(e1.shared)
print(e2.shared)
e1.name="C"
print(e1.name)
print(e2.name)
'''

#4. 사번 자동부여 클래스
'''class Employee:
    serial_num=1000 #클래스변수

    def __init__(self,name) -> None:
        Employee.serial_num+=1 #클래스변수는 self사용안해도 됨, 클래스변수를 1씩 증가가
        self.id=Employee.serial_num #사번
        self.name=name

    def __str__(self) -> str:
        return f"사번:{self.id}, 이름:{self.name}"

e1=Employee("홍길동")
print(e1)
e2=Employee("임꺽정")
print(e2)
employees=[Employee("이몽룡"),Employee("심청이"),Employee("변사또"),Employee("전우치")]
for employee in employees:
    print(employee)'''

'''class Employee:

    def __init__(self,name) -> None:
        self.serial_num=1000
        self.serial_num+=1
        self.id=self.serial_num
        self.name=name

    def __str__(self) -> str:
        return f"사번:{self.id}, 이름:{self.name}"

e1=Employee("홍길동")
print(e1)
e2=Employee("임꺽정")
print(e2)
employees=[Employee("이몽룡"),Employee("심청이"),Employee("변사또"),Employee("전우치")]
for employee in employees:
    print(employee)'''

#실습2.Supermarket 클래스
'''class Supermarket:

    def __init__(self,location,name,product,customer) -> None:
        self.location=location
        self.name=name
        self.product=product
        self.customer=int(customer)
    
    def print_location(self):
        return self.location

    def change_category(self,new_product):
        self.product=new_product

    def show_list(self):
        return self.product

    def enter_customer(self):
        self.customer+=1
        return self.customer

    def show_info(self):
        return f"위치:{self.location}, 가게이름:{self.name}, 상품:{self.product}, 손님 수:{self.customer}"

s1=Supermarket("마포구 염리동","마켓온","음료","11")
print(f"위치:{s1.print_location()}")
s1.change_category("과자")
print(f"상품:{s1.show_list()}")
s1.enter_customer()
print(s1.show_info())'''

#실습2.Supermarket 클래스
'''class Supermarket:
    def __init__(self,location,name,product,customer) -> None:
        self.location=location
        self.name=name
        self.product=product
        self.customer=customer

    def print_location(self):
        print(f"위치: {self.location}")

    def change_category(self,new_product):
        self.product=new_product

    def show_list(self):
        print(f"상품: {self.product}")

    def enter_customer(self):
        self.customer+=1

    def show_info(self):
        print(f"위치:{self.location}, 이름:{self.name}, 상품:{self.product}, 고객수:{self.customer}")
s1=Supermarket("마포구 염리동","마켓온","음료",12)
s2=Supermarket("은평구 응암동","응암마켓","과자",9)
s1.print_location()
s1.enter_customer()
s1.show_list()
s1.show_info()
s2.show_info()'''

'''class Supermarket:
    total_customer=0

    def __init__(self,location,name,product,customer) -> None:
        self.location=location
        self.name=name
        self.product=product
        self.customer=customer
        Supermarket.total_customer+=customer

    def print_location(self):
        print(f"위치: {self.location}")

    def change_category(self,new_product):
        self.product=new_product

    def show_list(self):
        print(f"상품: {self.product}")

    def enter_customer(self):
        Supermarket.total_customer+=1

    def show_info(self):
        print(f"위치:{self.location}, 이름:{self.name}, 상품:{self.product}, 고객수:{Supermarket.total_customer}")
s1=Supermarket("마포구 염리동","마켓온","음료",12)
s2=Supermarket("은평구 응암동","응암마켓","과자",9)
s1.print_location()
s2.enter_customer()
s1.enter_customer()
s1.show_list()
s1.show_info()
s2.show_info()
'''

#정보은닉
'''class Person:
    def __init__(self) -> None:
        self._name=""
        self._age=0
    #이름을 설정
    def setname(self,name):
        self._name=name
    #이름을 출력
    def getname(self):
        return self._name
    #나이를 설정
    def setage(self,age):
        self._age=age
    #나이를 출력
    def getage(self):
        return self._age
p1=Person()
p1.setname("홍길동")
print(p1.getname())
p1.setage(20)
print(p1.getage())'''

#실습3. 건강상태 만들기
class Hp:
    def __init__(self,name) -> None:
        self._name=name
        self._hp=100
    #이름을 설정
    def setname(self,name):
        self._name=name
    #이름을 출력
    def getname(self):
        return self._name
    #운동hp설정
    def setexercise(self,hours):
        self._hp+=hours
    #운동hp출력 
    def getexercise(self):
        return self._hp
    #술hp설정
    def setdrink(self,drink):
        self._hp-=drink
    #술hp출력
    def getdrink(self):
        return self._hp

            
p1=Hp("나몸짱")
p1.setexercise(5)
p1.setdrink(2)
print(f"{p1.getexercise()}시간 운동하다")
print(f"술을 {p1.getdrink()}잔 마시다")
print(f"{p1.getname()}-hp:{100+p1.getdrink()+p1.getexercise()}")
print()
p2=Hp("나약해")
p2.setexercise(1)
p2.setdrink(12)
print(f"{p2.getexercise()}시간 운동하다")
print(f"술을 {p2.getdrink()}잔 마시다")
print(f"{p2.getname()}-hp:{100+p2.getdrink()+p2.getexercise()}")
print()
