import math
from typing import Any

n = int(input("enter a number"))

sb = n//2
lb = n - sb - 1
time = n * 45 + sb * 5 + lb * 15
hour = time // 60 + 9
minutes = time % 60
print(f"{hour} {minutes}")


