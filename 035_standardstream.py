# print("python","java","javascript",sep=",",end="?")
# # (변수,변수 ,sep="str")시 변수와 변수사이의 문자를 결정할수있다
# print("무엇이 더 재밌을까요?")

# import sys
# print("python","java",file=sys.stdout)
# print("python","java",file=sys.stderr)

# #시험 성적
# scores = {"수학":0,"영어":50,"코딩":100}
# for subject, score in scores.items():
#     # print(subject,score)
#     print(subject.ljust(8),str(score).rjust(4),sep=":") 
#     #변수.ljust(a)는 변수를 a칸만큼 비우고 좌측정렬하는것이고
#     #변수.rjust(a)는 변수를 a칸만큼 비우고 우측정렬하는것이다

# 은행 대기 순번표
# 001, 002, 003
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))
    
answer = input("아무 값이나 입력하세요 : ")
print("입력하신값은 " + answer + "입니다/")