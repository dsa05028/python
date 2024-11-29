#실습. 함수 종합 프로그래밍 강사님

weather_data=[
    ["2024-11-20","서울",15.2,0.0],
    ["2024-11-20","부산",18.4,0.0],
    ["2024-11-21","서울",10.5,2.3],
    ["2024-11-21","부산",14.6,1.2],
    ["2024-11-22","서울",8.3,0.0],
    ["2024-11-22","부산",12.0,0.0]
] #weather_data는 전역 변수, 함수 내에 변수를 안넣어도 사용가능
# 평균 기온함수
def avg_temperature(weather_data):
    city=input("도시 이름을 입력하세요:")
    total=0
    count=0
    for data in weather_data:
        if data[1]==city:
            total+=data[2]
            count+=1
    # print(total,count)
    return city, total/count
    # temp=filter(lambda x: x[1]==city, weather_data) #도시 추출
    # temperatures=list(map(lambda x: x[2], temp)) #기온 추출
    # if not temperatures:
    #     return city, None
    # else:
    #     return city, sum(temperatures)/len(temperatures)
    

#최고/최저 기온 함수
def maxmin_temperatures(weather_data):
    city=input("도시 이름을 입력하세요:")
    temperatures=[data[2] for data in weather_data if data[1]==city]
    print(temperatures)
    # temp=filter(lambda x: x[1]==city, weather_data) #도시 추출
    # temperatures=list(map(lambda x: x[2], temp))
    if not temperatures:
        return city, None, None
    else: 
        return city, max(temperatures), min(temperatures)
    
#강수량과 비온 날 찾는 함수
def total_rain_day(weather_data): 
    city=input("도시 이름을 입력하세요:")
    temp=filter(lambda x: x[1]==city, weather_data) #도시 추출
    rain=list(map(lambda x: x[3], temp)) # 강수량 추출
    total_rain=sum(rain) #총 강수량, 없으면 강수량과 비온날이 0이기 때문에 if를 쓸 필요가 없음
    rain_day=len(list(filter(lambda x: x>0, rain)))
    return city, total_rain, rain_day

#날씨 데이터 추가 함수
def add_weather(weather_data):
    date=input("날짜를 입력하세요(YYYY-MM-DD):") #YYYY-MM-DD 개발할 때 많이 쓰임
    city=input("도시 이름을 입력하세요:")
    temperatures=float(input("평균 기온을 입력하세요(℃ ):"))
    rain=float(input("강수량을 입력하세요(mm):"))
    weather_data.append([date,city,temperatures,rain])
    return city

#전체 데이터 출력함수
def all_weather(weather_data):
    print("\n현재 저장된 날씨 데이터")
    for data in weather_data:
        print(f"날짜:{data[0]},도시:{data[1]},평균기온:{data[2]}℃ ,강수량{data[3]}mm")


#프로그램->함수 순서대로 짜기
def main_program():
    while True:
        print("[날씨 데이터 프로그램]")
        print("[1. 평균 기온 계산]")
        print("[2. 최고/최저 기온]")
        print("[3. 강수량 계산]")
        print("[4. 날씨 데이터 추가]")
        print("[5. 전체 데이터 출력]")
        print("[6. 종료]")
        choice=input("원하는 기능의 번호를 입력하세요:")
        if choice=="1":
            city, avg_result=avg_temperature(weather_data) #도시의 평균 기온 계산 함수
            if avg_result is None:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 평균기온:{avg_result:.2f}℃")
            
        elif choice=="2":
            city,max_value,min_value=maxmin_temperatures(weather_data) # 도시의 최고/최저 기온 찾는 함수
            city=input("도시 이름을 입력하세요:")
            if max_value is None:
                print(f"{city}의 정보가 존재하지 않습니다.")
            else:
                print(f"{city}의 최고 기온:{max_value}℃, 최저 기온:{min_value}℃")

        elif choice=="3":
            city,total_rain,rain_day=total_rain_day(weather_data) #강수량과 비온 날 찾는 함수
            print(f"{city}의 총 강수량:{total_rain:.1f}mm")
            print(f"{city}의 비가 온 날:{rain_day}일")

        elif choice=="4":
            city=add_weather(weather_data)
            print(f"{city}의 날씨 데이터가 추가되었습니다.")

        elif choice=="5":
            all_weather(weather_data) #변수를 넣어 명시해야 깔끔함
            
        elif choice=="6":
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("1~6까지의 번호를 입력하세요.")

#프로그램 실행 함수    
main_program()

