#En un archivo llamado Empleados 2024, se encuentra una lista de empleados del año pasado.
#Se debe actualizar la lista con empleados nuevos ingresados este año y crear un archivo txt nuevo
#que contenga a todos los empleados, ordenandos por DNI de forma ascendente, ademas de poder comprobar
#que x empleado se encuentra en la lista
from utilitys import busqueda_binaria_tuplas, ordenamiento #-Importamos las funciones del archivo de utilidades

empleados2024 = {} #-En este diccionario se guardaran los empleados del archivo empleados 2024.txt

with open('Empleados 2024.txt', 'r', encoding='utf-8') as archivo:
#-Abrimos el archivo con la funcion open y pasando el nombre del archivo en el primer parametro
#-En el 2do parametro pasamor 'r', que significa que se debe leer el archivo
#-En el 3er parametro, usamos enconding='utf-8' para tomar los caracteres especiales

    for linea in archivo: #-En archivo se encuentra guardado el contenido del documento.txt, lo recorremos
        partes = linea.strip().split()#-Con .strip() quitamos los saltos de linea al principio y final de la cadena
        #-Con .split() divide la cadena en partes usando espacios y creamos un array
        nombre = partes[0]#-Donde el primer elemento se guardara en nombre
        apellido = partes[1]#-El 2do en apellido
        dni = int(partes[2])#El 3ro en DNI como entero
        empleados2024[dni] = f"{nombre} {apellido}"#-Y por ultimo, guardamos en el diccionario creado anteriormente
        #-Donde la key es el dni y su valor es el nombre y apellido del empleado

#Mostramos el diccionario con los empleados desordenados
for dni, nombre_completo in empleados2024.items():
    print(f"{dni}: {nombre_completo}")


aux = list(empleados2024.items())#-Pasamos los elementos del diccionario a una lista de tuplas

flag = ""#-Variable de corte
while flag != "n":
    new_empl = input("Ingrese nombre y apellido del nuevo empleado: ")#-Ingreamos nombre de nuevo empleado
    new_dni = int(input("DNI: "))#-Ingreamos dni de nuevo empleado
    for dni in empleados2024:
        if dni == new_dni:
            print("DNI ya existente")
            break#-Comparamos el DNI ingresado con los almacenados en el diccionario, si coinciden se termina el bucle
        else:#-Si no, se almacena en la lista como tupla el dni y el nombre del nuevo empleado en la lista
            aux.append((new_dni, new_empl))
    flag = input("Desea agregar otro empleado? (y/n): ")#-Preguntamos al usuario si desea seguir cargando nuevo personal
    
ordenamiento(aux)#-Ordenamos la lista de tuplas de menor a mayor por DNI


buscar = input("Deseas saber si un empleadoe n especifico se encuentra en la lista? (y/n): ")#-Le consultamos al usuario si desea buscar algun empleado en la lista
while buscar == "y":
    a_buscar = int(input("DNI a buscar: "))
    if busqueda_binaria_tuplas(aux, a_buscar) != -1:
        print(f"El DNI {a_buscar} se encuentra en la lista")
    else:
        print("No se encontro un empleado con ese DNI")
    #-Basicamente estamos buscando en la lista ordenada si existe el empleado ingresado por DNI
    buscar = input("Deseas saber si un empleado en especifico se encuentra en la lista? (y/n): ")

empleados2025 = dict(aux)
#-Transformamos la lista de tuplas ordenada con nuevos empleados a un nuevo diccionario
#-y la mostramos con los datos ordenados y actualizados
for dni, nombre_completo in empleados2025.items():
    print(f"{dni}: {nombre_completo}")

#Creamos un nuevo archivo txt llamado Empleados 2025.txt, donde el 2do parametro en este caso
#-es 'w', que escribe el archivo en vez de leerlo
with open('Empleados 2025.txt', 'w', encoding='utf-8') as archivo:
    for dni, nombre in empleados2025.items():
        archivo.write(f"{dni} {nombre}\n")