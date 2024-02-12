### Higher Order Functions ###

from functools import reduce

def sum_one(value):
    return value + 1
def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))


### Closures ###

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1) #Este 1 es original value
print(add_closure(5))
print(sum_ten(5)(1))


### Built-in Higher Order Functions ### 

numbers = [2, 5, 10, 21, 3, 15, 30, 74]
 
#Map
    # Recorre todos los valores y ejecuta una función sobre ellos para modificar su valor.


def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter
# Recorre todos los valores y ejecuta una función que retorna True or False para saber como filtrar los valores 
    #del iterable

def filter_greater_that_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
print("Esto empieza aquí")
def sum_two_values (first_value, second_value): 
    print(first_value)
    print(second_value)
    return first_value + second_value 
print(reduce(sum_two_values, numbers)) 