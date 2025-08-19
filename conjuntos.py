#Un set es una estructura de datos que NO puede tener elementos repetidos y ademas tiene las propiedades matematicas de los
#conjuntos.
conjunto = {1, 2, 3}
print(conjunto)
#La funcion set() permite crear un conjunto vacio o convertir otro tipo de variable en un conjunto como por ejemplo una
#lista.
lista = set([2, 4, 6, 8, 10])
print(lista)

conjunto3 = {1, 1, 1, 1, 1, 2, 2}
print(conjunto3)#un conjunto no puede tener elementos repetidos. En el caso de que existan elementos repetidos, solo se tomara
#uno.

conjunto4 = {1, 'a', 'b', 'a', 1, 1, 2}
print(conjunto4)#un conjunto puede tener elementos de tipo string y tipo numerico.

#Funciones para modificar un conjunto
s1 = {1, 2, 3}
s1.add(4)#agregar un elemento
print(s1)

s2 = {2, 4, 6, 8}
s2.update([10, 12, 14])#agregar varios elementos.
print(s2)

s3 = {5, 10, 15, 20, 25, 27}
s3.remove(27)#Eliminar un elemento del set. Si el elemento no se encuentra en el set, devuelve error.
print(s3)

s4 = {10, 20, 30, 40, 50}
s4.discard(5)#A diferencia de remove, si el elemento a eliminar no esta en el set, no devuelve error.
print(s4)

s5 = {3, 6, 9, 12, 15}
s5.clear()#Funcion para vaciar un conjunto.
print(s5)

s6 = {4, 8, 12, 16, 20, 24}
print(len(s6))#Funcion len para contar los elementos de un conjunto.
s7 = {1,"a","b","a",1,1,2}
print(len(s7))#Si el set tiene elementos repetidos, entonces se contara una vez cada elemento diferente.

#Crea una funcion que reciba una lista y devuelva un set que contenga los valores que aparecen en la lista.
#Utilizar la funcion set() para crear un nuevo set y la funcion add() para agregar elementos a dicho set.
lista = [2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 10, 10]
def valores_no_repetidos(lista):
    return set(lista)
print(valores_no_repetidos(lista))
#solucion 2
def valores_no_repetidos2(lista):
    nuevo_set = set()
    for i in lista:
        nuevo_set.add(i)
    return nuevo_set
print(valores_no_repetidos2(lista))

#Operaciones de conjuntos
#Union: el resultado es un nuevo set con los elementos de los dos set anteriores.
set_1 = {1, 2, 3, 4, 5}
set_2 = {6, 7, 8, 9, 10}
print(set_1.union(set_2))
print(set_1 | set_2)

#Interseccion: el resultado es un set que contenga los elementos que se encuentren en ambos conjuntos.
set_3 = {2, 4, 6, 8}
set_4 = {1, 3, 6, 9}
print(set_3.intersection(set_4))
print(set_3 & set_4)

#Diferencia: el resultado son los elementos del conjunto 1 menos los elementos del conjunto 2.
set_5 = {1, 2, 3, 4}
set_6 = {3, 4, 5, 6}
print(set_5.difference(set_6))
print(set_5 - set_6)

#Diferencia simetrica: el resultado son los elementos que no se encuentren en ambos.
set_7 = {10, 20, 30, 40, 50}
set_8 = {5, 10, 15, 20, 25}
print(set_7.symmetric_difference(set_8))
print(set_7 ^ set_8)

#Sub conunto: verdadero si el conjunto1 es subconjunto del conjunto2.
set_9 = {1, 4, 7}
set_10 = {1, 4, 7, 10, 13}
print(set_9.issubset(set_10))
print(set_10.issubset(set_9))

#Super set: verdadero si el conjunto2 es subconjunto del conjunto1.
set_11 = {2, 4, 6, 8, 10}
set_12 = {4, 6, 8}
print(set_11.issuperset(set_12))
print(set_12.issuperset(set_11))

#Crea una funcion que reciba dos parametros de tipo set y devuelva un set que contenga los elementos del primer set mas 
#los del segundo.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
def union_de_sets(set1, set2):
    return set1.union(set2)
print(union_de_sets(set1, set2))

#Crea una funcion que reciba dos parametros de tipo set y devuelva un set que contenga la interseccion de ambos sets, 
#es decir, solamente los elementos que se encuentren en ambos sets.
setx = {4, 8, 12, 16}
sety = {12, 16, 20, 24}
def interseccion_de_set(setx, sety):
    return setx.intersection(sety)
print(interseccion_de_set(setx, sety))

#Ejercicio Uso de Sets: Dado un conjunto de números, elimina los repetidos y muestra el resultado.
numeros = [1, 2, 2, 3, 4, 4, 5, 5, 6]
print(set(numeros))

#Los sets no admiten elementos duplicados, sus elementos están desordenados, no pueden ser mutables y utilizan tablas hash para hacer 
#más eficiente la búsqueda.

#Forma correcta de crear un set vacio en Python:
set_de_ejemplo = set() #la funcion set permite crear un set vacio. Si se utiliza {}, se creara un diccionario vacio.
