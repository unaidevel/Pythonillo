### Lambdas ###

sum_two_values = lambda first_value, second_value: print(first_value + second_value)
print(sum_two_values(1, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 7))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))



lambda_func = lambda x: x**2
print(lambda_func(3))

#Lambda más sencillo: 
lambda_func = lambda x: True if x**2 >= 10 else False
lambda_func(3) # Retorna False
lambda_func(4) # Retorna True

