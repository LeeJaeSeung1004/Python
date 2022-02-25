# #출석번호가 1 2 3 4, 앞에 100을 붙이기로함 101,102,103,104
# students = [1,2,3,4,5]
# print(students)
# students = [i + 100 for i in students]
# #students에 있는 숫자들을 하나씩 i에 불러오고 100을 더한다
# print(students)

# students = ["Iron man", "Thor", "groot"]
# students = [len(i) for i in students]
# print(students)

#학생들 이름을 대문자로 변환
students = ["Iron man", "Thor", "groot"]
students = [i.upper() for i in students]
print(students)