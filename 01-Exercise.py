"""
Crear una función llamada devolver_distintos() que reciba 3 integers como parámetros
Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el número menor. 
Si la suma de los 3 numeros es un valor entre 10 y 15 (incluidos), va a devolver el número 
de valor intermedio. 
"""

def devolver_distintos(*numbers):
    """
    Devolver_distintos
    """
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    sum_numbers = a + b + c
    number = 0
    if sum_numbers  > 15 :
        number = my_list[0]
    elif sum_numbers < 10 :
        number = my_list[2]
    elif sum_numbers >= 10 and sum_numbers <= 15 :
        number = my_list[1]
    return number


print(devolver_distintos(2,5,3))
