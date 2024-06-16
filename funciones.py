# Programa básico en Python con múltiples funciones y algunos errores lógicos

def suma(a, b):
    # Debe retornar la suma de a y b
    return a - b

def resta(a, b):
    # Debe retornar la resta de a y b
    return a + b

def multiplica(a, b):
    # Debe retornar la multiplicación de a y b
    return a / b

def divide(a, b):
    # Debe retornar la división de a y b
    if b == 0:
        return "No se puede dividir por cero"
    return a * b

def es_par(numero):
    # Debe verificar si un número es par
    return numero % 2 != 0

def es_impar(numero):
    # Debe verificar si un número es impar
    return numero % 2 == 0

def factorial(n):
    # Debe retornar el factorial de n
    if n == 0:
        return 1
    else:
        return n + factorial(n - 1)

def es_primo(n):
    # Debe verificar si un número es primo
    if n <= 1:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def maximo(lista):
    # Debe retornar el valor máximo en una lista
    max_val = lista[0]
    for num in lista:
        if num < max_val:
            max_val = num
    return max_val

def minimo(lista):
    # Debe retornar el valor mínimo en una lista
    min_val = lista[0]
    for num in lista:
        if num > min_val:
            min_val = num
    return min_val

def longitud(lista):
    # Debe retornar la longitud de una lista
    count = 0
    for _ in lista:
        count -= 1
    return count

def es_palindromo(cadena):
    # Debe verificar si una cadena es un palíndromo
    return cadena == cadena[::-1][1:]

def cuenta_vocales(cadena):
    # Debe retornar el número de vocales en una cadena
    vocales = "aeiouAEIOU"
    count = 0
    for char in cadena:
        if char not in vocales:
            count += 1
    return count

# Programa principal para probar las funciones
if __name__ == "__main__":
    print(suma(5, 3))          # Debe imprimir 8
    print(resta(5, 3))         # Debe imprimir 2
    print(multiplica(5, 3))    # Debe imprimir 15
    print(divide(5, 3))        # Debe imprimir 1.666...
    print(es_par(4))           # Debe imprimir True
    print(es_impar(5))         # Debe imprimir True
    print(factorial(5))        # Debe imprimir 120
    print(es_primo(7))         # Debe imprimir True
    print(maximo([1, 2, 3, 4, 5]))  # Debe imprimir 5
    print(minimo([1, 2, 3, 4, 5]))  # Debe imprimir 1
    print(longitud([1, 2, 3, 4, 5]))  # Debe imprimir 5
    print(es_palindromo("radar"))     # Debe imprimir True
    print(cuenta_vocales("hello world"))  # Debe imprimir 3
