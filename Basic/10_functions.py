### Functions ###

def my_function():
    print("Esto es una función")
my_function()
my_function()
my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(52132, 41221)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Munoz", name = "Unai")

def print_name_with_default(name, surname, alias = "Sin alias"):  #Valor por defecto, sirve para que tenga un valor en caso de no llamarlo después
    print(f"{name} {surname} {alias}")

print_name_with_default("Unai", "Munoz")

def print_upper_text(*text):
    for texts in text:
        print(text.upper())


print_upper_text("Hola")
print_upper_text("Hola", "Mangolo", "Holuuuu")