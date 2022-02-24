#for

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

for waiting_no in range(1,6):
    print("대기번호 : {0}".format(waiting_no))
#for문의 기본구조
# for 변수 in 리스트,튜플,문자열:
#     문장1
#     문장2

# 범위를 설정하기위해 range 함수를 쓸때가 많다
# a만큼 크기를 지정하려면 range(a)
# a부터 b미만의 크기를 지정하려면 range(a,b)

starbucks = ["아이언맨", "토르","그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))