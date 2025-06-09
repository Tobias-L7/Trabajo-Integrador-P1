# Algoritmo de busqueda binaria por listas modificado para Tuplas
def busqueda_binaria_tuplas(lista, objetivo):
    inicio = 0
    fin = len(lista)-1
    while inicio <= fin:
        medio = (inicio+fin)//2
        dato = lista[medio][0]
        if dato == objetivo:
            return medio
        elif dato < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

#Algoritmo de ordenamiento: Bubble Sort
def ordenamiento(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]