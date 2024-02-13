"Ejercicio Fizzbuzz"

def fizzbuzz ():

    for number in range(1,101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        if number % 5 == 0:
            print("buzz")
        if number % 3 == 0:
            print("fizz")
        else:
            print(number)

fizzbuzz()
