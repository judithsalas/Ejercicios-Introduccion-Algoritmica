'''
Este código proporciona una función llamada calcular_intereses que se utiliza para calcular 
el importe de los intereses generados por un capital invertido a un interés dado durante un tiempo dado, 
expresado en meses. La función toma tres parámetros: capital, que representa la cantidad de dinero invertida, 
tasa_interes_anual, que es el porcentaje de interés anual aplicado a la inversión, y tiempo_meses, que es 
el período de tiempo durante el cual se invirtió el capital en meses.

El ejemplo de uso al final del código permite al usuario ingresar los valores del capital, 
la tasa de interés anual y el tiempo en meses, y luego imprime el importe de los intereses generados 
por esa inversión. En resumen, este código es útil para calcular los intereses generados por una inversión 
financiera dada una tasa de interés y un período de tiempo en meses.
'''
def calcular_intereses(capital, tasa_interes_anual, tiempo_meses):
    # Calcular la tasa de interés mensual
    tasa_interes_mensual = tasa_interes_anual / 12
    
    # Calcular los intereses generados
    intereses_generados = capital * (tasa_interes_mensual / 100) * tiempo_meses
    
    return intereses_generados

# Ejemplo de uso
capital = float(input("Ingrese el capital invertido: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual (%): "))
tiempo_meses = int(input("Ingrese el tiempo en meses: "))

intereses = calcular_intereses(capital, tasa_interes_anual, tiempo_meses)
print("Los intereses generados son:", intereses)
