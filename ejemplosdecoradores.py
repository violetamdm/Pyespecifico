# DECORADORES:
"""
Los decoradores son funciones que "gestionan" a otras 
funciones antes de llamarlas.
"""

## SINTAXIS:
def decorador(funcion):
    pass

@decorador
def funcion_a_decorar():
    pass

## EJEMPLO CON PRINT:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

my_decorator("hola")

## EJEMPLO CON TRY:
def decorador(funcion):
    def funcion_aux_del_decorador():
        x=""
        try:
            print('esto petará')
        except NameError:
            x = "Variable x is not defined"
        except:
            x = "Something else went wrong"
        return x
    return funcion_aux_del_decorador()
    
@decorador
def funcion_a_decorar():
    pass

