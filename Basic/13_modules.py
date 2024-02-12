### Modules ###

import my_module


my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")


from my_module import printValue, sumValue

sumValue(5, 2, 1)
printValue("Hola Python!")

import math

print(math.pi)
print(math.pow(2, 9))

from math import pi as PI_VALUE #Darle un alias a lo que importamos

print(PI_VALUE)
