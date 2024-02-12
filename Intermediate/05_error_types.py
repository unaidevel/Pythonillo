### Error Types ###

# SyntaxError
#print "Hola Comunidad!" # Descomentar para errorError
print("Hola Comunidad!")

# NameError
language = "Spanish"  # Comentar para error
print(language)     # Error por no definir 'language' primero

# Index Error
my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]
print(my_list[1])
print(my_list[-1])
print(my_list[0])
#print(my_list[5])   #Error, te has pasado de rango

# ModuleNotFoundError
#import maths #Descomentar para Error
import math

# AttributeError
#print(math.PI) #Descomentar para Error
print(math.pi)

#KeyError
my_dict = {"Nombre": "Unai", "Apellido":"Munoz", "Edad":23, 1:"Python"}
print(my_dict["Edad"])
#print(my_dict["Apeyido"]) #Descomentar para error.

# TypeError
my_list = ["Python", "Swift", "Kotlin", "Dart", "Javascript"]
#print(my_list["Kotlin"]) #Descomentar para error.
#print(my_list["0"]) #Descomentar para error.
print(my_list[0])

# ImportError
#from math import PI #Descomentar para Error
from math import pi
print(pi)

# ValueError
#my_int = int("10 anos") #Descomentar para Error
my_int = int("10")
print(type(my_int))

#ZeroDivisionError
print(4/0) #Descomentar para Error
print(4/2)


