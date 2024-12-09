#모듈

'''import calc

#모듈명.함수명
print(calc.add(10,4))
print(calc.sub(10,4))
print(calc.multiply(10,4))
print(calc.divide(10,4))
'''

'''import calc as a

print(a.add(10,4))
print(a.sub(10,4))
print(a.multiply(10,4))
print(a.divide(10,4))'''

'''from calc import add as a, sub as b

#모듈명.함수명
print(a(10,4))
print(b(10,4))
# print(calc.multiply(10,4))
# print(calc.divide(10,4))'''

'''from datetime import datetime, timedelta

now = datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print(f"{now.year}년 {now.month}월 {now.day}일")'''

'''from datetime import datetime, timedelta

now=datetime.now()
print(now)
print(now.year)'''

#특정 날짜 계산
'''from datetime import datetime, timedelta, timezone

now=datetime.now()
next_week=now+timedelta(weeks=1)
print(next_week)'''

#타임존 계산

'''
from datetime import datetime, timedelta, timezone

now=datetime.now()
print(timezone.utc)
print(datetime.now(timezone.utc))'''

'''from datetime import date

open_day = date(year=2024, month=11, day=18)
print(date.today())
print(date.today().weekday())
week=["월","화","수","목","금","토","일"]
print(week[date.today().weekday()])

pass_day=date.today()-open_day
print(pass_day.days)

import time

print(time.time())
print(time.localtime())
print("2초 대기")
time.sleep(2)
print("대기완료")
start=time.perf_counter()
time.sleep(1)
end=time.perf_counter()
print(end-start)'''

'''import math

# print(math.pi)
# print(math.sqrt(25))
# print(math.factorial(5))
print(math.ceil(2.44)) #올림
print(math.floor(4.48)) #버림
print(round(2.51))#반올림'''

#랜덤함수
'''import random
import math

print(random.randint(1000, 9999))
# print(random.uniform(1.1, 5,5))
print(random.random())
print(random.randrange(1000,10000))
choices=[1,2,3,4,5,6,7,8]
print(random.choice(choices))

rand=1000+math.floor(random.random()*9000)
print(rand)'''

# 실습. 로또 번호 뽑기
import random

lotto_num=list(i for i in range(1,46))
lotto=random.sample(lotto_num,6) #범위 내 중복 제외하고 여러 개 난수를 생성
print(sorted(lotto))


# 실습. 로또 번호 뽑기 강사님
'''import random

lotto=set()

while len(lotto)<6:
    lotto.add(random.randint(1,45))

print(sorted(lotto))'''

'''import random

lotto = random.sample(range(1,46),6)
print(sorted(lotto))'''

#sys
'''import sys

# print(sys.argv)
# print(sys.argv[1:])

if "-h" in sys.argv or "--help" in sys.argv:
    print("사용법: python main.py[옵션]")
    print("-h,--help           도움말표시")
    print("-v,--version 버전정보표시")
    sys.exit(0)

if "-v" in sys.argv or "--version" in sys.argv:
    print("버전 : 1.0.0")
    sys.exit(0)'''

#os
'''import os

dir_current=os.getcwd()
print(dir_current)
file_path=os.chdir(dir_current)
print(file_path)
dir=os.popen("ls")
print(dir.read())
os.mkdir("test")
'''

#실습.타자연습게임

'''import time
import random

start=time.time()
words = [
  "mountain", "river", 
  "forest", "ocean", 
  "desert", "tree", 
  "flower", "cloud", 
  "rain", "sunlight"
  ]

correct_word=0

input_times=[]

while correct_word<2:

    word=random.choice(words)
    print(f"단어:{word}")
    word_input=input("입력:")

    if word==word_input:
        correct_word+=1
        word_spendtime=time.time()
        input_times.append(word_spendtime)
        print("통과!")
    else:
        word2_time=time.time()
        print("오타! 다시 시도하세요.")

end=time.time()
avg=sum(input_times)/len(input_times)
print(f"총 {correct_word}개의 단어를 입력하셨습니다.")
print(f"총 걸린 시간:{end-start:.2f}")
print(f"평균 단어당 입력 시간:{avg}")
'''

#실습.타자연습게임
'''import time
import random

start=time.time()
words = [
  "mountain", "river", 
  "forest", "ocean", 
  "desert", "tree", 
  "flower", "cloud", 
  "rain", "sunlight"
  ]

total_words=0
start_time=time.time()

def game():
    print("영어 타자 연습 게임")
    print("게임종료를 원하시면 exit를 입력하세요")
    total_words=0
    start_time=time.time()

    while True:
        word=random.choice(words)
        print(f"단어:{word}")
        while True:
            user_input=input("입력 : ")

            if user_input=="exit":
                end_time=time.time()
                total_time=end_time-start_time
                print("\n게임종료")
                print(f"총 입력한 단어는 {total_words}개 입니다.")
                print(f"총걸린시간은 {total_time}초")
                print(f"단어 당 평균 시간은 {total_time/total_words}초")
                return
        
            if user_input==word:
                print("통과")
                total_words+=1
                break

            else:
                print("오타! 다시입력")

game()'''