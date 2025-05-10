#las tuplas son parecidas a las listas, con la diferencia de que no son modificables.
#index: indice, devuelve la posición en la que se encuentra un elemento dentro de la tupla
tupla_ejemplo = (2, 5, 7, 4, 2, 6, 2)
print(tupla_ejemplo.count(2)) #devuelve la cantidad de veces que aparece un elemento
print(tupla_ejemplo.index(7)) #devuelve la posicion en la que se encuentra un elemento

lista = [9, 3, 6, 7, 2, 8, 7]
def min_max(lista):
    minimo, maximo = min(lista), max(lista)
    return (minimo, maximo)
print(min_max(lista))

x = min_max([9, 3, 6, 7, 2, 8, 7])
print(x)
print(x[0]) #devuelve el elemento de menor valor dentro de una tupla
print(x[1]) #devuelve el elemento de mayor valor dentro de una tupla

tupla = (100, 200)
elemento, elemento2 = tupla #se le asigna a las dos variables los elementos de la tupla como valor
print(elemento)
print(elemento2)

minimo, maximo = min_max(lista)
print(minimo)
print(maximo)

lista = [10, 20, 30, 40, 50]
tuplaDiez = tuple(lista) #a partir de una lista, se crea una tupla
print(tuplaDiez)

tupla = (11, 22, 33, 44, 55)
listaN = list(tupla) #a partir de una tupla, se crea una lista
print(listaN)

#La funcion zip() recibe dos listas y genera una lista de tuplas con los valores que se encuentran en la misma posicion
nombres = ['Carlos', 'Santiago', 'Julian']
edades = [31, 24, 41]
#print(list(zip(nombres, edades)))
def generarListaTuplas(nombres, edades):
    return list(zip(nombres, edades))
print(generarListaTuplas(nombres, edades))

#Tambien se pueden generar tuplas separadas con los elementos que se encuentren en la misma posicion
def generarTuplas(nombres, edades):
    for t in zip(nombres, edades):
        print(t) 
    return ' '
print(generarTuplas(nombres, edades))
