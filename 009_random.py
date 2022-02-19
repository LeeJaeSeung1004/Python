# random 라이브러리를 사용해야 쓸 수 있는 random함수
from random import *

# print(random()) #random안에 아무것도 없을시 0.0 ~ 1.0 미만의 임의의 값을 생성
# print(random() * 10) # random() * a는 0.0 ~ a.0 미만의 임의의 값을 생성
# print(int(random() * 10)) # int(random() * a)는 0 ~ a미만의 임의의 정수값을 생성 
# print(int(random() * 10) + 1) # int(random() * a) + b는 b ~ a+b 미만의 임의의 정수값을 생성

#로또값을 생성해보기
# print(int(random() * 45) + 1) # 1 ~ 46미만의 임의의 값을 생성
# print(int(random() * 45) + 1) # 1 ~ 46미만의 임의의 값을 생성
# print(int(random() * 45) + 1) # 1 ~ 46미만의 임의의 값을 생성
# print(int(random() * 45) + 1) # 1 ~ 46미만의 임의의 값을 생성
# print(int(random() * 45) + 1) # 1 ~ 46미만의 임의의 값을 생성
# print(int(random() * 45) + 1) # 1 ~ 46미만의 임의의 값을 생성

print(randrange(1,46)) # randrange(a,b)는 a ~ b미만의 임의의 값을 생성

print(randint(1,45)) #randint(a,b)는 a ~ b이하의 임의의 값을 생성