CantidadPasajes = []
ListaPasajero = []
asiento_Comun = 60000
EspacioAd_Piernas = 80000
no_Reclina = 50000

def registrarPersona ():
    nombres = int("ingrese nombre")    
    rut = int(input("Ingresar rut de la persona"))
    print("*******************************")
    for i in range (rut):
        print(i,rut[i])
        asientoComun = (60000)
        espacioPiernas = (80000)
        noReclina = (50000)
        cantidad_pasajes = (asientoComun+espacioPiernas+noReclina)
        nombre = nombres [cantidad_pasajes]

        ListaPasajero.append(nombre)


def ListaPasajeros ():

    print("CANTIDAD PASAJES \t NOMBRE \t RUT \t ASIENTOCOMUN \t ESPACIOPIERNAS \t NORECLINA \t")
    print("-------------------------------------------------------------------------------")

    # for i in range (CantidadPasajes):
    #     print(CantidadPasajes[i],[0]end=)
    #     print(CantidadPasajes[i],[1]end=)
    #     print(CantidadPasajes[i],[2]end=)
    #     print(CantidadPasajes[i],[3]end=)
    #     print(CantidadPasajes[i],[4]end=)
    #     print(CantidadPasajes[i],[5]end=)
    #     print()
        
while True:
    print("""
                    
          (1)Comprar Pasajes
          (2)Mostrar ubicaciones disponibles
          (3)Ver listado de pasajeros
          (4)Buscar pasajero
          (5)Reasignar asiento
          (6)Mostrar ganancias totales
          
          """)
    
    op = int(input("Ingresar opcion"))

    if op ==1:
        print("Compro pasaje")

    elif op ==2:
        print("mostro las ubicaciones disponibles")
    
    elif op ==3:
        print("lista pasajeros")

    elif op ==4:
        print("Pasajeros")

    elif op ==5:
        print("asigno asientos")
