from Expresiones.expresion import *
import math
class ExpresionAritmetica(Expresion):
    def __init__(self, tipo, valor1, valor2, linea, columna):
        self.tipo = tipo
        self.valor1 = valor1
        self.valor2 = valor2
        self.linea = linea
        self.columna = columna


    def interpretar(self):
        valor1 = self.valor1
        valor2 = self.valor2
        
        # validar si es un numero o una Expresion
        if isinstance(self.valor1, Expresion):
            valor1 = round(self.valor1.interpretar(), 2)
            print("RESULTADO: ", valor1)
        
        if isinstance(self.valor2, Expresion):
            valor2 = round(self.valor2.interpretar(), 2)
            print("RESULTADO: ", valor2)

        print("`"*20)
        print("tipo: ", self.tipo)
        print("valor1: ", valor1)
        print("valor2: ", valor2)
        
        
        if self.tipo == "suma":
            return valor1 + valor2
        elif self.tipo == "resta":
            return valor1 - valor2
        elif self.tipo == "multiplicacion":
            return valor1 * valor2
        elif self.tipo == "potencia":
            return math.pow(valor1, valor2)
        elif self.tipo == "raiz":
            return math.pow(valor1, 1/valor2)

    def __str__(self) -> str:
        return super().__str__() + " tipo: " + self.tipo + " valor1: " + str(self.valor1) + " valor2: " + str(self.valor2)

        
        
    
    