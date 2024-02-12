### Tuples ###

#Forma de crear tuplas
my_tuple = tuple()
my_other_tuple = ()


my_other_tuple = (23, "hola")
my_tuple = (23, 1.78, "Unai", "Munoz")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) index error
#print(my_tuple[-6]) index error

print(my_tuple.count("Unai"))
print(my_tuple.index("Munoz"))
print(my_tuple.index("Unai"))

#my_tuple[5] = 1.59
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "Manolardo" 
my_tuple.insert(1, "Negrako")
print(tuple(my_tuple))

#del my_tuple[2] Type Error: 'tuple'object doesnt support item deletion

del my_tuple
#print(my_tuple) NameError:a name 'my_tuple'is not defined
