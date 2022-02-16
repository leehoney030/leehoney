

def gcd(a, b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            print(i)
            break
a=int(input("첫 번째 숫자는: "))
b=int(input("두 번째 숫자는: "))
gcd(a, b)
c= (min(a, b))
print(f"{c}")