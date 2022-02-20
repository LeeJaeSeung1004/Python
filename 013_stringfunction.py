apple = "Apple is Delicious"
print(apple.lower()) #문자열을 전부 소문자로 바꿀때는 (변수.lower())
print(apple.upper()) #문자열을 전부 대문자로 바꿀때는 (변수.upper())
print(apple[0].isupper()) 
#문자열의 a번째가 대문자인지확인할때는 (변수[a-1].isupper())
print(len(apple))# 문자열의 길이를 반환할때는 (len(변수))
print(apple.replace("Apple","Banana"))
#문자열의 a부분을 b로 수정할때는(변수.replace("a","b"))
#대소문자가 틀릴 경우 변경되지 않음

index = apple.index("i")
print(index)
#문자열에서 a문자가 어디있는지 확인할때는(변수.index("a")) 0부터 시작
index = apple.index("i", index + 1)
#문자열에서 b지점부터 a문자가 어디있는지 확인할때는 (변수.index("a",b))
print(index)

print(apple.find("i")) 
#index와 비슷하게 문자열에서 a문자가 어디있는지 찾을때(변수.find("a"))
print(apple.find("Banana"))
#하지만 문자열에 존재하지 않는 문자를 찾을경우 -1을 반환한다
#print(apple.index("Banana"))
#반면 index로 없는 문자를 찾으면 오류가 난다 
# 그리고 다음에 존재하는 코드가 실행되지 않고 끝난다

print(apple.count("i"))
#문자열에 a문자가 몇번 등장하는지 셀경우(변수.count("a"))