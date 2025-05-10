strings = ["pochoclo", "legumbres", "sal", "carnes", "mariscos"]
print(strings[2])#devuelve el elemento en la posicion 2.

strings[1] = "verduras" #sustituye un elemento por otro en la posicion indicada.

strings.append("legumbres") #con append agregamos un valor a la lista.

strings.insert(3, "frutas") #con insert se agrega un elemento en la posicion indicada.

strings.remove("pochoclo") #remove elimina la primera aparicion del elemento indicado, NO todas las veces que aparece.
print(len(strings)) #devuelve la cantidad de elementos que tiene la lista.

print("pochoclo" in strings) #devuelve un booleano indicando si el elemento aparece o no en la lista.
print("sal" in strings)

print(strings[1:3]) #muestra todos los elementos comprendidos en el rango de posiciones indicados.
print(strings[2:]) #muestra todos los elemntos desde la posicion inicial indicada en adelante.

#listas y strings
listaNum = [10, 20, 30, 40, 50, 60, 70, 80, 90]
string = 'El elefante se balanceaba'

print(listaNum[3: 10: 2]) # el primer numero corresponde al inicial, el segundo al final y el tercero al tipo de conteo.
print(listaNum[2])
print(listaNum[-3])
print(string[3])
print(string[-2])
print(listaNum[0:3])
print(listaNum[-2: ])
print(string[3:11])
print(string[-10: ])

#si en el tercer termino se utiliza un numero negativo, se realiza un decremento, por lo que el valor inicial debe ser
#mayor que el final. 
print(listaNum[ : : -1])
print(listaNum[4: : -1])
#mostrar los valores impares de mi lista y despues mostrar los ultimos cinco valores invertidos.
print(listaNum[0: : 2])
print(listaNum[: -6: -1])

#mostrar las letras en las posiciones pares del string y luego mostrar el string invertido.
print(string[2: :2])
print(string[ : : -1])

#se puede crear una nueva lista a partir de la original, sin modificarla.
materias = ['matematica', 'biologia', 'filosofia', 'geografia', 'historia', 'ingles', 'dibujo']
materias2 = materias[3:]

#al multiplicar una lista por un entero, se repetiran los valores de la lista por la cantidad de veces especificada.
numero = [5, 7, 10] * 4 # esta lista pasar a tener los valores 5, 7, 10 repetidos 4 veces.

#crea una variable x que contenga una lista con 20 ceros.
x = [0] * 20
print(x)

#con los strings sucede algo similar
animales = ['leon', 'tigre', 'pantera', 'leopardo'] * 3
print(animales)

#La funcion list() permite crear listas a partir de conjuntos, tuplas, etc.
#Ejemplo de como transformar un set a lista.
set_ejemplo = {2, 3, 4, 5, 6}
print(set_ejemplo)
lista_set = list(set_ejemplo)
print(lista_set) 
#La funcion range permite crear listas con numeros enteros.
#Como el resultado de la funcion range no es una lista, se utiliza la funcion list.
(list(range(10))) #Asi se genera una lista con numeros enteros.
(list(range(21)))

#La funcion range permite tambien establecer precisamente un rango de numeros, donde debemos indicar su inicio y fin.
#print(list(range(12, 23)))
#Tambien se puede especificar un tercer parametro, que sera el encargado de sumar o restar entre ese rango de numeros.
(list(range(10, 41, 2))) # Desde el 10 al 40 de a dos
(list(range(100, 1001, 150))) # Desde el 100 al 1000 contando de a 150
(list(range(150, 50, -10))) # Cuenta regresiva desde 150 hasta 50 contando de a -10.
(list(range(10, -1, -1))) # Cuenta regresiva desde 10 a 0.

#Crea una funcion sumar_pares_hasta_impar(numeros) que sume los elementos de la lista que son pares hasta que
#aparezca un numero impar y devuelva dicha suma.
numeros = [2, 8, 4, 10, 20, 14, 5, 6, 12]
def sumar_pares_hasta_impar(numeros):
    suma_de_pares = 0
    for i in numeros:
        if i % 2 == 0:
            suma_de_pares = suma_de_pares + i
        else:
            break # el break se puede usar, pero es mala practica(?).
    return suma_de_pares
#print(sumar_pares_hasta_impar(numeros))

decimales = [8.4, 5.4, 7.3, 9.6, 3.1, 6.9]
print(decimales)
decimales.append(2.7) # append es la funcion que permite agregar valores, en este caso para una lista.
decimales.append(5.4)
print(decimales)
x = decimales.count(5.4) # count permite contar la cantidad de veces que aparece un elemento en una lista. Se puede 
#almacenar dicho valor en una variable.
print(x)
print(len(decimales)) #con len se cuenta la cantidad de elementos dentro de la lista.
decimales.remove(6.9) #funcion remove permite eliminar un elemento de una lista.
print(decimales)
i = decimales.index(9.6) #con index obtenemos la posicion de un elemento dentro de una lista.
print(i)

decimales.sort() #esta funcion permite ordenar valores numericos almacenados en una lista.
print(decimales)
#Ordenar los elementos en base a su cantidad de elementos, orden descendente
cars = ['Ford', 'Mitsubishi', 'BMW', 'Volvo', 'Citroen']
def orden(e):
    return len(e)
