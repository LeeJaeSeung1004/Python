#분기 
# weather = input("오늘 날씨는 어때요? ")

# #if를 사용하려면
# # if 조건:
# #     실행 명령문
# if weather == "비" or weather == "눈": #조건을 비교하고 맞으면 밑의 문장을 실행하고 빠져나옴 
#     print("우산을 챙기세요") # 아닐경우 다음 조건을 비교하고
# elif weather == "미세먼지":  # 맞으면 밑의 문장을 실행하고 나옴
#     print("마스크를 챙기세요") 
# else: #if로 명시된 조건외의 모든 경우는  else가 처리함 else가 없을경우 아무것도 출력하지 않음
#     print("준비물 필요 없어요.")

temp = float(input("기온은 어때요? "))

if 30 <= temp: # a가 b 이상일때 a >= b 혹은 b <= a
    print("너무 더워요. 나가지 마세요.")
elif 10<= temp and temp < 30: # a가 b 이상일때 그리고 a가 c보다 미만일때
    print("괜찮은 날씨에요.") # a >= b and a < c
elif 0 <=  temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무추워요. 나가지 마세요.")