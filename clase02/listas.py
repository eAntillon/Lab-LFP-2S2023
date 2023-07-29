# crear una lista de palabras de 3 palabras

letras =     ['a', 'b', 'w', 'd', 'e', 'f', 'g']
#posiciones    0    1    2    3    4    5    6
#inverso      -7   -6   -5   -4   -3   -2   -1


# imprimir la lista
print(letras)

# imprimir la longitud de la lista
print(len(letras))

# imprimir la lista en orden inverso
print(letras[::-1])


# list slicing
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:7])


# lista[inicio:fin:pasos]
# lista[inicio:fin] 
# lista[inicio:] == lista[inicio:len(lista)]
# lista[:fin] == lista[0:fin]
# lista[::pasos] == lista[::] == lista
# lista[:] == lista[::] == lista
# lista[::] == lista[:] == lista 


# iterables

# Mal uso
lista = [5, 4, 9, 2]
i = 0
while i < len(lista):
    elemento = lista[i]
    print(elemento)
    i += 1
# Salida: 5, 4, 9, 2

lista = [5, 4, 9, 2]
for elemento in lista:
    print(elemento)
# Salida 5, 4, 9, 2


# agregar un elemento a la lista
letras.append("a")

# agregar un elemento en una posicion especifica

letras.insert(4, "x")

# eliminar un elemento de la lista
letras.remove("e")

# eliminar el ultimo elemento de la lista
letras.pop()

# eliminar un elemento de la lista por su indice

del letras[0]

# eliminar todos los elementos de la lista

letras.clear()

numeros = [1, 10, 2, 8, 3, 11, 5, 4, 9]

# ordenar la lista
numeros.sort()

print("numeros ordenados: ", numeros)

# contar cuantos elementos hay en la lista
print('count: ', numeros.count('a'))

# posicion de un elemento en la lista
print('index: ', numeros.index('a'))


# list comprehension

unos = [1 for i in range(5)]
#[1, 1, 1, 1, 1]


cuadrados = [i**2 for i in range(5)]
#[0, 1, 4, 9, 16]


