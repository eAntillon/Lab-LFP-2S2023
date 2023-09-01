from Expresiones.expresion import *
import math
class ExpresionTrigonometrica(Expresion):
    def __init__(self, tipo, valor, linea, columna):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea
        self.columna = columna

    
    def interpretar(self):

        valor = self.valor
        # validar si es un numero o una Expresion
        if isinstance(self.valor, Expresion):
            valor = round(self.valor.interpretar(), 2)

        print("`"*20)
        print("tipo: ", self.tipo)
        print("valor: ", valor)
        if self.tipo == "seno":
            return math.sin(valor)
        