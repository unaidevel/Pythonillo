### Exceptions Handling ###

numberOne, numberTwo = 5, 1
numberTwo = "1"


# Try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: 
    # Se ejecuta si se produce una excepción 
    print("Se ha producido un error")


# Try-except-else-finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except: 
    print("Se ha producido un error")

else: #opcional
    #Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")

finally: #opcional
    # Se ejecuta siempre
    print("La ejecución continúa")


# Exceptiones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError: #Solo se ejecuta si hay un ValueError
    print("Se ha producido un ValueError")
except TypeError: #Solo se ejecuta si hay un TypeError
    print("Se ha producido un TypeError") 


#Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error: #le damos nombre a la variable del error
    print(error)
except Exception as exceptionError: 
    print(exceptionError)