# numero de linea
line = 1
# numero de columna
col = 1

tokens = []


# formar un string
def tokenize_string(input_str, i):
    token = ""
    print("POSICION: ", i)
    for char in input_str:
        if char == '"':
            return [token, i]
        token += char
        i += 1
    print("Error: string no cerrado")


def tokenize_number(input_str, i):
    token = ""
    for char in input_str:
        if char.isdigit() or char == ".":
            token += char
            i += 1
        else:
            break
    return [token, i]


def tokenize_input(input_str):
    # referenciar las variables globales
    global line, col, tokens
    # iterar sobre cada caracter del input
    i = 0
    # mientras no se llegue al final del input
    while i < len(input_str):
        # obtener el caracter actual
        char = input_str[i]
        print({"char": char, "line": line, "col": col, "i": i})
        if char.isspace():
            # si es un salto de linea
            if char == "\n":
                tokens.append("EOL")
                line += 1
                col = 1
            # si es un tabulador
            elif char == "\t":
                col += 4
            # si es un espacio
            else:
                col += 1
            # incrementar el indice
            i += 1
        # si es un string formar el token
        elif char == '"':
            token, pos = tokenize_string(input_str[i + 1 :], i)
            i = pos + 2
            print("SALIDA:", i)
            tokens.append(token)
            col += len(token) + 1
        elif char in ["{", "}", "[", "]", ",", ":"]:
            tokens.append(char)
            col += 1
            i += 1
        elif char.isdigit():
            token, pos = tokenize_number(input_str[i:], i)
            i = pos + 1
            tokens.append(token)
            col += len(token) + 1
        else:
            print(
                "Error: caracter desconocido:",
                char,
                "en linea:",
                line + 1,
                "columna:",
                col + 1,
            )
            i += 1
            col += 1


entrada = open("ejemplo_entrada.json", "r").read()
tokenize_input(entrada)
for i in tokens:
    print("Token: ", i)
