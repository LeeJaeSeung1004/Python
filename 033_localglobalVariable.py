gun = 10

# def checkpoint(soldiers): #경계근무
#     global gun #전역변수를 로컬에서 사용하려면 global 변수
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
    
def checkpoint_ret(gun,soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun
    
    
print("전체 총 : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun,2) #2명이 경계근무 나감
print("남은 총 : {0}".format(gun))