#Variables

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#Algunas funciones del sistema
print(len(my_string_variable))

#Variables en una sola línea. Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Unai", "Munoz", "Tyson", 23
print("Me llamo", name, surname, "Mi edad es", age, "Y mi alias es:", alias)

# Inputs
name = input("Cuál es tu nombre? ")
age = input("Cuántos anos tienes? ")
print(name)
print(age)

# Cambiando su tipo
name = 23
age = "Unai"
print(name)
print(age)

#Forzamos el tipo?
address: str  = "Mi dirección"
address = 32
address = True
address = 1.2
print(type(address))