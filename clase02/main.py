# manejopr de archivos
archivos = open('archivos/entrada.txt', 'r')

# leer una linea del archivo
linea = archivos.readline()
print(linea)

# leer todas las lineas del archivo
lineas = archivos.readlines()
print(lineas)


# leer todo el archivo
archivo = archivos.read()
print(archivo)


# escribir un archivo
archivos = open('archivos/entrada.txt', 'w')

# escribir una linea en el archivo de texto plano (sobreescribe el archivo) 
archivos.write('\n CAMBIO')

# cerrar el archivo para liberar memoria RAM y recursos del sistema operativo
archivos.close()


# manejo de archivos con with
with open('archivos/entrada.txt', 'r') as archivo:
    for linea in archivo:
        print(linea)

# agregar lineas al final del archivo
with open('archivos/entrada.txt', 'a') as archivo:
    for i in range(10):
        archivo.write(f'\n linea {i}')


