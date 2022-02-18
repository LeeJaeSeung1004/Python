# 애완동물을 소개 해주세요

animal = "강아지"
name = "뽀삐"
age = 4
hobby = "산책"
is_adult = age >= 3

'''이렇게하면
여러문장이 
주석처리 
됩니다'''

#여러문장을 주석처리할때는 범위를 선택하고 ctrl + /를 하면 주석처리가 된다

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이고, " + hobby + "을 좋아해요")
print(name, "는 ", age, "살이고, ", hobby, "을 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))
