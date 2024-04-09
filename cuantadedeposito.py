'''
Este código define y gestiona cuentas bancarias, permitiendo depositar y retirar dinero, y 
consultar el saldo. Incorpora la posibilidad de un descubierto autorizado, ofreciendo flexibilidad en 
las operaciones de retiro. 

La clase "Cuenta" representa una cuenta bancaria con un titular, saldo, y un límite 
de descubierto opcional. Este diseño facilita realizar operaciones bancarias básicas de forma segura, asegurando 
que las retiradas no excedan el saldo disponible más cualquier límite de descubierto establecido, proporcionando 
así una herramienta útil para la gestión financiera personal o empresarial.
'''

class Cuenta:
    def __init__(self, titular, saldo, limite_descubierto=0):
        self.titular = titular
        self.saldo = saldo
        self.limite_descubierto = limite_descubierto

    def __str__(self):
        return f"Cuenta de {self.titular}, Saldo: {self.saldo}, Límite de Descubierto: {self.limite_descubierto}"
 
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if self.saldo - cantidad >= -self.limite_descubierto:
            self.saldo -= cantidad
            return True
        return False

    def consultar_saldo(self):
        return self.saldo


mi_cuenta = Cuenta("Juan Perez", 1000)
print(mi_cuenta)

mi_cuenta.depositar(500)
print(mi_cuenta)

if not mi_cuenta.retirar(1600):
    print("Fondos insuficientes para esta retirada.")
else:
    print(mi_cuenta)

# Permitiendo un descubierto
mi_cuenta.limite_descubierto = 200
if mi_cuenta.retirar(1600):
    print("Retirada exitosa con descubierto.")
    print(mi_cuenta)
else:
    print("Fondos insuficientes, incluso con descubierto.")
