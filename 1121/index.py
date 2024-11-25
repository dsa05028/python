#변수의 사이즈를 알아보는 방법(바이트 단위)
'''from sys import getsizeof

print(getsizeof(1))
print(getsizeof("1")) #문자열과 숫자가 다름'''

#변수의 자료형 알아보는 방법
'''print(type(1111111)) #int
print(type(333.3333)) #float
print(type("안녕하세요")) #str
print(type(True)) #bool 
print(type(None)) #NoneType'''

#자료형 변환
'''num=int(input("숫자를 입력하세요"))
a=num%2==0
print("True면 짝수, False는 홀수", a)

num=input("숫자를 입력하세요")
a=int(num)%2==0
print("True면 짝수, False는 홀수", a)'''

'''print(int(5.5)) 
print(type(int("30")))
a="10"
print(type(int(a)))
print(type(a))'''
'''num=10
print(type(str(num)))'''

#문자열 연산
'''a="파이썬"
print("안녕하세요 "+a+" 반갑습니다") #+연산자는 문자열끼리 연결
#print("오류"+1234) 오류
print("hey"*10) #*연산자 : 문자열 반복 출력
print("데이터확인",a)''' #데이터 확인할 때 많이 사용

#여러줄 문자열 출력
'''korea_song="""
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세"""
print(korea_song)'''

#따옴표 출력
'''print('"오늘 저녁 뭐먹지?"')
print("'오늘 저녁 뭐먹지?'")'''

#문자열 이스케이프
'''print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\\World")
print('\'HelloWorld\'')
print('\"HelloWorld\"')'''

#문자열 포매팅
'''print("올해는 2024년 용띠의 해이다") #년도와 띠를 일일히 수정해야함
year ="올해는 %d년 %s띠의 해이다" %(2024,"용") #%d는 정수, %s는 문자열
year ="올해는 %d년 %s띠의 해이다" %(2025,"뱀")
print(year)'''

# 포맷코드 활용
'''number = "저는 올해 %d살입니다" % 20
print(number)
calc="20 나누기 3은 %.2f" % 6.67 #%f는 소숫점 6자리까지 표현, 소수점 n자리 표현 %.nf
print(calc)
text="저는 %s에서 살고 있습니다" % "서울" #%ns는 공백+문자열=n자리 표현, %-ns는 문자열+공백=n자리
print(text)
char="이모티콘은 %c 이것으로 할게요" %"😊"
print(char)'''

#format() 사용한 포매팅
'''country="대한민국"
city="서울"
people="한국인"
text="저는 올해 {0}살입니다".format(20)
print(text) #저는 올해 20살입니다
text="저는 {0} 사람이며 {1}에 살고 있습니다".format(country,city)
print(text) #저는 대한민국 사람이며 서울에 살고 있습니다  
text="저는 {1} 사람이며 {0}에 살고있습니다." .format(country,city)
print(text) #저는 서울 사람이며 대한민국에 살고있습니다.
text="제가 사는 {0}은 {a}에 있습니다.".format(city, a="한국")
print(text) #제가 사는 서울은 한국에 있습니다.
text="중괄호 출력하고 싶을 때 {{ 중괄호 }}".format()
print(text) #중괄호 출력하고 싶을 때 { 중괄호 }
text="{},{},{},{}".format(80,90,100,200)
print(text) #80,90,100,200
a="[{0:<10}]".format("hey")
print(a) #[hey       ]
a="[{0:>10}]".format("hey")
print(a) #[       hey]
a="[{0:^10}]".format("hey")
print(a) #[   hey    ]
a="[{0:&^10}]".format("hey")
print(a) #[&&&hey&&&&]'''

#f문자열 포매팅
'''name="홍길동"
age=20
print(f"내 이름은 {name}입니다. 나이는 {age+1}살입니다") #내 이름은 홍길동입니다 나이는 21살입니다
print(f"내이름은 [{name:@^20}]") #내이름은 [@@@@@@@@홍길동@@@@@@@@@]
'''

#실습. 이스케이프 연습
'''print("|\_/|\n|q p|\t/}")
print("( 0 )\"\"\"\\")
print("|\"^\"` \t |\n||_/=\_ _|")'''

'''print("|\_/|\n|q p|\t/")   

print("( 0 )\"\"\"\\")
print("|\"^\"\'\t|\n|_/=\_ _|")'''

