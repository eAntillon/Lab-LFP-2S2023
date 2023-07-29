estudiante = {
    'edad': 22,
    'dpi': 123456,
    'nombre': 'Erick'
}

# modificar un valor
estudiante['edad'] = 23

# agregar un valor
estudiante['apellido'] = 'Antillon'

# eliminar un valor
del estudiante['dpi']

# eliminar todos los valores

estudiante.clear()

print(estudiante)
estudiante = {
    'edad': 22,
    'dpi': 123456,
    'nombre': 'Erick'
}

# imprimir el diccionario

print(estudiante)

# imprimir un valor especifico

print(estudiante['edad'])


# iterar un diccionario

print("iterar un diccionario")
for key in estudiante:
    print(key, estudiante[key])

# iterar un diccionario con items
print("iterar un diccionario con items")
for key, value in estudiante.items():
    print(key, value)
