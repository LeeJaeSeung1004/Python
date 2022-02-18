#산술연산자
print(1+1)
print(3-2)
print(5*8)
print(85/5)

print(2**3)# **는 제곱을 의미하고 2**3은 2의 3제곱이다
print(5%3)# %는 나눗셈은 나머지를 구하는 기호이고 5%3은 2이다
print(5//3)# //은 몫을 구하는 기호이고 5//3은 1이다

#비교연산자 boolean값을 반환함
print(10 > 3) # a > b 는 a는 b보다 크다 10 > 3 = True
print(4 >= 7) # a >= b 는 a는 b보다 크거나 같다이고 
#등호앞에 > 또는 <을 붙여나타낸다 4 >= 7 = False
print(10 < 3) # False
print(5 <= 5) # True
print(3 == 3) # a == b는 a는 b와 같다를 나타낸다 3 == 3은 True
print(4 == 2) # False
print(3 + 4 == 7) # True
print(1 != 3) # a != b는 a는 b와 같지않다를 나타낸다 1 != 3은 True

#논리연산자 논리식을 판단하며 boolean값을 반환함
print(not(1 != 3)) #not은 뒤에 나온 boolean값의 반대를 표기할때 사용한다
#not(1 != 3)은 False

print((3 > 0) and (3 < 5)) # a and b 는 a와 b가 모두 True일때만
#True값을 반환하고 아닐경우 False를 반환한다
print((3 > 0) & (3 < 5)) #and 대신 &를 쓸수 있다
#(3 > 0) and (3 < 5) 는 True

print((3 > 0) or (3 > 5)) # a or b 는 a와 b 둘중 하나만
# True여도 True값을 반환함
print((3 > 0) | (3 > 5)) # or 대신 |를 쓸수 있다
#(3 > 0) | (3 > 5)는 True

print(5 > 4 > 3) # True

#간단한수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)

#할당연산자
number += 2 # a += b 는 a값에 b만큼 더하고 재할당
print(number)

number *= 2 # a *= b 는 a값에 b만큼 곱하고 재할당
print(number)

number /= 2 # a /= b 는 a값에 b만큼 나누고 재할당
print(number)

number -= 2 # a -= b 는 a값에 b만큼 빼고 재할당
print(number)

number %= 5 # a %= b 는 a값에 b만큼 나누고 나머지를 재할당
print(number)