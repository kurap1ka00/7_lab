import math
n = int(input("К-во ступенек:")) + 1
a = int((((1+math.sqrt(5))/2)**n - ((1-math.sqrt(5))/2)**n)/math.sqrt(5))
print(a)