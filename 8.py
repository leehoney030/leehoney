import random
a = random.randrange(1,100)



def Check_num():


    while True:
        b = int(input("어떤 숫자 일까요?"))
        if a == b:
            print("success")
            break
        elif a > b:
            print("up")
        else:
            print("down")


Check_num()


