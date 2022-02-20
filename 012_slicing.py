jumin = "990120-1234567"

print("성별: "+ jumin[7])
print("년: " + jumin[0:2]) # 불러올 정보가 a부터 b까지라면 [a:b+1]
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])

print("생년월일 :" + jumin[:6]) #불러올 정보가 0부터 a까지라면 [0:a+1]
print("뒤 7자리 :" + jumin[7:]) #불러올 정보가 a부터 끝까지 라면[a:]
print("뒤 7자리 (뒤에서부터): " + jumin[-7:]) 
#뒤에서부터 a번째에 있는걸 불러오려면 [-a]