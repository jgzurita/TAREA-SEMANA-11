#### UEA ####


## DEFINO LA MATRIZ
matriz = [
    [3, 2, 7],
    [9, 8, 1],
    [6, 5, 4]
]
## desarrollamos mediante el metodo Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]
    return matriz
#### ordenamos la primera fila en este caso 0
fila_a_ordenar = 0

#imprimimos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)
# imprimimos la matriz ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)
