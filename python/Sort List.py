def SortedListInsrt(l,x):
    newList=[]
    inserted = False
    for z in l:
        if not inserted:
            if x<z:
                newList+=[x]
                inserted=True
        newList+=[z]

    if not inserted:
        newList+=[x]
    return(newList)

s=[15, 21, 22, 25, 29, 31, 34, 35, 41, 44, 45, 46, 47, 48, 53, 54, 57, 59, 64, 67, 68, 69, 71, 72, 81]

w=SortedListInsrt(s,39)

print(w)