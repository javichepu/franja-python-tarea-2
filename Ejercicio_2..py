# 2: Función que calcule el área de un círculo 
# y otra que calcule el volumen de un cilindro usando la primera función.

#AREA DEL CIRCULO
importar matemáticas

radio = float(input("Ingrese el valor del radio de su circulo: "))
área = matemáticas. pi * (radio**2)
resultado = área
print(f"El resultado del area de su circulo es {resultado} ")
#VOLUMEN DEL CILINDRO (ZONA * h)
alturah = float(input("Ingrese la altura de su cilindro: "))
resultado = área * alturah 
print(f"El resultado del volumen del cilindro es {resultado}")