def lista():
    x="a"
    l=[]
    while x!="0":
        x=input("Introduce una palabra: ")
        if x!="0":
            l.append(x)
    return l
# PP
a = lista()
print(a)
