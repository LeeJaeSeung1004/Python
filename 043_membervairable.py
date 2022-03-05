#멤버변수는 클래스 안에서 정의된 변수이며 그변수로 초기화와 실제사용도가능하다
#클래스 외부에서 원하는 변수를 확장할수 있다
#확장한 변수는 확장한 객체에서만 사용가능하다
class Unit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력{0},공격력 {1}".format(self.hp,self.damage))
        
# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크",150,35)

#레이스 :공중유닛,비행기 ,클로킹(상대에게 보이지않음)
wraith1 = Unit("레이스",80,5)
print("유닛 이름 : {0},공격력 : {1}".format(wraith1.name,wraith1.damage))

# 마인드컨트롤: 상대방 유닛을 내것으로 만드는 것
wraith2 = Unit("빼앗은 레이스",80,5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))