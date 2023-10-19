def final(arreglo):
    #se usa sorted para que todos las x iguales a 0 vayan al final
    ordenado = sorted(arreglo, key=lambda x: x == 0)
    return ordenado

n = int(input("Ingrese la cantidad de números en el arreglo: "))
arreglo = []


for i in range(n):

    #se pide que ingrese numeros n cantidad de veces
    numero = int(input(f"Ingrese un número {i + 1}: "))
    arreglo.append(numero)
    
arreglo_final = final(arreglo)
print(arreglo_final)
