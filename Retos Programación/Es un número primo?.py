
def primo():
    for numeros in range (1,101):
        if numeros >=2:

            is_divisible = False
            for index in range(2, numeros):
                if numeros % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(numeros)

primo()

