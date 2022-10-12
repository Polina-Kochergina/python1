def bilet(x,y):
    numb = list()
    k = 0
    for a in range(x, y):
        b = '0'
        a = str(a)
        if (len(a)<6):
            listok =  (6-len(a))*b + a
        else: listok = a

        num = list(listok)

        if (int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5])):
            k += 1   
    
    
    print(k)


bilet(0, 999999)
