x_1 = int(input())
x_2 = int(input())
x_3 = int(input())
x_4 = int(input())

y_1 = int(input())
y_2 = int(input())
y_3 = int(input())
y_4 = int(input())

print(f"(x1, y1), (x2,y2) 의 값은 ({x_1},{y_1}), ({x_2}, {y_2})")
print(f"(x3, y3), (x4,y4) 의 값은 ({x_1},{y_1}), ({x_2}, {y_2})")

dy_1 = (y_2-y_1) / (x_2-x_1)
dy_2 = (y_4-y_3) / (x_4-x_3)

if dy_2 == dy_1:
    print("평형")

else:
    print("평형하지 않습니다")

