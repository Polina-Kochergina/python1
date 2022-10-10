def crossword(x,y):  
    world1 = list(x)
    world2 = list(y)

    w_1 = set(x)
    w_2 = set(y)

    lenth = len(x)

    space = ' '
    letter = w_1 & w_2
   
    letter = list(letter)
    letter = letter[0]

    index1 = world1.index(letter)
    index2 = world2.index(letter)

    for i in range(0,index1):
        print(index2*space + world1[i])

    print(y)

    for i in range(index1+1, lenth):
        print(index2*space + world1[i])

crossword('hello', 'world')
