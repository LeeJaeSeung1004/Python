#continue와 break는 반복문 내에서 사용가능하다

absent = [2,5] #결석
no_book = [7] #책이 없음
for student in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent: #if 리스트 in 리스트는 for와는 다르게 비교연산자로 사용된다
        continue
    elif student in no_book:
        print("오늘 수업 여기까지 {0}는 교무실로 따라와".format(student))
        break
    print("{0},책을 읽어봐".format(student))