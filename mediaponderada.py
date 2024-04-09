'''
Este código está diseñado para calcular la media ponderada de un conjunto de números, 
dados sus correspondientes coeficientes de ponderación. 
Se pide al usuario que introduzca una lista de números y una lista de sus ponderaciones respectivas. 
La función calcular_media_ponderada toma estas listas, 
verifica que tengan la misma longitud para asegurarse de que cada número tiene asociado 
un coeficiente de ponderación, y luego procede al cálculo. Esto se hace multiplicando cada número por 
su ponderación, sumando todos estos productos, y dividiendo el resultado por la suma de todas las ponderaciones. 

El resultado final es la media ponderada, que proporciona un único valor representativo del conjunto de números, 
teniendo en cuenta la importancia relativa (ponderación) de cada número.

'''

def calcular_media_ponderada(numeros, ponderaciones):
    # Verificar que las listas tengan la misma longitud
    if len(numeros) != len(ponderaciones):
        return "Error: Las listas de números y ponderaciones deben tener la misma longitud"
    
    # Calcular la suma de los productos de cada número por su ponderación
    suma_productos = sum([numeros[i] * ponderaciones[i] for i in range(len(numeros))])
    
    # Calcular la suma de las ponderaciones
    suma_ponderaciones = sum(ponderaciones)
    
    # Calcular la media ponderada
    media_ponderada = suma_productos / suma_ponderaciones
    
    return media_ponderada

# Ejemplo de uso
numeros = [float(x) for x in input("Ingrese los números separados por espacios: ").split()]
ponderaciones = [float(x) for x in input("Ingrese las ponderaciones separadas por espacios: ").split()]

media = calcular_media_ponderada(numeros, ponderaciones)
print("La media ponderada es:", media)
