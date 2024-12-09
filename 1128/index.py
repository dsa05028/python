#실습 건강상태 클래스 만들기

'''class Health:
    def __init__(self,name) -> None:
        self._hp=100
        self._name=name
    
    def get_name(self):
        return self._name
    
    def set_name(self,value):
        self._name=value

    def set_hp(self,value):
        self._hp=value
        if self._hp>=100:
            self._hp=100
        else:
            self._hp=value

    def get_hp(self):
        return self._hp
    
    def exercise(self,hour):
        self.set_hp(self._hp+hour)
        print(f"{hour}시간 운동하다")

    def drink(self,cups):
        self.set_hp(self._hp-cups)
        print(f"술을 {cups}잔 마셨다")

    def info(self):
        print(f"{self.get_name()}-hp:{self.get_hp()}")

p1=Health("나몸짱")
p1.set_hp(70)
p1.exercise(5)
p1.drink(2)
p1.info()

p2=Health("나약해")
p2.set_hp(50)
p2.exercise(1)
p2.drink(12)
p2.info()'''

#getter, setter 데코레이터

'''class Person:
    def __init__(self, name, age) -> None:
        self.__name=name
        self.__age=age
    #getter
    @property
    def name(self,):
        return self.__name
    
    #setter
    @name.setter
    def name(self,value):
        self.__name=value
    #    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,value):
        self.__age=value
        
p1=Person("홍길동",20)
print(p1.name) #괄호가 없어도 됨
print(p1.age)

p1.name="이몽룡" #setter에 접근하여 이름 변경
p1.age=25 #setter에 접근하여 나이 변경
print(p1.name)
print(p1.age)'''