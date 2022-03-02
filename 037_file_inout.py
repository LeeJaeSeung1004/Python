# score_file = open("score.txt","w",encoding="utf8")
# # #파일객체 = open(파일이름,파일열기모드)
# # #파일열기모드 r= 읽기만할때 w=내용쓰기 a=마지막에 새로운 내용더하기
# # #파일을 쓰기 모드로 열면 해당 파일이 이미 존재할 경우 
# # # 원래 있던 내용이 모두 사라지고,
# # # 해당 파일이 존재하지 않으면 새로운 파일이 생성된다.
# print("수학 : 0", file=score_file)# 파일에 내용을쓸때 (내용,file=파일명)
# print("영어 : 50",file=score_file)
# score_file.close()#파일을 열면 반드시 닫아줘야함

# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end="") #줄별로 읽기 한줄로 읽고 커서는 다음줄로 이동
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()
# score_file = open("score.txt","r",encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line,end="")
# score_file.close()
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() # list형태로 저장
for line in lines:
    print(line, end="")
score_file.close()