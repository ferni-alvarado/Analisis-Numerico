import math

x = 6
n = 1
while x > 0:
    n = n * x
    x = x - 1 

print(n)

m = math.factorial(6)
print(m)

def mi_factorial():
    x = int(input("ingrese un numero:"))
    n = 1
    while x > 0:
        n = n * x
        x = x - 1 
    return n

ej5 = mi_factorial()
print(ej5)
