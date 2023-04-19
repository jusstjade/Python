# any%4==0 and (a%400> or a%100==0):
def any(a)
    if a %4==0 and (a%400> or a%100==0):
        print("Es any de traspaso")
    else:
        print("No es any de traspaso")
# PP
b=input("Introduce un any")
any(int(b))