a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c and b >= c:
    print(c, a, b)
elif a >= b and a >= c and b <= c:
    print(b, c, a)
elif b >= a and b >= c and a >= c:
    print(c, a, b)
elif b >= a and b >= c and a <= c:
    print(a, c, b)
elif c >= a and c >= b and a >= b:
    print(b, a, c)
elif c >= a and c >= b and a <= b:
    print(a, b, c)