### Lists ###

#Constructores, maneras de crear una lista: 
my_list = list()
my_other_list = []


print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [23, 1.78, "Unai", "Munoz"]

print(type(my_other_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
print(my_other_list.count("Unai"))   #El .count es para buscar elementos en una lista.
#print(my_other_list[4])
#print(my_other_list[-5])

age, height, address, surname = my_other_list
print(surname)

address, height, age, surname = my_other_list

print(my_list + my_other_list)
#print(my_list - my_other_list)


my_other_list.append("Manolardo")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30) #Remove para quitar un objeto que sabemos que está
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list [2]  #Hacer del, elimina por índice, aún sin saber que elemtno concreto hay.
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"
print(my_list)
print(type(my_list))
