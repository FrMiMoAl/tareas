contador=1
while contador>0:
    a =int(input("Introducza el numero de serie:\n1. 2,4,8,16...\n2. 1,3,9,27...\n3. 0.2,0.5,0.8...\n4. 1,4,9,16...\n5. Salir\n"))
    if a==1:
        exponente=1
        base=2
        print("2,4,8,16...\n")
        while exponente<=20:
            print(base**exponente)
            exponente+=1
    if a==2:
        exponente=1
        base=3
        print("3,6,9,27...\n")
        while exponente<=20:
            print(base**exponente)
            exponente+=1
    if a==3:
        a=0.2
        b=0.3
        contador=1
        print("0.2,0.5,0.8,1.1...\n")
        while contador<=20:
            print(a)
            contador+=1
            a+=b
    
    if a==4:
        exponente=2
        base=1
        contador=1
        print("1,4,9,16...")
        while contador<=20:
            print(base**exponente)
            contador+=1
            base+=1
    if a==5:
        print("Hasta Luego.")
        contador=0
        
