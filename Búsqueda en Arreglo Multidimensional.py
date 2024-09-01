#### UEA  ####


#### defino la matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
## desarrollo la busqueda
def buscar(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            ### comparamos
            if matriz[i][j] == valor:
                ## imprimimos el resultado
                return f" El valor {valor} fue encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz"
valor_buscado = 5
resultado = buscar(matriz, valor_buscado)
print(resultado)
