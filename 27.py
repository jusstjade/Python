aactual = input("Any Actual: ")
b = []
for i in range(0,4):
    aux=[]
    aux.append(input("Nom: "))
    aux.append(input("Any: "))
    aux.append(aactual-aux[1])
    b.append(aux)
    
    