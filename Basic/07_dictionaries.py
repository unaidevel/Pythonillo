### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Unai", "Apellido":"Munoz", "Edad":23, 1:"Python"}

my_dict = {"Nombre":"Unai", 
           "Apellido":"Munoz", 
           "Edad":23,
            "Lenguajes":{"Python," "Swift", "Kotlin"},
            1:1.77
        }

print (my_other_dict)
print(my_dict)


print(len(my_other_dict))
print(len(my_dict))

print(my_dict['Nombre'])

my_dict["Nombre"] = 'Manolo'
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle Unai"  #anadir valores al diccionario
print(my_dict)

del my_dict ["Calle"] #como eliminar un elemento del diccionario
print(my_dict)

print("Unai" in my_dict)   #Busca por clave, no por valor
print("Apellido" in my_dict)
print(my_dict["Apellido"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, ("Unai", "Munoz"))
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict)) #Transformandolo en una lista solamente da las claves
print(tuple(my_new_dict))
print(set(my_new_dict))
