'''
Este código en está diseñado para calcular el área de un triángulo, 
dadas la longitud de su base y su altura. Al ejecutarlo, solicita al usuario que ingrese estos dos valores. 
Utiliza una fórmula sencilla, que es la multiplicación de la base por la altura dividida entre dos, para calcular 
y luego mostrar el área del triángulo. Además, este enfoque también es válido para calcular el área de un triángulo 
rectángulo, utilizando las longitudes de los lados perpendiculares como la base y la altura.

Contestando a la segunda pregunta, sí, se deberán de proporcionar los lados perpendiculares para el cálculo de su área.
'''

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# Uso del código para calcular el área de un triángulo
base = float(input("Ingrese la longitud de la base: "))
altura = float(input("Ingrese la longitud de la altura: "))

area_triangulo = calcular_area_triangulo(base, altura)
print("El área del triángulo es:", area_triangulo)
