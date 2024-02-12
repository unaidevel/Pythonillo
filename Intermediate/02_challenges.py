### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ"
Escribe un programa que muestre por consola (con un print) los 
números de 1 a 100(ambos incluidos y con un salto de línea entre cada impresión),
sustituyendo los siguientes: 
-Múltiplos de 3 por la palabra "fizz"
-Múltiplos de 5 por la palabra "buzz"
-Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
""" 


def acertijo():
    for number in range(1, 101):
        
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)
#Se imprimen correctamente porque: Si no se cumple el primer if, pasa al elif, sino al otro elif
# sino al else hasta completarse.           
acertijo()




"""
ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne verdadero o falso(Bool)
según sean o no anagramas.
-Un anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial
-No hace falta comprobar que ambas palabras existan
-Dos palabras exactamente iguales no son anagrama
""" 


def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower()) 
# El sorted va a ordenar todas las letras de la palabra
print(is_anagram("Amor", "roma"))


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
-La serie Fibonacci se compone por una sucesión de números en la que el siguiente
siempre es la suma de los dos anteriores. 0, 1, 1, 2, 3, 5, 8, 13...
"""

#Lo he hecho en vez de 2 con 3 números para darle un poco más de dificultad.


def sucesión_fibonacci():
    prev_prev = 0
    prev = 1
    next = 2

    for index in range (0, 50):
        print(prev_prev)    
        fib = prev_prev + prev + next
        prev_prev = prev
        prev = next 
        next = fib
sucesión_fibonacci()


"""
ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo. Hecho esto, imprime los
números primos entre 1 y 100.
"""


def numeros_primos():
    for numeros in range(1, 101):
        if numeros >= 2:
            
            is_divisible = False
            for index in range(2, numeros):
                if numeros % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:   
                print(numeros)


numeros_primos()


"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
-Si le pasamos "Hola Mundo" nos retornaria "odnum aloH"

"""

def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range (0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text

print(reverse("Hola Mundo"))










