def greater(lista):
    length=len(lista)
    while(length>2):
        a=[]
        b=max(lista)
        c=lista.index(b)
        lista.pop(c)
        length=length-1
    print("third maximum number in a list = ",b)
greater([23,4,5,65,89])
