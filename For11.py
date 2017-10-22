angulo= int(input("Ingrese un angulo en grados:"))
angulo*=3.14159265385/180
seno=0
for i in range(10):
    fac=1
    j=1
    for c in range(1,2*i+2):
        fac*=c
        c+=1
    seno +=(((-1)**i)*(angulo**(2*i+1)))/fac
print("Sen(",angulo*180/3.14159265385,")=",seno)
