num=int(input("ingrese el numero:\n"))
dias = (int(num/3600*24))
horas = (int(num/3600))
minutos = int((num-(horas*3600))/60)
segundos = num-((horas*3600)+(minutos*60))
print(str(dias)+"d "+str(horas)+"h "+str(minutos)+"m "+str(segundos)+"s")

