#클래스 메서드
'''class Converter:
    conversion_rate=1.60934

    @classmethod
    def miles_to_kliometers(cls,mile):
        return mile*cls.conversion_rate
    
#클래스 매서드도 인스턴스 변수를 생성할 수 있지만, 다른 매서드와 구분되지 않기 때문에 인스턴스를 생성하지 않는다.
print(Converter.miles_to_kliometers(7))'''

'''class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    
    @classmethod
    def from_brith_year(cls,name,birth_year):
        age=2024-birth_year
        return cls(name,age)

p1=Person.from_brith_year("홍길동",1990)
print(p1) #('홍길동', 34):튜플로 출력
print(p1.name,p1.age) #객체를 생성'''

'''class Counter:
    count=0

    @classmethod
    def increment(cls):
        cls.count+=1

    @classmethod
    def get_count(cls):
        return cls.count
    
Counter.increment()
Counter.increment()
Counter.increment()
Counter.increment()
print(Counter.get_count())'''

#자식클래스의 정보유지
'''class Animal:
    species="동물"

    @classmethod
    def get_species(cls):
        return cls.species

class Dog(Animal):
    species="진돗개"

print(Animal.get_species()) #진돗개
print(Dog.get_species()) #동물
'''

#정적 메서드
'''class Mathutils:
    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def minus(a,b):
        return a-b
    
print(Mathutils.add(30,40))
print(Mathutils.minus(30,40))'''

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
    
    def __init__(self,usage_data) -> None:
        self._usage_data=usage_data
        self._total_usage=self.calculate_total_usage()

    #usage_data getter
    @property
    def usage_data(self):#전력 사용량 데이터 리스트, 각 항목은 날짜와 사용량을 포함한 딕셔너리 형태
        return self._usage_data

    #usage_data setter
    @usage_data.setter
    def usage_data(self,new_data):
        self._usage_data=new_data
        self._total_usage=self.calculate_total_usage()

    #total_usage getter    
    @property
    def total_usage(self):
        return self._total_usage
    
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
        self._usage_data.append({"date":date,"usage":usage})
        self._total_usage=self.calculate_total_usage
    
    #특정 날짜의 전력 사용량 삭제 메서드=>list.remove 사용
    def remove_usage(self,date):
        self._usage_data=[entry for entry in self._usage_data if entry["date"]]
        self._total_usage=self.calculate_total_usage()

#자식클래스
class HomeElectricityData(ElectricityData):
    #총 전력 사용량 계산 추상메서드 코드 구현
    def calculate_total_usage():#total_usage
        return sum(entry ["usage"] for entry in self._usage_data)

    def get_usage_on_date(self,date):
        for entry in self._usage_data:
            if entry["date"]==date:
                return entry["usage"]
        return 0

    @classmethod
    def filter_electricity_usage(cls,start_date,end_date):
        return [
            entry for entry in cls.usage_data
            if start_date<=entry["date"]<=end_date
        ]

    @staticmethod
    def max_electricity_usage(self):
        if not self.usage_data:
            return None, 0
        highest=max(self.usage_data, key=lambda x:x["usage"])
        return highest["date"], highest["usage"]


home_data=HomeElectricityData(electricity_usage)
print



