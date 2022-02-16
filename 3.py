x = int(input("x 좌표를 입력하세요: "))
y = int(input("y 좌표를 입력하세요: "))

if x>0 and y>0:
    print("1")
else:
    print("1 x")

if x>0 and y<0:
    print("4")
else:
    print("4 x")
if x<0 and y<0:
    print("3")
else:
    print("3 x")
if x<0 and y>0:
    print("2")
else:
    print("2 x")