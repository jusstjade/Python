def llegir_paraula():
    return(input("Introduce una palabra"))
def comparar_paraules(a,b):
    if a==b:
        print("Son iguals, per tant rimen")
    elif a[-3:]==b[-3:]:
        print("Rimen, perque les 3 darreres lletres són iguals")
    elif a[-2:]==b[-2:]:
        print("Rimen un poc, perque les 2 darreres lletres són iguals")

a= llegir_paraula()
b= llegir_paraula()
compara_paraules(a,b)