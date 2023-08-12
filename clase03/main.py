
opcion = 0


lineas = []


def leerArchivoInicial():
    # leer el archivo .inv y va a retornar las lineas
    with open("entrada.inv", encoding="utf-8") as file:
        return file.readlines()

while(opcion != 4):
    print("-"*10)
    print("practica 1")

    print("1. Cargar inventario inicial")
    print("2. Cargar movimientos")
    print("3. Crear informe")
    print("4. Salir \n")

    print("Ingrese una opcion:")
    opcion = int(input())

    if opcion == 1:
        print("Cargar inventario")
        lineas =  leerArchivoInicial()
        print("ARCHIVO CARGADO EXITOSAMENTE")
        for i in lineas:
            print(i)
            instruccion = i.split(' ')
            if(instruccion[0] == "crear_producto"):
                print("Encontre una instruccion para crear")
            datos = instruccion[1].split(";")
            print(datos)
        pass
    elif opcion == 2:
        print("Cargar movimientos")
        pass
    elif opcion == 3:
        print("Crear informe")
        pass
    elif opcion == 4:
        print("Salida")
        break 


