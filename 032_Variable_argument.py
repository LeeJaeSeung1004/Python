#가변인자를 이용한 함수호출
# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age),end= " ")
#     print(lang1,lang2,lang3,lang4,lang5)

#가변인자를 만드려면 (*변수)
def profile(name,age,*language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age),end= " ")
    for lang in language:
        print(lang,end=" ")
    
profile("유재석",20,"python","java","C","C++","C#")
profile("김태호",25,"kotlin","swift")