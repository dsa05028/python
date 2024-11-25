#조건문
'''age=21

if age<=20: # ':'은 필수
    print("미성년자입니다") #들여쓰기는 한칸이라도 해야 함

print(f"나이는 {age}입니다") #나이는 21입니다
'''

#실습.if
#비밀번호 abc123을 입력했을때 '비밀번호가 맞습니다' 출력시켜주기
'''password = 'abc123'
x=input("비밀번호를 입력하세요")

if x==password:
    print('비밀번호가 맞습니다.')'''

#짝수 숫자를 입력했을때 '짝수입니다'출력시켜주기
'''x=int(input("숫자를 입력하세요"))
even = x%2

if even==0:
    print('짝수입니다.')
   '''

#실습.if 강사님.ver
#비밀번호 abc123을 입력했을때 '비밀번호가 맞습니다' 출력시켜주기
'''password=input("비밀번호를 입력해주세요")
if password=="abc123":
    print("비밀번호가 맞습니다.")'''
#짝수 숫자를 입력했을때 '짝수입니다'출력시켜주기
'''number=int(input("숫자를 입력하세요:"))
if number%2==0:
    print("짝수입니다.")'''

#else문
'''age=21

if age<=20: # ':'은 필수
    print("미성년자입니다") #들여쓰기는 한칸이라도 해야 함
else:
    print("미성년자가 아닙니다.")

print(f"나이는 {age}입니다") #나이는 21입니다
'''

#실습.if~else(강사님과 동일)
#비밀번호 abc123을 입력했을때 '비밀번호가 맞습니다' 출력시켜주기
#비밀번호가 틀리면 '비밀번호가 틀렸습니다' 출력
'''password=input("비밀번호를 입력해주세요")
if password=="abc123":
    print("비밀번호가 맞습니다.")
else:
    print("비밀번호가 틀렸습니다.") '''
#비밀번호를 입력해주세요abc1234
#비밀번호가 틀렸습니다.

#짝수 숫자를 입력했을때 '짝수입니다'출력시켜주기
#짝수가 아닌 수를 입력했을 때 '홀수입니다' 출력시켜주기

'''number=int(input("숫자를 입력하세요:"))
if number%2==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")'''
#숫자를 입력하세요:15
#홀수입니다.

#elif문
'''age=int(input("나이를 입력하세요."))

if age<20:
    print("10대입니다.")
elif age <30:
    print("20대입니다.")
elif age<40:
    print("30대입니다.")
elif age<50:
    print("40대입니다.")
else:
    print("50대이상입니다.")'''

#실습.elif문
'''score=int(input("점수를 입력하세요."))

if score<60:
    print("학점:F")
elif score<70:
    print("학점:D")
elif score<80:
    print("학점:C")
elif score<90:
    print("학점:B")
else:
    print("학점:A")'''


#실습.elif문 강사님.VER
'''score=int(input("점수를 입력하세요."))

if score>=90:
    print("학점:A")
elif score>=80:
    print("학점:B")
elif score>=70:
    print("학점:C")
elif score>=60:
    print("학점:D")
else:
    print("학점:F")'''

#실습.중첩 조건문=>나이가 음수일때, 결재방법이 카드,현금 외 다른 것 입력할 경우를 고려해야함
'''age=int(input("나이를 입력해주세요.:"))
pay=input("결제방법을 입력해주세요 (현금 또는 카드):")
money=[0,450,720,1000,1200,1300]

if pay=="현금":
    if age<8 and age>=0:
        print(f"{age}세의 카드요금은 {money[0]}원입니다.")
    elif age<14:
        print(f"{age}세의 카드요금은 {money[1]}원입니다.")
    elif age<20 :
        print(f"{age}세의 카드요금은 {money[2]}원입니다.")
    elif age<75:
        print(f"{age}세의 카드요금은 {money[4]}원입니다.")
    else:
        print(f"{age}세의 카드요금은 {money[0]}원입니다.")
elif pay=="카드":
     if age<8 and age>=0:
        print(f"{age}세의 카드요금은 {money[0]}원입니다.")
     elif age<14:
        print(f"{age}세의 카드요금은 {money[1]}원입니다.")
     elif age<20:
        print(f"{age}세의 카드요금은 {money[3]}원입니다.")
     elif age<75:
        print(f"{age}세의 카드요금은 {money[5]}원입니다.")
     else:
        print(f"{age}세의 카드요금은 {money[0]}원입니다.")
'''
#실습.중첩 조건문 강사님.ver
'''age=int(input("나이를 입력해주세요.:"))

if age>0:
    method=input("결재방법을 입력해주세요")
    if method=="카드":
        if age<8:
            price="무료"
        elif age<14:
            price="450원"
        elif age<20:
            price="720원"
        elif age<75:
            price="1200원"
        else:
            price="무료"
    elif method=="현금":
        if age<8:
            price="무료"
        elif age<14:
            price="450원"
        elif age<20:
            price="1000원"
        elif age<75:
            price="1300원"
        else:
            price="무료"
    else:
        price=None
        print("결재방법을 카드나 현금으로 입력하세요")        
    if price:
        print(f"{age}세의 {method}요금은 {price}입니다.")
else:
    print("나이는 음수가 될 수 없습니다.")
'''

#삼항연산자
'''age=int(input("나이를 입력하세요:"))
message="20대입니다."if age<30 and age>=20 else "20대가 아닙니다"
print(message)'''

#조건문 2개 이상의 삼항연산자>2개 이상은 복잡해지므로 지양
'''age=int(input("나이를 입력하세요:"))
message="20대입니다."if age<30 and age>=20 else "30대입니다." if age<40 and age>=30 else "20대도 30대도 아닙니다."
print(message)'''

#pass : 조건문 내에서 코드를 비울 때 사용

#조건문에서 in 연산자 활용
'''fruits=input("과일을 한글로 입력하세요:")

if fruits in ["사과","바나나","복숭아"]:
    print(f"{fruits}은(는) 과일에 포함되어 있습니다.")
else:
    print("존재하지 않는 과일입니다.")'''

#실습.in 연산자 활용=>get메서드 이용가능
'''dict_fruits={
    'apple':95,
    'banana':105,
    'cherry':50
    }
fruit=input("과일을 영문으로 입력하세요:")

if fruit in dict_fruits:
    print(f"{fruit}의 칼로리는 {dict_fruits[fruit]}kcal입니다.")
else:
    print("존재하지 않는 과일입니다.")'''

#실습.in 연산자 활용 강사님.ver
'''fruits={
    'apple':95,
    'banana':105,
    'cherry':50
}

fruit=input("과일을 영문으로 입력하세요:")

if fruit in fruits:
    print(f"{fruit}의 칼로리는 {fruits[fruit]}Kcal입니다.")
else:
    print(f"{fruit}은(는) 정보가 존재하지 않습니다.")'''
