def transformer(lis):
    i=0
    list_tr = []
    k = 0
    while i <= len(lis) - 1:
        k = i
        # print(lis[i])
        for m in range(i,len(lis)-1):
            if lis[m] == lis[1+m]-1:
                k += 1
            else:
                break

        if i == k:
            list_tr.append(str(lis[i]))
        else:
            list_tr.append(str(lis[i]) + '-' + str(lis[k]))

        i = k + 1

    print(list_tr)

transformer([1,3,4,5,9])

