# import pickle

# with open("profile.pickle","rb") as profile_file:
#     # profile.pickle을 읽기전용으로 불러와서 profile_file이라는 변수로 불러옴
#     print(pickle.load(profile_file))#profile_file을 불러와서 출력함
    
# with open("study.txt","w" ,encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())