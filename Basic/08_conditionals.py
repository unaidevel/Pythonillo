### Conditionals ###


my_condition = False

if my_condition: #Es lo mismo que if my_condition == True: 
    print("Se ejecuta la condición del if")

my_condition = 5 * 3

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

elif my_condition > 10 and my_condition < 20: 
    print("Es mayor que 10 y menor que 20")
#Elif va relacionado con el primer if. Si no se cumple el if, va a elif(else if). 
#No se puede poner solamente elif#

elif my_condition == 1: 
    print("Es igual a 1")

else: 
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecución continúa")

my_string = "Mi cade de texto"

if not my_string:
    print("Mi cadena de texto es vacía")
if my_string == "Mi cadena de textooooooo":
    print("Estas cadenas  de texto no coinciden")
