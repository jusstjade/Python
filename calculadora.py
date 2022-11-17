# Definición de funciones auxiliares
# función del menuú principal
def menu_principal():
   print("""Calculadora
       Menú:
       1. Números enters
       2. Números reals
       3. Canvis de base
       0. Sortir
   """)
   opcio=input("Seleccioni l'opció que vulgui: ")
   return opcio

# función del menú de números enters
def menu_enters():
   print("""
            Menú calculadora de números enters:
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Potència
            6. Mòdul
            0. Sortir
            """)
   opcio=input("Seleccioni l'opció que vulgui: ")
   return opcio
 
# Funció del menú dels números reals
def menu_reals():
   print("""
           Menú calculadora de números reals:
           1. Sumar
           2. Restar
           3. Multiplicar
           4. Dividir
           0. Sortir
           """)
   opcio=input("Seleccioni l'opció que vulgui: ")
   return opcio
#Funcions de canvis de base
def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario
def decimal_a_octal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal
def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal
# Programa principal de la calculadora
opcio=1
while(opcio!=0):
   opcio= menu_principal()
   match opcio:
       case "1":
           opcio2=input("Seleccioni l'opció que vulgui: ")
           a = int(input("Indiqui el primer operand: "))
           b = int(input("Indiqui el segon operand: "))
           match opcio2:
               case "1":
                   c=a+b
                   print("La suma de ",a," més ",b," és ",c)
               case "2":
                   c=a-b
                   print("La resta de ",a," menys ",b," és ",c)
               case "3":
                   c=a*b
                   print("La multiplicació de ",a," per ",b," és ",c)
               case "4":
                   c=a/b
                   print("La divisió de ",a," per ",b," és ",c)
               case "5":
                   c = a ** b
                   print("La potència de ", a, "elevat a ", b, " és ", c)
               case "6":
                   c = a % b
                   print("El mòdul de ",a," mòdul ",b, " és ",c)
               case "0":
                   print("Adéu")
               case other:
                   print("Opció no vàlida!")
       case "2":
           print("""
           Menú calculadora de números reals:
           1. Sumar
           2. Restar
           3. Multiplicar
           4. Dividir
           0. Sortir
           """)
           opcio2=input("Seleccioni l'opció que vulgui: ")
           a = float(input("Indiqui el primer operand: "))
           b = float(input("Indiqui el segon operand: "))
           match opcio2:
               case "1":
                   c=a+b
                   print("La suma de ",a," més ",b," és ",c)
               case "2":
                   c=a-b
                   print("La resta de ",a," menys ",b," és ",c)
               case "3":
                   c=a*b
                   print("La multiplicació de ",a," per ",b," és ",c)
               case "4":
                   c=a/b
                   print("La divisió de ",a," per ",b," és ",c)
               case "0":
                   print("Adéu")
               case other:
                   print("Opció no vàlida!")
       case "3":
           print("""
           Menú calculadora canvis de base:
           1. Donat un binari passar a octal, decimal i hexadecimal.
           2. Donat un octal passar a binari, decimal i hexadecimal.
           3. Donat un decimal passar a binari, octal i hexadecimal.
           4. Donat un hexadecimal passar a binari, octal i decimal.
           0. Sortir
           """)
           opcio2=input("Seleccioni l'opció que vulgui: ")
           a = input("Indiqui el número a convertir: ")
           match opcio2:
               case "1": # Binari a
                   b=int(a,base=8)
                   c=int(a,base=10)
                   d=int(a,base=16)
                   print("El número ",a," en octal= ",b, " en decimal= ",c," en hexadecimal= ", d)
               case "2": # Octal a
                   b=int(a,base=2)
                   c=int(a,base=10)
                   d=int(a,base=16)
                   print("El número ",a," en binari= ",b, " en decimal= ",c," en hexadecimal= ", d)
               case "3": # Decimal a
                   b=decimal_a_binario(int(a))
                   c=decimal_a_octal(int(a))
                   d=decimal_a_hexadecimal(int(a))
                   print("El número ",a," en binari= ",b, " en octal= ",c," en hexadecimal= ", d)
               case "4": # Hexadecimal a
                   b=int(a,base=2)
                   c=int(a,base=8)
                   d=int(a,base=10)
                   print("El número ",a," en binari= ",b, " en octal= ",c," en decimal= ", d)
               case "0":
                   print("Adéu")
               case other:
                   print("Opció no vàlida!")