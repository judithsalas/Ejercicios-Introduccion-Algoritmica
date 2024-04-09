'''
El siguiente código proporciona una función llamada calcular_precio_con_impuestos que se utiliza para calcular el 
valor con todos los impuestos incluidos (TII) dados un costo sin impuestos y un porcentaje de IVA. 
La función toma dos parámetros: precio_sin_impuestos, que es el precio base sin impuestos, y porcentaje_iva, 
que es el porcentaje de impuestos sobre el precio base. Luego, devuelve el precio final con impuestos incluidos.

En el final del código se muestra cómo usar la función, 
solicitando al usuario que ingrese el precio sin impuestos y el porcentaje de IVA, 
y luego imprime el precio final con todos los impuestos incluidos. 
En resumen, este código es útil para calcular el precio total de un producto o servicio, 
teniendo en cuenta los impuestos aplicables.'''

def calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_iva):
    # Calcular el monto del impuesto
    impuesto = precio_sin_impuestos * (porcentaje_iva / 100)
    
    # Calcular el precio con impuestos incluidos
    precio_con_impuestos = precio_sin_impuestos + impuesto
    
    return precio_con_impuestos

# Ejemplo de uso
precio_sin_impuestos = float(input("Ingrese el precio sin impuestos: "))
porcentaje_iva = float(input("Ingrese el porcentaje de IVA: "))

precio_final = calcular_precio_con_impuestos(precio_sin_impuestos, porcentaje_iva)
print("El precio con todos los impuestos incluidos es:", precio_final)
