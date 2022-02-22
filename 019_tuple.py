#튜플
#리스트와 다르게 추가,변경이 불가함
#대신 리스트보다 빠름

menu = ("돈까스", "치즈까스") #튜플을 만드려면 변수 = (value1,value2)
print(menu[0]) #a번째 튜플을 출력하려면 변수[a-1]
print(menu[1])

#menu.add("생선까스") 변경불가

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)

#다른튜플의 생성법

(name,age,hobby) = ("김종국",20,"코딩") 
#변수a,b,c 를 튜플로 만들때 (a,b,c) = (value1,value2,value3)
print(name, age, hobby)