### Loops ###

# While: Sirve para hacer que algo se repita un numero de veces en función de una condición
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1 
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continúa")

my_list = [23, 12, 41, 39, 39, 14, 22]

#for: Se va a repetir tantas veces como elementos iterables tengamos.

for element in my_list:
    print(element)

my_tuple = (23, 1.77, "Unai", "Munoz", "Mongolardo")
for element in my_tuple:
    print(element)

my_set = {"Unai", "Munoz", 23}
for element in my_set:
    print(element)

my_dict = {"Nombre":"Unai", "Apellido":"Munoz", "Edad":23}
for element in my_dict:
    print(element)
    if element == "Edad":
        continue #este continue vuelve al for sin importar lo que está abajo
        break #el break termina con el bucle for y sigue ejecuntando lo siguiente
    print("se ejecuta")
else: 
    print("El bucle for para diccionario ha finalizado")
