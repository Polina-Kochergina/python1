def bilet(x,y):
    numb = list()
    k = 0
    for a in range(x, y):
        b = '0'
        a = str(a)
        if (len(a)<6):
            bil =  (6-len(a))*b + a
        else: bil = a

        num = list(bil)

        if (int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5])):
            k += 1   
    
    
    print(k) 


bilet(0, 999999)
