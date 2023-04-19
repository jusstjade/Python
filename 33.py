import random 
import time

puntuacion = 0 # Variable para almacenar la puntuación 

# Función donde explicamos qué pasa
def intro():
    print ("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar,
    Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.
    Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran
    i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.
    """)

# Funció on demanem a quin talaiot volem anar
def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

# Funció que ens indica si compartiran el menjar o serem nosaltres el seu àpat
def trobada(canviTalaiot):
    global puntuacion # Para acceder a la variable puntuación

    print ("T'estas apropant al talaiot...")
    time.sleep(2)
    print ("Està fosc i és tenebrós...")
    time.sleep(2)
    print ("Un gran gegant salta davant teu, t'agafa i ...")
    print ("")
    time.sleep(2)
    gegantamic = random.randint (1, 2)
    if canviTalaiot == str(gegantamic):
        print ("Et convida a menjar...")
        puntuacion += 1 # Sumamos 1 punto a la puntuación 
    else:
        print ("Se't menja d'un mos...ÑAMÑAMÑAM")
        puntuacion -= 1 # Restamos 1 punto a la puntuación

# Funció principal 
partidaNova = ("si")
while partidaNova == ("s") or partidaNova == ("si"):
    intro()
    nTalaiot = canviTalaiot()
    trobada(nTalaiot)
    print("Tu puntuación actual es: ", puntuacion)
    partidaNova = input("Vols tornar a mejar (jugar)? Introdueixi si o no: ")
    print("\n")
