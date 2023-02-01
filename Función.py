# 1. Leer una lista de elementos, en nuestro caso enteros
def leer_lista():
    l=[]
    for i in range(10): # hacemos un bucle/repeticiones de 10 elementos, 10 recorridos
        l.append(input()) # append > añade al final de la lista   # input > leemos del teclado
    return l 

# 2. Suma elementos Programa Principal
x = leer_lista() 
suma=0
for e in x:
    suma+= int(e) 
print("La suma es: ",suma)