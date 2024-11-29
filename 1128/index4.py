#실습.클래스 종합 프로그래밍
from abc import ABC, abstractmethod

#날짜별 전력사용량
electricity_usage=[
    {"date":"2024-11-01","usage":12.5},
    {"date":"2024-11-02","usage":15.3},
    {"date":"2024-11-03","usage":10.8},
    {"date":"2024-11-04","usage":14.2},
    {"date":"2024-11-05","usage":13.6}
] #usage_data

#usage_data와 total_usage는 getter와 setter로 캡슐화

#부모클래스
class ElectricityData(ABC): #생성자를 통해 usage_data와 total_usage 초기화
    def __init__(self,usage_data,total_usage) -> None:
        self._usage_data=usage_data
        self._total_usage=total_usage
        
    #usage_data getter
    @property
    def usage_data(self):#전력 사용량 데이터 리스트, 각 항목은 날짜와 사용량을 포함한 딕셔너리 형태
        pass #return 

    #usage_data setter
    @usage_data.setter
    def usage_data(self,new_data):
        pass

    #total_usage getter    
    @property
    def total_usage(self):
        pass #return 
    
    #total_usage setter  
    @total_usage.setter
    def total_usage(self):
        pass 
    
    #총 전력 사용량 계산 추상메서드
    @abstractmethod
    def calculate_total_usage():#total_usage
        pass
    

    #특정 날짜의 전력사용량 반환 추상메서드 return이용
    @abstractmethod
    def get_usage_on_date(self,date):
        pass
        
    #새로운 날짜의 전력 사용량 추가 메서드=>list.append사용
    def add_usage(self, date ,usage):
        pass
    
    #특정 날짜의 전력 사용량 삭제 메서드=>list.remove 사용
    def remove_usage(self,date):
        pass

#자식클래스
class HomeElectricityData(ElectricityData):
    #총 전력 사용량 계산 추상메서드 코드 구현
    def calculate_total_usage():#total_usage
        pass
    #특정 날짜 전력 사용량 반환 추상메서드 코드 구현
    def get_usage_on_date(self,date):
        pass
    #electricity_usage 리스트에서 특정 날짜 범위 내의 데이터를 필터링
    @classmethod
    def filter_electricity_usage(cls):
        pass
    #전력 사용량 데이터에서 가장 높은 사용량 찾기
    @staticmethod
    def max_electricity_usage(self):
        pass

# print(f"총 전력사용량:{}")
# print(f"{self.date} 추가 후 총 전력 사용량:{}")
# print(f"특정 날짜 범위 내 사용량:{}")
# print(f"가장 높은 사용량:{}")
