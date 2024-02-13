"Sucesión de Fibonacci"

def fibonacci():
    prev_prev = 0
    prev = 1
    next = 2
    
    for index in range(0,50):
        print(prev_prev)
        fib = prev_prev + prev + next
        prev_prev = prev
        prev = next
        next = fib
        

fibonacci()
