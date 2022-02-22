#사전 {}
# cabinet = {3:"유재석", 100:"김태호"} #키는 중복이 불가하다
#사전을 만들때 변수 = {key:value1,key:value2}
# print(cabinet[3]) #값을 출력할때 변수[key]
# print(cabinet[100])

# print(cabinet.get(3)) #값을 출력할때 변수.get(key)
# print(cabinet[5]) #대괄호로 없는 값을 출력시 오류가 나며 프로그램이 끝남
# print(cabinet.get(5))
# #get으로 없는값을출력시 none이 출력되며 다음 코드가 실행됨
# print(cabinet.get(5,"사용 가능")) 
# #get으로 없는값을 출력시 none대신 원하는 값을 출력하려면 변수.get(key,value)

# #사전자료형 안에 원하는 값이 있는지 확인할때 (key in 변수)
# print(3 in cabinet) #True
# print(5 in cabinet) #False

#키는 string형으로도 가능

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새로 자료를 넣을때
print(cabinet)
cabinet["C-20"] = "조세호" 
#사전에 새로운 자료형을 넣으려면 변수[key] = value
cabinet["A-3"] = "김종국" #원래 있는 키에 새로운 값을 넣으면 값이 덮어씌워짐
print(cabinet)

#자료를 제거할때 del 변수[key]
del cabinet["A-3"]
print(cabinet)

#key들만 출력할때 변수.keys()
print(cabinet.keys())

# value들만 출력할때 변수.values()
print(cabinet.values())

#key, value 둘다 출력할때 변수.items()
print(cabinet.items())

#모든값을 제거할때 변수.clear()
cabinet.clear()
print(cabinet)
