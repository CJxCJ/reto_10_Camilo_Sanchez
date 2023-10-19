#funcion de  punto producto
def producto(arreglo1, arreglo2):
    if len(arreglo1) != len(arreglo2):
        True
    
    multi = 0
    for i in range(len(arreglo1)):
        multi += arreglo1[i] * arreglo2[i]
    return multi

#pedir que ingrese los valores de los arreglos
n = int(input("Ingrese la longitud de los arreglos: "))

arreglo1 = []
arreglo2 = []

#se pide que ingrese numeros n cantidad de veces para el primer arreglo 
print("Ingrese los valores del primer arreglo:")
for i in range(n):
    num = float(input(f"Valor {i + 1}: "))
    arreglo1.append(num)

#se pide que ingrese numeros n cantidad de veces para el segundo arreglo 
print("Ingrese los valores del segundo arreglo:")
for i in range(n):
    num = float(input(f"Valor {i + 1}: "))
    arreglo2.append(num)

#se imprime el producto punto 
prod = producto(arreglo1, arreglo2)
print(f"El producto punto de los arreglos es: {prod}")
