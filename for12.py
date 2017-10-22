a = -1
while a<0:
    a=int(input("Introduzca un numero entero + para calcular el factorial:"))
factorial = 1
for i in range(1,a+1):
    factorial*=i
print(a,"!=",factorial)
