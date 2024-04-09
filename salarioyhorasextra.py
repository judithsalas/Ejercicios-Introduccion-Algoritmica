'''
Este código está diseñado para calcular el importe adicional que debe pagarse por las horas extra trabajadas 
por un empleado, basándose en su salario mensual bruto. 

La lógica de cálculo toma en cuenta dos rangos de incremento para las horas extra: 
las primeras 8 horas extra se pagan con un 125% de incremento sobre la tarifa horaria normal, 
y las horas extra subsiguientes se pagan con un 150% de incremento. 

La tarifa horaria normal se calcula dividiendo el salario mensual bruto entre el total de horas trabajadas en un mes estándar 
(140 horas, asumiendo 35 horas semanales por 4 semanas). Este script es útil en contextos laborales donde se  
compensan las horas extra a diferentes tasas incrementales, facilitando a los empleadores el cálculo preciso del  
pago adicional debido por trabajo extra más allá de la jornada laboral estándar.

'''
def calcular_pago_horas_extra(salario_mensual_bruto, horas_extra):
    # Supuestos
    horas_normales_por_semana = 35
    semanas_por_mes = 4
    
    # Cálculo de la tarifa por hora
    tarifa_hora_normal = salario_mensual_bruto / (horas_normales_por_semana * semanas_por_mes)
    
    # Inicialización del pago de horas extra
    pago_horas_extra = 0
    
    # Cálculo de pago para las primeras 8 horas extra (36ª a 43ª hora)
    if horas_extra > 8:
        pago_horas_extra += 8 * tarifa_hora_normal * 1.25
        horas_extra -= 8
    else:
        pago_horas_extra += horas_extra * tarifa_hora_normal * 1.25
        horas_extra = 0
    
    # Cálculo de pago para las horas extra restantes (a partir de la 44ª hora)
    if horas_extra > 0:
        pago_horas_extra += horas_extra * tarifa_hora_normal * 1.5
    
    return pago_horas_extra

# Ejemplo de uso
salario_mensual_bruto = float(input("Ingrese el salario mensual bruto: "))
horas_extra = int(input("Ingrese el número total de horas extra trabajadas: "))

pago_por_horas_extra = calcular_pago_horas_extra(salario_mensual_bruto, horas_extra)
print(f"El pago total por horas extra es: {pago_por_horas_extra:.2f}")
