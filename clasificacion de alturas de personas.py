estatura = input("estatura:")
 
estatura = int(estatura)
if estatura >= 30 :
    print("La estatura es correcta")

    if estatura <= 150 :
        print("Persona baja")
        
    if estatura >= 151 and estatura <= 170 :
        print("Persona de altura media")
        
    if estatura >= 171 :
        print("Persona alta")
