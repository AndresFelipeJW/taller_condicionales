# Programa que lea las coordenadas cartesianas (x, y) de un punto en el plano y calcule el cuadrante al cual pertenece el punto y si el punto está sobre un eje también debe indicarlo.

print("--------------------------------")
print("------ INGRESE UN NUMERO -------")
print("--------------------------------")

#input

x = float(input("Ingrese la coordenada x: "))
y = float(input("Ingrese la coordenada y: "))

#processing

if x == 0 and y == 0:
    print("El punto se encuentra en el origen.")
if x > 0 and y > 0:
    print("El punto se encuentra en el I cuadrante.")
if x < 0 and y > 0:
    print("El punto se encuentra en el 	II cuadrante.")
if x < 0 and y < 0:
    print("El punto se encuentra en el 	III cuadrante.")
else:
    print("El punto se encuentra en el IV cuadrante.")