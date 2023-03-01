
"""
https://j2logo.com/args-y-kwargs-en-python/

Parámetros especiales: 
    *args: 
        Número variable de argumentos opcionales posicionales.

    **kwargs:
        Número variable de argumentos opcionales con nombre.

"""

# pydantic par tipar

# Ejemplo *args:
def sum(*args: int):
    value = 0
    for n in args:
        value += n
    return value

print("funcion suma: 1 + 3 = ", sum(1, 3))
print("funcion suma: 1 + 3 + 5 + 98 = ", sum(1, 3, 5, 98))

# Ejemplo **kargs crea una consulta sql:
def filter(**kwargs):
    query = "SELECT * FROM clientes"
    i = 0
    for key, value in kwargs.items():
        if i == 0:
            query += " WHERE "
        else:
            query += " AND "
        query += "{}='{}'".format(key, value)
        i += 1
    query += ";"
    return query

print("funcion filter, genera consulta sql con dni y nombre sobre la tabla clientes:\n", filter(dni = "87745602L", nombre = "nombre"))

#Clases:

class num:
    
    def __init__(self, numero: int) -> None:
        self.numero = numero
    
    def funcion_sumar(self, numero:int) -> int: 
        return self.numero + numero
   
class operacion_con_un_numero(num):

    def __init__(self, numero: int, n: int) -> None:
        super().__init__(numero) 
        self.n = n

    def suma(self):
        return super().funcion_sumar(self.n)


class numeros():
    n1: num
    n2: num
    n3: num

    def __init__(self, n1: int, n2: int, n3: int) -> None:
        self.n1.__init__(n1)
        self.n2.__init__(n2)
        self.n3.__init__(n3)

    def suma(self):
        return super().funcion_sumar(self.n)
    

num1 = num(4)
nums = operacion_con_un_numero(6, 8)

print(nums.suma())