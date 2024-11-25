#함수

'''def say_hello(born,name):
    age=2024-born
    print(f"{name}님의 나이는 {age}입니다.")

say_hello(2000,"민지") #나이는 24입니다.
say_hello(2001,"혜린")'''

#곱셈함수
'''def gugudan(dan,end):
    print(f"{dan}단")
    for i in range(1,end+1):
        print(f"{dan} * {i}={dan*i}")
gugudan(4,20)
gugudan(7,50)'''

#결과값이 있는 함수
'''def calc_sum(num1, num2):
    total=0
    for i in range(num1,num2+1):
        total+=i
    return total

result = calc_sum(1,10)
print(result)'''

#리스트 반환
'''def fruits():
    return ["사과","바나나","복숭아"]

print(fruits())

def students():
    return{
        "name":"홍길동",
        "age":20,
        "major":"컴퓨터공학"
    }
print(students())'''

#실습1.
'''def add(num1,num2):
    if num1==num2:
        print("결과(곱):",num1*num2)
    else:
        print("결과(합):",num1+num2)

add(2,2)
add(2,3)'''

#실습1. 강사님
'''def multi_or_add(num1,num2):
    if num1==num2:
        return num1*num2 #return 쓰는 습관을 들여야함
    else:
        return num1+num2
    
result1=multi_or_add(2,2)
result2=multi_or_add(2,3)
print("결과(곱):",result1)
print("결과(합):",result2)'''

#실습2.
'''def delivery(item,price):
    if price<20000:
        print(f"{item} 가격:{price+2500}원")
    else:
        print(f"{item} 가격:{price}원")

delivery("상품1",30000)
delivery("상품2",15000)'''

#실습2. 강사님
'''def calc_price(price):
    total=0 #total 초기화는 생략가능
    fee=2500
    if price<20000:
        total=price+fee
    else:
        total=price
    return total
result=calc_price(15000)
result1=calc_price(30000)
print(f"상품가격은 {result}원")
print(f"상품가격은 {result1}원")'''

#매개변수로 리스트 전달
'''def times(nums):
    return [i**2 for i in nums]
number=[2,3,6,9]
print(times(number))'''

#실습.자판기 프로그램 함수화
'''vending_machine=["게토레이","게토레이","레쓰비","생수","생수","생수","이프로"]

def check_machine():
    return vending_machine

def is_drink(drink):
    if drink in vending_machine: #있으면 제거
        vending_machine.remove(drink)
        return drink, vending_machine
    else:
        print("음료수가 없습니다.")

def add_drink(drink):
    vending_machine.append(drink)
    print("추가 완료")
    return vending_machine

def remove_drink(drink):
    if drink in vending_machine:
        vending_machine.remove(drink)
        return vending_machine
    else:
        print(f"{drink}는 현재 없습니다.")
'''

#실습.자판기 프로그램 함수화

def check_machine():
    print("남은 음료수 :",vending_machine)

def is_drink(drink):
    return drink in vending_machine

def add_drink(drink):
    vending_machine.append(drink)
    print("추가 완료")

def remove_drink(drink,user_input):
    if user=="1"or user=="소비자":
        vending_machine.remove(drink)
        print(f"{drink}를 드릴게요")
    else:
        vending_machine.remove(drink)
        print(f"{drink} 삭제 완료")
        
    

vending_machine=["게토레이","게토레이","레쓰비","생수","생수","생수","이프로"]
user_input=input("사용자를 선택하세요.(1.소비자 2.주인 3.종료)")

while True:

    if user_input=="1"or user_input=="소비자":
        drink=input("마시고 싶은 음료는?")
        if is_drink(drink): #있으면 제거
            remove_drink(drink,user_input)
        else:
            print("음룓수가 없습니다.")
        print("남은 음료수 :",vending_machine)

    elif user_input=="2" or user_input=="주인":
        move=input("할일을 선택하세요.(1. 추가 2. 삭제):")
        if move=="1"or move=="추가":
            drink=input("추가할 음료수는?:")
            add_drink(drink)
        elif move=="2"or move=="삭제":
            drink=input("삭제할 음료수는?")
            if is_drink(drink):
                remove_drink(drink,user_input)
            else:
                print(f"{drink}는 현재 없습니다.")
        else:
            print("값을 잘못 입력하셨습니다.")
        print("남은 음료수 :",vending_machine)
            
    elif user_input=="3" or user_input=="종료":
        print("자판기 프로그램을 종료합니다")
        break
    else:
        print("값을 잘못 입력하셨습니다.")

