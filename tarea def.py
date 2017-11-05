def fibonacci(a):
    if a==0:
        return 0
    else:
        if a==1:
            return 1
        else:
            if a>=2:
                return fibonacci( a - 1 ) + fibonacci( a - 2 )
            else:
                return -1
 
for i in range(100):
    print( fibonacci( i ) )
