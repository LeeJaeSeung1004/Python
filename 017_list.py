# 리스트 []

# # 지하철 칸별로 10명, 20명, 30명
# subway = [10,20,30] #리스트를 만드려면 변수 = [value1,value2,value3,...]
# print(subway)

# subway = ["유재석", "조세호","박명수"]
# print(subway)

# # 조세호가 몇 번째 칸에 타고 있는가
# print(subway.index("조세호")) 
# #리스트 안에 자료a의 위치를 알려면(변수.index(a))

# #하하가 다음 정류장에서 다음 칸에 탐
# subway.append("하하") 
# #만들어진 리스트에 자료a를 추가하려면 변수.append(a)
# print(subway)

# #정형돈을 유재석 / 조세호 사이에 탐
# subway.insert(1,"정형돈")
# #index a,b 사이에 자료c를 추가하려면 변수.insert(b의 위치,c)
# print(subway)

# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) #리스트의 자료를 뒤에서부터 꺼낼때 (변수.pop())
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # 같은 이름의 사람이 몇명있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))
# # 리스트안에 자료a가 몇개 있는지 확인할때 (변수.count(a))

# #정렬도 가능
# num_list = [5,3,4,1,2]
# num_list.sort()
# print(num_list)
# #정렬하려면 내부의 데이터 타입이 같아야함
# #리스트를 정렬하려면 변수.sort()
# #기본적으로 오름차순으로 정렬됨

# #순서 뒤집기
# num_list.reverse()
# print(num_list)

# #리스트를 모두지울때
# num_list.clear
# print(num_list)

# 다양한 자료형 함께 사용
num_list = [5,3,4,1,2]
mix_list = ["조세호", 20, True]
#print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)