##강사님
'''print("|\\_/|")
print("|q p|   /}")
print("(0)\"\"\"\\   ")
print("|\"^\"`   |")
print("||_/=\\\\__|")'''

#실습. f문자열 포매팅 
'''name="name"
name=f"[{name:=^10}]"
print(name)
text=f"문자열 실습입니다.{{중괄호}}를 출력해보세요."
print(text)'''

##강사님
'''name="name"
print(f"[{name:=^30}]")
print(f"문자열 실습입니다. {{ 중괄호 }}를 출력해보세요")
'''

#문자열 인덱싱
#퀴즈 위 python을 인덱싱을 이용해서 출력해보세요
'''a="Hello, Python"
print(a[7] + a[8] + a[9] + a[10] + a[11] + a[12]) #Python
#문자열 슬라이싱
print(a[7:]) #Python
print(a[7:13]) #Python'''

#퀴즈
'''a="20240930"
print(a[0:4]년"a[4:6]"월"a[6:8]"일")'''
      
#강사님
'''date="20240930"
year=date[:4]
month=date[4:6]
day=date[6:]
print(year+"년",month+"월",day+"일")'''

#길이구하기
'''a="Hello, Python"
print("문자열 a의 길이는",len(a))'''

#개수 세기
'''a="Hello, Python"
print(a.count('l'))'''

#위치 찾기 find함수
'''a="Hello, Python"
print(a.find("P"))
print(a.find("s"))
print(a.find("o")) #가장 앞선 문자를 찾음
first_o=a.find('o')
print(first_o)
second_o=a.find('o',first_o+1)
print(second_o) #두번째 o를 찾는 방법'''

#위치 찾기 index함수
'''a="Hello, Python"
print(a.index("P"))
print(a.index("s")) # 문자열에 포함되지 않은 문자는 오류 발생
'''

#문자열 바꾸기 replace
'''a="Hello, Python"
print(a.replace("Python","파이썬"))
#문자열 나누기 split
print(a.split('l'))'''

#대/소문자 바꾸기 upper은 대문자, lower은 소문자, 회원가입 등에 많이 사용
'''a="Hello, World"
print(a.upper()) #HELLO, WORLD
print(a.lower()) #hello, world'''

#공백 지우기
'''a="        Hello          "
print(f"[{a.rstrip()}]") #[        Hello], f문자열 포매팅을 이용하여 공백확인
print(f"[{a.lstrip()}]") #[Hello          ]
print(f"[{a.strip()}]") #[Hello]'''

#문자열 판별하기(숫자판별)
'''print("1234".isdecimal()) #True
print("1234".isdigit()) #True ,isdigit을 가장 많이 사용
print("1234".isnumeric()) #True
print("-1234".isdigit()) #False, 음수는 항상 False
'''

#문자열 판별하기(문자 공백판별)
'''print("hello".isalpha())
print("안녕하세요".isalpha())
print("hello123".isalpha())
print("hello123".isalnum())
print("hello!".isalnum())
print("안녕하세요123".isalnum())
print("   ".isspace())
print("\t\n".isspace())
print("hello".isspace())'''

#문자열 판별하기(대소문자 판별)
'''print("Hello".islower()) #False, H는 대문자
print("HELLO".isupper()) #True, 대문자로만 구성
'''

#실습.종합실습
#1번
'''name=input("이름을 입력하세요.")
age=input("나이를 입력하세요")
print("안녕하세요!",name+"님",f"({age}세)")'''

#1번 정답
'''a=input("이름을 입력하세요")
b=input("나이를 입력하세요")
print(f"안녕하세요 {a}님 ({b}세)")'''

#2번
'''name=input("이름을 입력하세요.")
byear=int(input("태어난 년도를 입력하세요"))
cyear=int(input("올해 년도를 입력하세요."))
age1=(cyear-byear)+1
print(f"올해는 {cyear}년,{name}님의 나이는 {age1}세 입니다.")
'''

#2번 강사님
'''a=input("이름을 입력하세요")
b=int(input("태어난 년도를 입력하세요"))
c=int(input("올해 년도를 입력하세요"))
print(f"올해는 {c}년, {a}님의 나이는 {c-b}세 입니다.")
'''
'''x=5
print("True면 짝수, False면 홀수:",x%2==0)'''
