### Regular Expressions ###

# https://regex101.com/   Aprender, montar  y validar expresiones regulares. Muy recomendable.


import re

my_string = "Esta es la lección número 7: lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I) 
print(match)
start, end = match.span()
print(my_string[start:end])



match = re.match("Esta es la lección", my_other_string)
#if not(match == None): #Otra forma de comprobar el None
#If match is not None: #Otra forma más de comprobar el None
if match != None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])

print(re.match("Expresiones Regulares", my_string))

# search     #Hacer una busqueda de algo en concreto
 
search = re.search("lección", my_string, re.I)   #El re.I para que ignore si es mayus o minus 
print(search)
start, end = search.span()
print(my_string[start:end])

# findall    #Encontrar todos los resultados que busquemos

findall = re.findall("lección", my_string, re.I)
print(findall) 

# split  #Hacer un split donde deseemos

print(re.split(":", my_string))

# sub     #Sustituir cadenas de texto

print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))


# Patterns

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.findall(pattern, my_string))

pattern = r"\d"   #\d significa hacer match donde el string contiene dígitos
print(re.findall(pattern, my_string))

pattern = r"\D" #\D significa hacer match donde el string no contiene digitos
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "unai@unai.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$" #el dolar significa que tenga en cuenta todo lo de atrás
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "unai@unai.com.mx"
print(re.findall(pattern, email))
