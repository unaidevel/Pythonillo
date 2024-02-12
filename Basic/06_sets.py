### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Unai", "Manolardo", 23}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Mongolino") 

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("Mongolino") # Un set no admite repetidos

print(my_other_set)

print("Unae" in my_other_set)  #Comprobar objeto de set
print("Unai" in my_other_set)

my_other_set.remove("Unai")    #Remover objeto
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) Name Error: name 'my_other_set'is not defined

my_set = {"Unai", "Munoz", 23}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Mongolo", "Francés"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Javascript", "C#"})) 
#los primeros union no funcionan porque en los sets no se puede duplicar

print(my_new_set.difference(my_set))


