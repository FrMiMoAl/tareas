dia = input("Dia: ")
mes = input("Mes: ")
 
dia = int(dia)
mes = int(mes)
 
if dia >= 1 and dia <= 31 :
    print("El dia esta correcto")
    if mes >= 1 and mes <= 12:
        print("El mes esta correcto\n\n")
   #ambos datos estan bien
   #20/01 al 18/02
   if (mes == 01 and dia >20)or(mes == 02 and dia <=18 ):
       print ("el signo es Acuario")
       
   #19/02 al 20/03
   if (mes == 02 and dia >19)or(mes == 3 and dia <=20 ):
       print ("el signo es Piscis")
       
   #21/03 al 19/04
   if (mes == 03 and dia >21)or(mes == 04 and dia <=19 ):
       print ("el signo es Aries")
       
   #20/04 al 20/05
   if (mes == 04 and dia >20)or(mes == 05 and dia <=20 ):
       print ("el signo es Tauro")

   #21/05 al 20/06
   if (mes == 05 and dia >21)or(mes == 06 and dia <=20 ):
       print ("el signo es Geminis")
       
   #21/06 al 22/07
   if (mes == 06 and dia >21)or(mes == 07 and dia <=22 ):
       print ("el signo es Cancer")
       
   #23/07 al 22/08
   if (mes == 07 and dia >23)or(mes == 08 and dia <=22 ):
       print ("el signo es Leo")
      
   #23/08 al 22/09
   if (mes == 08 and dia >23)or(mes == 09 and dia <=22):
      print ("el signo es Virgo")
      
   #23/09 al 22/10
   if (mes == 09 and dia >23)or(mes == 10 and dia <=22):
      print ("el signo es Libra")
      
   #23/10 al 21/11
   if (mes == 10 and dia >23)or(mes == 11 and dia <=21):
      print ("el signo es Escorpio")
      
   #22/12 al 19/01
   if (mes == 12 and dia >22)or(mes == 01 and dia <=19):
      print ("el signo es Escorpio")       
   
    else :
        print("Error en el mes")
 else:
    print("Error en el dia")
