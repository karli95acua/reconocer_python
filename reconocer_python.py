# EJERCICIO RECONOCER PYTHON

num1 = 42  # variable declaration: a num1 se le asigna valor de 42, lo que corresponde a "Number" --> primitive data type
num2 = 2.3 # variable declaration: a num2 se le asigna valor de 2.3, lo que corresponde a "Number" del tipo flotante --> primitive data type
boolean = True # variable declaration: al boolean se le asigna valor de True, lo que corresponde a un "Boolean" --> primitive data type
string = 'Hello World' # variable declaration: a string se le asigna un valor de 'Hello World', lo que corresponde a un "String" --> primitive data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration: a pizza_toppings se le asigna una "List", o sea pizza_toppings es una lista --> Composite data type
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration: a person se le asigna un "Dictionary", o sea person es un diccionario --> Composite data type
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration: a fruit se le asigna un "Tuple", o sea fruit es un tuple --> Composite data type
print(type(fruit)) # log statement: imprime el tipo de variable que es "fruit" --> print es una función incorporada de Python del tipo Declaración de Salida
print(pizza_toppings[1]) # log statement: imprime el segundo valor de izquierda a derecha o index 1 de la lista de pizza_toppings --> access value

pizza_toppings.append('Mushrooms') # List method: agrega "Mushrooms" a lista de pizza_toppings --> add value

print(person['name']) # log statement: imprime el valor de "name" clave del diccionario person --> access value
person['name'] = 'George' # Dictionary method: cambia el valor "name" clave del diccionario person a "George" --> change value
person['eye_color'] = 'blue' # Dictionary method: aagrega una nueva clave-valor al diccionario person --> add value

print(fruit[2]) # log statement: imprime el tercer valor de izquierda a derecha o index 2 del tuple fruits --> access value




if num1 > 45: # conditional: la condicional if revisa si el num1 es mayor a 45
    print("It's greater") # log statement: imprime "It's greater" si la condicional if es True
else: # conditional: la condicional else se ejecuta si la condición if es False
    print("It's lower") # log statement: imprime "It's lower" si la condición if es False



if len(string) < 5: # conditional: la condicional if revisa si el largo de la string es menor a 5
    print("It's a short word!") # log statement: imprime "It's a short word!" si la condicional if es True
elif len(string) > 15: # conditional: la condicional elif revisa si el largo de la string es mayor a 15 si la condición if previa es False
    print("It's a long word!") # log statement: imprime "It's a long word!" si la condición de elif es True
else: # conditional: condicional else ejecuta algo si las condiciones if y elif previas son False 
    print("Just right!") # log statement: imprime "Just right!" si las condiciones if y elif son False





for x in range(5): # for loop: una secuencia loop
    print(x) # log statement: imprime el valor actual de x
for x in range(2,5): # for loop: una secuencia loop
    print(x) # log statement: imprime el valor actual de x
for x in range(2,10,3): # for loop: una secuencia loop
    print(x) # log statement: imprime el valor actual de x
x = 0 # variable declaration: a x se le asigna un valor de 0, el cual es un "Number" --> primitive data type
while(x < 5): # while loop: un loop while en donde se revisa si x es menor a 5 y si es True ejecuta el bloque de código dentro del loop
    print(x) # log statement: imprime el valor actual de x
    x += 1 # increment: incrementa el valor de x en 1



pizza_toppings.pop() # List method: remueve el último valor de la lista pizza_toppings --> delete value
pizza_toppings.pop(1) # List method: remueve el segundo valor de izquierda a derecha o index 1 de la lista pizza_toppings --> delete value

print(person) # log statement: imprime el diccionario person
person.pop('eye_color') # Dictionary method: remueve el valor clave 'eye_color' del diccionario person --> delete value
print(person) # log statement: imprime el diccionario person

for topping in pizza_toppings: # for loop: una secuencia loop donde se revisa cada topping dentro de la lista pizza_toppings
    if topping == 'Pepperoni': # conditional: condicional if revisa si el valor actual del topping es "Pepperoni"
        continue # control flow: si la condición if anterior es True, deja la revisión y comienza a iterar la instrucción que viene ahora
    print('After 1st if statement') # log statement: imprime "After 1st if statement"
    if topping == 'Olives': # conditional: condicional if revisa si el valor actual del topping es "Olives"
        break # control flow: si la condicional if es True, rompe el loop y continúa ejecutando el código después del loop

def print_hello_ten_times(): # function declaration: se define una funcion llamada print_hello_ten_times sin parámetros
    for num in range(10): # for loop: un loop en donde num toma cada valor de la secuencia declarada hasta el rango
        print('Hello') # log statement: imprime "Hello"s

print_hello_ten_times() # function call: se llama a la función print_hello_ten_times

def print_hello_x_times(x): # function declaration: define una funcion llamada print_hello_x_times con el parametro x
    for num in range(x): # for loop: un loop en donde num toma cada valor de la secuencia declarada hasta el rango
        print('Hello') # log statement: imprime "Hello"

print_hello_x_times(4) # function call: se llama a la función print_hello_x_times con el argumento 4

def print_hello_x_or_ten_times(x = 10): # function declaration: se define a la función llamda print_hello_x_or_ten_times con un parámetro en donde x vale 10
    for num in range(x): # for loop: un loop en donde num toma cada valor de la secuencia declarada hasta el rango
        print('Hello') # log statement: imrpime "Hello"

print_hello_x_or_ten_times() # function call: se llama a la función print_hello_x_or_ten_times y se mantiene valor ya enunciado
print_hello_x_or_ten_times(4) # function call: se llama a la función print_hello_x_or_ten_times y x es 4

"""
Bonus section
"""

# print(num3) # NameError: respuesta terminal --> name'num3' is not defined
# num3 = 72 # variable declaration: ahora a num3 se le asignó el valor de 72, esto es un "Number" --> primitive data type
# fruit[0] = 'cranberry' # TypeError: respuesta terminal --> 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: respuesta terminal --> 'favorite_team'
# print(pizza_toppings[7]) # IndexError: respuesta terminal --> list index out of range
#   print(boolean) # IndentationError: respuesta terminal --> unexpected indent
# fruit.append('raspberry') # AttributeError: respuesta terminal --> 'tuple' object has no attribute 'append'
# fruit.pop(1) # AttributeError: respuesta terminal --> 'tuple' object has no attribute 'pop'
