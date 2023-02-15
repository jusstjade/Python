# 1
x = int(input("Introduce un número"))
if x % 2 == 0:
    print("El número {} es par".format(x))
else:
    print("El numero {} es impar".format(x))

# 2
x = int(input("Introduce un número"))
if x > 10:
    print("El número {} es mayor que 10".format(x))
elif x<10:
    print("El numero {} es menor que 10".format(x))
else: print("El numero {} es 10".format(x))

# 3
def leer():
    a = "b"
    l = []
    while a !=".":
        a = input("Introduce un número: ")
        if a!=".":
            l.append(int(a))
            return l
def comparar(a,c):
    for e in a:
        if e>c:
            print(e)
# programa principal
x = leer()
y = input("Introduce el número a comparar: ")
comparar(x,y)

# 4
def menu():
    print("""
    Calculadora de numeros enteros
    1. sumar
    2. restar
    3. multiplicar
    4. dividir
    5. potencia
    0. salir
    """)
    x = input("Introduce la opción deseada")
    return int(x)

def leer_valores():
    a = input("Introduce el primer valor: ")
    b = input("Introduce el segundo valor: ")
    return int(a), int(b)

# PP
opcio = 10
while opcio!=0:
    if opcio!=0:
        match opcio:
            case 1:
                a,b = leer_valores()
                c = a + b
                print("La suma de {} y {} es {}".format(a, b, c))
            case 2:
                a,b = leer_valores()
                c = a - b
                print("La resta de {} y {} es {}".format(a, b, c))
            case 3:
                a,b = leer_valores()
                c = a * b
                print("La multiplicación de {} y {} es {}".format(a, b, c))
            case 4:
                a,b = leer_valores()
                c = a / b
                print("La división de {} y {} es {}".format(a, b, c))
            case 5:
                a,b = leer_valores()
                c = a ** b
                print("La potencia de {} elevado a {} es {}".format(a, b, c))
            case other:
                print("Opcion no valida")

# 5
def leer(): 
    a = "b"
    l = []
    while a !=".":
        a = input("Introduce una palabra: ")
        if a!=".":
            l.append(a)
    return l
# Programa principal