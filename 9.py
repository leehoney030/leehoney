from random import randint

def a():
    ran = []
    i=0
    while i<3:
        c = randint(0,9)
        if c not in ran:
            ran.append(c)
            i+=1
    return ran

def d():
    print("숫자를 입력하세요")
    i=0
    user = []
    while i<3:
        f = int(input("{}번째 숫자".format(i+1)))
        if f>9:
            print("error")
            continue
        elif f in user:
            print("error")
            continue
        else :
            user.append(f)
            i+=1
    return user

def g(gue,sol):
    str = 0
    ball = 0
    i = 0

    while i<3:
        if gue[i] == sol[i]:
            str += 1
            i += 1
        elif gue[i] in sol:
            ball += 1
            i += 1
        else:
            i += 1
    return str, ball


answer = a()
i=0
while i<9 :
    guess = d()
    strike, ball = g(guess, answer)
    print("{}s {}b".format(strike, ball))

    if strike == 3:

        break
    else:
        i+=1
        print("{}번 실패하셨습니다.".format(i))

print("user win")

#format은 중괄호 안에 괄호안의 값을 넣음
#while 문 사용할때 i=0, i<x 형태로 원하는 만큼 반복 가능
#[]안에다가 뭔갈 넣고싶으면 []를 대행하는 문자에.append() 하면 됨 (?)
#len 은 []안에 있는 문자열의 숫자(?)