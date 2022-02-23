# 집합 (set)
# 중복 안됨, 순서없음
my_set = {1,2,3,3,3} #집합를 만드려면 변수 = {value1, value2}
print(my_set)

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])
# 리스트를 만들고 집합 시키는 법은 set([list])

# 교집합 (java 와 python을 모두 할수 있는 개발자)
print(java & python) #교집합을 시키려면 set1 & set2
print(java.intersection(python)) 
#교집합을 시키려면 set.intersection(python)

#합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python) #합집합을 만드려면 set1 | set2
print(java.union(python)) #합집합을 만드려면 set1.union(set2)

#차집합 (java 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python) #차집합을 만드려면 set1 - set2
print(java.difference(python)) #차집합을 만드려면 set1.difference(set2)

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java 를 잊음 
java.remove("김태호")
print(java)