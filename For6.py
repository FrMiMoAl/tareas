x = y = 0
while x>=y:
    x=int(input("Introduzca x:"))
    y=int(input("Introduzca y: "))
    if x>=y:
        print("X debe ser menor que y")
    
for i in range(x,y+1):
    if i%3==0:
        print("+")

    else:
        if i%10==0:
            print("*")
        else:
            print(i)
