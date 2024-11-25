 #<반복문(while문)> 숫자야구게임 많이 만듦
'''i=0
while i<3:
    print("반복문",i)
    i+=1 #종료조건 없으면 무한루프, ctrl+c하면 무한루프 종료
print("종료")'''

#합계 구하기>코딩 테스트 빈출
'''num=1
total=0
while num<=10:
    total+=num #total=total+num
    num+=1 #num=num+1
print(f"1부터 10까지의 합은 {total}입니다.")'''

#입력값 받기
'''user_input=""
while user_input != "종료":
    user_input=input("원하는 값을 입력하세요. 종료하려면 '종료'를 입력하세요.:")
    print(f"입력한 값:{user_input}")
print("프로그램이 종료되었습니다.")'''

# break문
'''while True:
    dinner=input("오늘 저녁 뭐먹지?")
    if dinner=="제육":
        break
    print(f"다시 골라보세요.")
print("저녁메뉴완료")'''

'''count=0

while True:
    print(count,end=" ")
    count +=1
    if count==10:
        break''' #0123456789

#continue문

'''count=0
while count<10:
    count+=1
    if count%2==0:
        continue
    print(count,end=" ") #1 3 5 7 9'''

#실습.while문 사용하기
'''while True:
    num=input("양수를 입력하세요('종료'입력 시 프로그램 종료):"))
    sum=0
    i=1

    if num>0:
        sum+=i
        i+=1
        print(f"1부터 {num}까지의 합은 {sum}입니다.")
    if num==0:
        continue
    if num<0:
        print("양수를 입력하세요.")
        break
'''

#실습.while문 사용하기 강사님.ver
'''while True:
    user_input=input("양수를 입력하세요('종료'입력 시 프로그램 종료):") #int하면 버그, 문자열과 숫자 둘다 받기 때문
    if user_input=='종료': #종료 조건
        print("프로그램을 종료합니다.")
        break
    if not user_input.isdigit(): #음수 판별
        print("양수를 입력하세요")
        continue
    number=int(user_input)
    if number==0:
        continue
    total=0
    num=1
    while num<=number:
        total+=num
        num+=1
    print(f"1부터 {number}까지의 합은 {total}입니다.")
'''

#for문
'''for i in range(10):
    print(i,end=" ") #0 1 2 3 4 5 6 7 8 9 
print()
for i in range(3,9):
    print(i,end=" ") #3 4 5 6 7 8
print()
for i in range(1,100,12):
    print(i,end=" ") #1 13 25 37 49 61 73 85 97
'''
'''fruits=["사과","바나나","포도","체리"] #리스트 변수명은 복수형
for fruits in fruits:
    print(fruits,end="|")
'''

#합계 구하기
'''numbers=[1,2,3,4,5,6,7,8,9,10]
total=0
for num in numbers: #증가조건 필요없음, 리스트 내에 있는 요소만 사용
    total+=num
print(f"합계는 {total}입니다.")
'''

#조건문 사용
'''numbers=[1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    if num%2!=0:
        print(num,end=" ") #1 3 5 7 9 
'''