### Python Package Manager ###

# PIP https://pypi.org

# pip install pip
#pip --version

#pip install numpy
import numpy   

print(numpy.version.version)

numpy_array = numpy.array([1, 4, 6, 2, 33, 11])
print(type(numpy_array))

print(numpy_array * 2)

import pandas   #pip install pandas

# pip list    #sacar listado de paquetes instalados
# pip uninstall pandas
# pip show numpy

import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())


# Arithmetics Package 

from mypackage import arithmetmics

print(arithmetmics.sum_two_values(1, 4))