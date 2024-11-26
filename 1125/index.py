#<for문>
#리스트와 for문
'''fruits=["사과","포도","바나나","복숭아"]
for fruit in fruits: #리스트 내 요소들을 반복하여 출력
    print("과일은",fruit)'''

'''과일은 사과
과일은 포도
과일은 바나나
과일은 복숭아'''

#합계 구하기
'''number=[10,20,30,40,50]
total=0
for num in number:
    total+=num
print(f"리스트 값의 합계는{total}입니다.") #리스트 값의 합계는150입니다.
'''

#조건문 사용
'''number=[1,2,3,4,5,6,7,8,9]
for num in number: #for문 종료조건 필요없음
    if num%2==0:
        print(num,end=" ") #2468
'''

#리스트 내포
'''squares=[i**2 for i in range(1,20)] #너무 복잡한건 안됨
print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
'''

#if문과 함께 사용, if문은 선택적
'''even_squares=[i**2 for i in range(1,10) if i%2==0]
print(even_squares) #[4, 16, 36, 64]
even_squares=[i for i in range(1,10) if i%2==0]
print(even_squares) #[2, 4, 6, 8]
'''

#딕셔너리와 for문
'''my_dic={
    "name":"홍길동",
    "address":"서울시 은평구",
    "gender":"남자",
    "hobby":["런닝","헬스","낚시"]
}

for i in my_dic: #key값만 순회
    print(i, end=" ") #name address gender hobby 
print()
for i in my_dic.keys(): #key 메서드 사용
    print(i, end=" ") #name address gender hobby 
#key 메서드를 사용안해도 key값이 나오지만 협업 시 명시적으로 메서드를 사용하는 것이 좋다
print()
for i in my_dic.values(): #value값 출력
    print(i,end=" ") # 홍길동 서울시 은평구 남자 ['런닝', '헬스', '낚시']
print()
for i in my_dic.items(): #key,values값 출력
    print(i,end=" ") # 튜플 형태로 출력, ('name', '홍길동') ('address', '서울시 은평구') ('gender', '남자') ('hobby', ['런닝', '헬스', '낚시'])
print()
for key,value in my_dic.items(): #key,values값 출력
    #print(key,value,end=" ")
    print(f"{key}:{value}",end="/") #name:홍길동/address:서울시 은평구/gender:남자/hobby:['런닝', '헬스', '낚시']/
'''

#실습, 구구단(강사님과 동일)
'''num=int(input("몇단을 출력할까요?:"))

for i in range(1,10):
    print(f"{num}*{i}={num*i}")'''

#실습, 정수 합(강사님과 동일)
'''num=int(input("어디까지 계산할까요?"))
odd_sum=0
for i in range(1,num+1):
    if i%2!=0:
        odd_sum+=i
print(f"1부터 {num}까지의 홀수의 합:{odd_sum}")'''

#실습, 평균값 구하기
'''students={
    "학생1":{"국어":83,"영어":92,"수학":88},
    "학생2":{"국어":90,"영어":79,"수학":86},
    "학생3":{"국어":88,"영어":86,"수학":94}   
}
#평균=총합/3
for student,scores in students.items():
    total=sum(scores.values())
    print(total)
    average=total/3
    print(f"{student}의 평균점수:{average:.2f}")
'''

#이중for문 이용
'''stu1_mean=((students["학생1"]["국어"])+(students["학생1"]["영어"])+(students["학생1"]["수학"]))/3
print(f"학생1의 국어,영어,수학 평균점수는 {stu1_mean}")
stu1_mean=((students["학생2"]["국어"])+(students["학생2"]["영어"])+(students["학생2"]["수학"]))/3
print(f"학생1의 국어,영어,수학 평균점수는 {stu1_mean}")
stu1_mean=((students["학생3"]["국어"])+(students["학생3"]["영어"])+(students["학생3"]["수학"]))/3
print(f"학생1의 국어,영어,수학 평균점수는 {stu1_mean}")'''

#실습, 평균값 구하기 강사님
'''students={
    "학생1":{"국어":83,"영어":92,"수학":88},
    "학생2":{"국어":90,"영어":79,"수학":86},
    "학생3":{"국어":88,"영어":86,"수학":94}   
}

for student,score in students.items():
    print(student,score, end=",") #학생1 {'국어': 83, '영어': 92, '수학': 88},학생2 {'국어': 90, '영어': 79, '수학': 86},학생3 {'국어': 88, '영어': 86, '수학': 94}, 
    total=sum(score.values())#세과목의 합계
    avg=total/len(score)
    print(f"{student}의 평균은{avg:.2f}")'''

#이중 for문
'''for i in range(5):
    for j in range(3):
        print(f"i:{i}, j:{j}")
    print() #Enter'''

#2차원 리스트와 이중 for문
'''matrix=[
    [3,6,9,12],
    [2,4,6,8],
    [10,20,30,40],
    [11,12,13,14]
]

for row in matrix:
    for elem in row:
        if elem%3==0:
            print(elem, end=" ")'''

#실습.이중for문 구구단 만들기(2단~9단), rkdtkslarhk ehddlf  
'''for i in range(2,10):
    print(f"[{i}단]")
    for j in range(1,10):
        num=i*j
        print(f"{i}*{j}={i*j}")
    print()'''

#실습.자판기 프로그램
'''vending_machine=["게토레이","게토레이","레쓰비","생수","생수","생수","이프로"]

user=input("사용자 종류를 입력하세요.1.사용자, 2.주인, 3.종료")
while True:
    if user==1:
        drink=input("마시고 싶은 음료는?:") 
        if drink in vending_machine:
            print(f"{drink}드릴게요")
            vending_machine.remove(drink)
            print("남은 음료수:",vending_machine)
            break
        else:
            print("없음")
    elif user==2:
        choice=int(input("1. 추가 2.삭제"))
        if choice==1 or choice=="사용자":
            print("남은 음료수:",vending_machine)
            drink_add=input("추가할 음료수?")
            vending_machine.append(drink_add)
            print("추가 완료")
            print("남은 음료수:",vending_machine)
            break
        elif choice==2:
            print("남은 음료수:",vending_machine)
            drink_remove=input("삭제할 음료수?")
            if drink_remove in vending_machine:
                vending_machine.remove(drink_remove)
                print("삭제 완료")
                print("남은 음료수:",vending_machine)
                break
            else:
                print(f"{drink_remove}는 없습니다.")
                break
    elif user==3:
        print("종료")
        break
    else:
        print("잘못된 사용자 유형입니다.")'''
    

#실습. 자판기 프로그램 강사님
'''vending_machine=["게토레이","게토레이","레쓰비","생수","생수","생수","이프로"]

while True:
    user_input=input("사용자를 선택하세요.(1.소비자 2.주인 3.종료)")

    if user_input=="1"or user_input=="소비자":
        drink=input("마시고 싶은 음료는?")
        if drink in vending_machine: #있으면 제거
            vending_machine.remove(drink)
            print(f"{drink}를 드릴게요")
        else:
            print("음룓수가 없습니다.")
        print("남은 음료수 :",vending_machine)

    elif user_input=="2" or user_input=="주인":
        move=input("할일을 선택하세요.(1. 추가 2. 삭제):")
        if move=="1"or move=="추가":
            drink=input("추가할 음료수는?:")
            vending_machine.append(drink)
            print("추가 완료")
        elif move=="2"or move=="삭제":
            drink=input("삭제할 음료수는?")
            if drink in vending_machine:
                vending_machine.remove(drink)
                print(f"{drink} 삭제 완료")
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
'''

