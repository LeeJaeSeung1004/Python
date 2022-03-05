# __init__ :파이썬에서 사용되는 생성자함수이다
# class 로부터 만들어진것을 객체라고한다
# 그리고 객체는 클래스명의 인스턴스라고 한다
#함수를 생성할때 self를 제외한 init에 정의된 변수만큼동일하게 값을 줘야한다
#그렇지 않으면 사용이 불가능하다
class Unit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력{0},공격력 {1}".format(self.hp,self.damage))
        
marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)