cars.sort(reverse=True, key=orden)
print(cars)
#Ordena la lista por largo de los valores, orden ascendente
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)
cars = ['Ford', 'Mitsubishi', 'BMW', 'Volvo', 'Citroen']
cars.sort()
print(cars) #ordena los strings dentro de la lista alfabeticamente.

#Funciones para los strings
mi_frase = "2 ElEfaNtEs Se balAncEaban"
print(mi_frase.lower()) # devuelve la frase convertida en minuscula
print(mi_frase.upper()) # devuelve la frase convertida en mayuscula
print(mi_frase.replace('2', '8')) #replace recibe un fragmento del string y lo reemplaza por el indicado. El primer
#fragmento es el recibido y el segundo es el introducido.
print(mi_frase.split()) # la funcion split devuelve una lista, donde cada elemento de la lista es una palabra.
cantidad = mi_frase.split()
print(len(cantidad)) # primero transformo la frase en una lista y despues cuento los elementos.
# Listas dentro de listas
#lista de enteros
enteros = [2, 4, 5, 7, 10, 22, 20]
#lista de decimales
decimales = [2.4, 5.7, 44.6, 23.1, 5.1]
#Lista de strings
animales = ['Tigre', 'Leon', 'Pantera', 'Dragon de komodo', 'Anaconda', 'Elefante']
#las lisas pueden albergar ambos tipos de datos
variada = [2, 5.7, 'Tigre', 20, 44.6, 'Anaconda']

#se pueden usar listas como elementos de una lista
lista_de_listas = [enteros, decimales, animales, variada]
print(lista_de_listas[1][2])#asi se obtiene el decimal 44.6, donde 1 y 2 son coordenadas que permiten llegar a un 
#elemento puntual de una lista.

#Utiliza un for para mostrar solamente los elementos de la tercera lista de la variable lista de listas.
def obtener_lista(lista_de_listas):
    for i in lista_de_listas[2]:
        print(i)
    return ' '#si se crea una funcion y no se especifica un retorno, el programa devolvera 'none'. Se le puede especificar
              #algo al return de forma simbolica para evitar esto.
print(obtener_lista(lista_de_listas))

#Crear una lista de listas en una sola linea
listas = [[0, 1, 2, 3, 4], [10, 11, 12, 13, 14], [20, 21, 22, 23, 24]]
print(listas)
#utiliza un for para mostrar los elementos de la variable listas, es decir, las listas y sus elementos.
for i in listas:
    print(i)
#utiliza dos for, uno adentro de otro para mostrar uno a uno los elementos de la listas.
for i in listas:
    for j in i:
        print(j)

#Nota: cuando las listas solo contienen numeros, las podemos comparar con lo que en matematica se conoce como
#vectores y matrices.
#Una lista puede compararse con lo que en matematica se conoce como un vector.
#Una lista de listas puede ser comparada con lo que en matematica se conoce como una matriz.
#En las listas de listas podemos pensar que cada elemento esta en una posicion dada por dos numeros:
#un numero que nos dice la fila
#un numero que nos dice la columna
for l in listas:
    print(l)

numero_filas = len(listas)#la cantidad de filas sera la cantidad de listas anidadas
print(numero_filas)
numero_columnas = len(listas[0])#la cantidad de columnas sera la cantidad de elementos por lista
print(numero_columnas)
for i in range(numero_filas):
    for j in range(numero_columnas):
        print(f'El elemento de la fila {i} y columna {j} es: {listas[i][j]}')
#en la fila 0 se encontraran los valores de la primera lista en base a su posicion en la misma, que corresponda a la columna.
#en la fila 1 se encontraran los valores de la segunda lista en base a su posicion en la misma, que corresponde a la columna.
#en la fila 2 se encontraran los valores de la tercera lista en base a su posicion en la misma, que corresponde a la columna.

#utiliza dos for para mostrar uno a uno los elementos de listas en donde el numero de fila y el numero de columna
#es el mismo. (0, 11, 22)
for i in range(numero_filas):
    for j in range(numero_columnas):
        if i == j:
            print(f'Los elementos que comparten numero de fila y columna son: {listas[i][j]}')

#Crear una funcion que reciba una lista cuyos elementos son solamente los strings 'hombre' y 'mujer' y devuelva dos listas:
#una que contenga unos en las posiciones donde dice hombre y ceros donde dice mujer, y otra que contenga unos donde dice
#mujer y cero donde dice hombres.
individuos = ['hombre', 'hombre', 'mujer', 'mujer', 'hombre', 'mujer', 'mujer', 'mujer', 'hombre', 'hombre']

def obtenerDummies(individuos):
    hombre, mujer = [], [] #se crean las dos listas
    for i in individuos:
        if i == 'hombre': #si la variable de iteracion toma el string 'hombre'
            hombre.append(1) #agrega unos a la lista hombre
            mujer.append(0) #agrega ceros a la lista mujer
        else: #de lo contrario
            hombre.append(0) #agrega ceros a la lista hombre
            mujer.append(1) #agrega unos a la lista mujer
    return hombre, mujer
    
print(obtenerDummies(individuos))
