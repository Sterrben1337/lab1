a = int(input())
b = int(input())
c = int(input())

if a == b:
   if a == c:
       print("3")
   else:
       print("2")
else:
   if a == c or b == c:
       print("2")
   else:
       print("0")

