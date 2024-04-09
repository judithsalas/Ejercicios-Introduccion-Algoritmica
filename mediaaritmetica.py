'''
Este código proporciona una función llamada `calcular_media_aritmetica` que se utiliza 
para calcular la media aritmética de tres números dados. La función toma como entrada los tres números 
y devuelve la media aritmética calculada.

El ejemplo de uso al final del código permite al usuario ingresar los tres números y 
luego muestra la media aritmética calculada. 
En resumen, este código es útil para calcular la media aritmética de un conjunto de tres números.
'''

def calcular_media_aritmetica(numero1, numero2, numero3):
    # Calcular la suma de los tres números
    suma = numero1 + numero2 + numero3
    
    # Calcular la media aritmética
    media = suma / 3
    
    return media

# Ejemplo de uso
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

media = calcular_media_aritmetica(numero1, numero2, numero3)
print("La media aritmética de los tres números es:", media)
