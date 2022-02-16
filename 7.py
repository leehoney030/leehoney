


def a():
    import random
    tmp = []
    for i in range(3):
        tmp.append(random.randrange(1, 10))
    print(tmp[0], tmp[1], tmp[2])

def b():
    if 'tmp[0]'=='tmp[1]'=='tmp[2]'==7:
        print("777")
    elif 'tmp[0]'=='tmp[1]'=='tmp[2]':
        print("good")
    elif 'tmp[0]'=='tmp[1]'or 'tmp[1]'=='tmp[2]'or'tmp[0]'=='tmp[2]':
        print("nice")
    else:
        print("sad")
#작성하신 코드 보고 했는데 왜 tmp에 ''을 붙여야 인식?을 하는지와 a()에서 뽑은
#숫자들을 더하려면 어떻게 해야하는지도 모르겠네요..
