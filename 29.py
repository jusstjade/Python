def leer():
    l=[]
    a='a'
    while a!='.':
        a=input("Pon el nombre: ")
        if a!='.':
            l.append(a)
    return l

def ncp(l, c):
    p=[]
    x=0
    for e in l:
        if e[0]== c:
            x +=1
            p.append(e)
    print("El número de palabras que comienzan {} son {} y son {}".formado(c,x,p))

# PP
a=leer()
c=input("Introduce el carácter que desea buscar: ")
ncp(a,c)
