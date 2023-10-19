#funcion para el promedio del arreglo
def promedio(arreglo):
    if len(arreglo) == 0:
        return 0 
    suma = sum(arreglo)
    promedio = suma / len(arreglo)
    return promedio

#se pide que ingrese la cantidad de valores en el arreglo
n = int(input("Ingrese la cantidad de números en el arreglo: "))
arreglo = []

#se pide que ingrese numeros n cantidad de veces
for i in range(n):
    numero = float(input(f"Ingrese un número {i + 1}: "))
    arreglo.append(numero)

#muestra el promedio
prom = promedio(arreglo)
print(f"El promedio de los números es: {prom}")

