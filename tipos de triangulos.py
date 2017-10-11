a=int(input("Ingresa lado: \n" ))
b=int(input("Ingresa lado: \n" ))
c=int(input("Ingresa lado: \n" ))

if((abs(a-c)<b)and(b<(a+c))):   
 print("Si Forma un triangulo")
else:
 print("No Forma un triangulo")

 if(a==b and b==c):
     print ("/nEl triangulo es Equilatero")
     
 if(a==b or a==c or b==c ):
     print ("/nEl triangulo es Isoceles")
     
 if(a != b or a != c or b != c):
     print ("/nEl triangulo es Escaleno")

 
