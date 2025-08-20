#Crea dos listas: una con nombres de 5 frutas y otra con 5 numeros. Concatenar ambas listas para posteriormente
#imprimir la lista de frutas y numeros. Acceder y mostrar el tercer elemento de la lista frutas y el cuarto de la lista numeros.
#Imprime el tercer elemento de la lista, que en este caso será la fruta en el índice 2.
frutas = ['manzana', 'banana', 'naranja', 'frutilla', 'anana']
numeros = [32, 44, 88, 22, 16]
lista = frutas + numeros #variable que almacena las dos listas anteriores.
print(lista)
print(frutas, numeros)
print(frutas[2], numeros[3]) #se muestran determinados elementos de las listas frutas y numeros
print(lista[2]) #se muestra determinado elemento en base a su posicion en la lista

#Crear un programa que agregue cuatro nombres de futas a una lista y luego borre dos. Se debe mostrar la lista actualizada
#despues de cada operacion.
import random
def pruebaListas():
    frutas = []#lista que almacenara las frutas
    while len(frutas) < 4:#el bucle se repetira hasta que la lista tenga cuatro elementos
        add = str(input('Ingrese el nombre de una fruta: '))
        frutas.append(add)#se agrega un elemento a la lista
        print(frutas)
    borrar = random.choice(frutas)#se escoge un elemento al azar de la lista
    frutas.remove(borrar)#se borra el elemento de la lista
    print(frutas)
    borrar2 = random.choice(frutas)
    frutas.remove(borrar2)
    print(frutas)
    return 'Fin' 
print(pruebaListas())

#Dada una lista de nombres de ciudades, buscar la ciudad "Maldonado" en la lista usando .index(). Luego mostrar su posicion en
#la lista si esta presente, en caso de no estarlo, mostrar un mensaje de error.
ciudades = ["Montevideo", "Salto", "Paysandú", "Maldonado", "Colonia", "Rivera"]
def posicionCiudad(ciudades):
    ciudad = str.capitalize(input('Escriba el nombre de una ciudad para ver su posicion en la lista: '))
    if ciudad in ciudades:
        return (f'La ciudad ingresada se encuentra en la posicion {ciudades.index(ciudad)}')
    else:
        return (f'La ciudad {ciudad} no esta en la lista.')
print(posicionCiudad(ciudades))
print(ciudades.index('Maldonado'))#obtener la posicion (indice) del elemento en la lista

#Dada una lista de colores, crear una funcion que compruebe si los colores "azul" y "morado" estan en la lista y devuelva un
#mensaje indicando si estan o no.
colores = ["rojo", "azul", "verde", "amarillo", "naranja"]
def estanColores(colores):
    return 'azul' and 'morado' in colores
if estanColores(colores):
    print('Ambos colores estan en la lista.')
else:
    print('Uno o dos de los colores no estan en la lista.')

#Dada la siguiente lista de paises, muestra un mensaje dependiendo de si el pais Chile esta o no en la lista.
paises = ['Argentina', 'Brasil', 'Chile', 'Perú']
if 'Chile' in paises:
    print('Chile esta en la lista paises.')
else:
    print('Chile no esta en la lista paises.')

#¿Cual es el valor de x despues de iniciar el codigo?
fruit = 'banana'
x = fruit[1]
print(x)
#En Python, se puede trabajar con los strings como si fuesen listas. Cada letra corresponde a un elemento de la lista,
#por lo tanto, podemos acceder a una letra pos su valor posicional.

tipos_datos = [32, 4.8, 'variados', True]#una lista puede contener diferentes tipos de datos.

strings = ["pochoclo", "legumbres", "sal", "carnes", "mariscos"]
print(strings[2])#devuelve el elemento en la posicion 2.
strings[1] = "verduras" #sustituye un elemento por otro en la posicion indicada.
strings.append("legumbres") #con append agregamos un valor a la lista.
strings.insert(3, "frutas") #con insert se agrega un elemento en la posicion indicada.
strings.remove("pochoclo") #remove elimina la primera aparicion del elemento indicado, NO todas las veces que aparece.
print(len(strings)) #devuelve la cantidad de elementos que tiene la lista.
elemento = strings.pop(0)#con .pop se elimina un elemento de una lista en base a su indice.
print(elemento)#en la variable queda almacenado el elemento eliminado.
strings.reverse()#se invierte el orden de los elementos en la lista
print(strings)
print("pochoclo" in strings) #devuelve un booleano indicando si el elemento aparece o no en la lista.
print("sal" in strings)

print(strings[1:3]) #muestra todos los elementos comprendidos en el rango de posiciones indicados.
print(strings[2:]) #muestra todos los elemntos desde la posicion inicial indicada en adelante.

#listas y strings
listaNum = [10, 20, 30, 40, 50, 60, 70, 80, 90]
string = 'El elefante se balanceaba'

print(listaNum[3: 10: 2]) #el primer numero corresponde al inicial, el segundo al final y el tercero al tipo de conteo.
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
numero = [5, 7, 10] * 4 #esta lista pasar a tener los valores 5, 7, 10 repetidos 4 veces.

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
decimales.append(2.7)
decimales.append(5.4)
print(decimales)
x = decimales.count(5.4)#count permite contar la cantidad de veces que aparece un elemento en una lista.
print(x)
print(len(decimales))#con len se cuenta la cantidad de elementos dentro de la lista.
decimales.remove(6.9)
print(decimales)
i = decimales.index(9.6)
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
print(mi_frase.replace('2', '8')) #recibe un fragmento del string y lo reemplaza por el indicado. El primer fragmento es el 
#recibido y el segundo es el introducido.
print(mi_frase.split()) #la funcion split devuelve una lista, donde cada elemento de la lista es una palabra.
cantidad = mi_frase.split()
print(len(cantidad)) #primero transformo la frase en una lista y despues cuento los elementos.

#Listas dentro de listas
enteros = [2, 4, 5, 7, 10, 22, 20]
decimales = [2.4, 5.7, 44.6, 23.1, 5.1]
animales = ['Tigre', 'Leon', 'Pantera', 'Dragon de komodo', 'Anaconda', 'Elefante']
variada = [2, 5.7, 'Tigre', 20, 44.6, 'Anaconda'] #las lisas pueden albergar ambos tipos de datos

#se pueden usar listas como elementos de una lista
lista_de_listas = [enteros, decimales, animales, variada]
print(lista_de_listas[1][2])#asi se obtiene el decimal 44.6, donde 1 y 2 son coordenadas que permiten llegar a un 
#elemento puntual de una lista.

#Utiliza un for para mostrar solamente los elementos de la tercera lista de la variable lista de listas.
def obtener_lista(lista_de_listas):
    for i in lista_de_listas[2]:
        print(i)
    return ''#si se crea una funcion y no se especifica un retorno, el programa devolvera 'none'. Se le puede especificar
              #algo al return de forma simbolica para evitar esto.
print(obtener_lista(lista_de_listas))

#Crear una lista de listas en una sola linea
listas = [[0, 1, 2, 3, 4], [10, 11, 12, 13, 14], [20, 21, 22, 23, 24]]
#utiliza un for para mostrar los elementos de la variable listas, es decir, las listas y sus elementos.
for i in listas:
    print(i)
#utiliza dos for, uno adentro de otro para mostrar uno a uno los elementos de la listas.
for i in listas:#primero se itera en cada lista
    for j in i:#se itera en cada elemento de cada lista
        print(j)

#Arrays: son estructuras de datos similares a las listas, utilizadas en otros lenguajes de programacion. Aunque comparten
#algunas similitudes con las listas, los arrays suelen tener una longitud fija y contener elementos del mismo tipo de datos.

#Matrices: son estructuras de datos bidimensionales que se utilizan para representar datos en formas de tablas o cuadriculas.
#Cada elemento de una matriz tiene dos indices para indicar su posicion en la filas y columnas y tambien son conocidas como
#arrays bidimensionales.

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

#Crear una funcion que reciba una lista de palabras y devuelva una lista con el largo de cada palabra de la lista original.
#Usando mapeo de listas.
palabras = ['mastodonte', 'mamut', 'ardilla', 'kazuario']
def numero_letras(palabras):
    salida = []
    for i in palabras:
        salida.append(len(i))
    return salida
print(numero_letras(palabras))

#Usando listas por comprension.
def numero_letras2(palabras):
    return [len(i) for i in palabras]#la transformacion de la variable de iteracion seguida del bucle for. Se itera dentro de la
print(numero_letras2(palabras))#lista, por lo que no hace falta usar append.

#Dada una lista de nombres en mayúsculas, crea un programa que use map() para convertir todos los nombres a minúsculas.
nombresM = ['JULIO', 'KARIM', 'EUSEBIO', 'KARINA', 'BEATRIZ']
#Forma 1
def nombresMinusculas(nombres):
    x = []
    for i in nombres:
        x.append(str.lower(i))
    return x
print(nombresMinusculas(nombresM))
#Forma 2
#la funcion map() ejecuta una funcion para la variable introducida. La variable pasa a ser parametro de la funcion.
nombres_minuscula = list(map(str.lower, nombresM))
print(nombres_minuscula)
#Forma 3
def minusculas(nombres):
    return [str.lower(i) for i in nombres]
print(minusculas(nombresM))

#¿Que es el mapeo en programacion?
#Transformar una coleccion de datos aplicando una funcion a cada elemento.
#El mapeo en programacion se refiere a la operacion de aplicar una funcion a cada elemento de una coleccion de datos, 
#generando asi una nueva coleccion con los reultados de aplicar la funcion a cada elemento individualmente.
#Para construir una lista por comprensión en Python, necesitas una expresión que determine cómo se transformarán los elementos 
#de una secuencia y un bucle "for" que itere sobre los elementos de esa secuencia. La lista por comprensión toma cada elemento 
#de la secuencia, aplica la expresión y genera una nueva lista con los resultados.

nums = [6, 12, 18, 24, 30]
numeros_dobles = [num * 2 for num in nums]
print(numeros_dobles)
#Esta lista por comprensión toma cada elemento num de la secuencia nums, multiplica cada elemento por 2 (num * 2) y crea 
#una nueva lista con los resultados que se almacena en numeros_dobles.

#Dada una lista de numeros, devolver la suma de los numeros pares
lista_numeros = [1, 4, 7, 10, 15, 20, 25, 30]
def pares(lista):
    return sum([i for i in lista if i % 2 == 0])
print(pares(lista_numeros))

#Dada una lista de palabras, crea un programa que filtre las palabras que tienen 4 letras o menos y las devuelva en una lista.
#Utiliza el metodo filter().
#Forma 1
palabras = ['cerro', 'pantano', 'sol', 'luz', 'mar', 'montaña', 'cielo', 'bosque', 'lago']
def palabrasCortas(lista):
    return [p for p in lista if len(p) <= 4]
print(palabrasCortas(palabras))

#Forma 2
palabras_cortas = list(filter(lambda palabra: len(palabra) <= 4, palabras))
print(palabras_cortas)
#la palabra reservada lambda permite crear funciones anonimas, para ello se le debe asignar un parametro y la condicion (en este 
#caso). Asi cumplimos con el primer argumento del metodo filter(); el segundo sera la lista sobre la que se realizara el filtrado.

#¿Como se relaciona el filtrado con el mapeo en programacion?
#El filtrado es una forma especifica de mapeo. El filtrado es una forma especifica de mapeo en la que solo se seleccionan ciertos
#elementos en lugar de transformar todos los elementos de una coleccion. Por lo tanto, el filtrado es un caso particular de mapeo.

#¿Cual es el proposito del filtrado en programacion?
#Seleccionar elementos de una coleccion que cumplan ciertos criterios. El filtrado permite extraer y retener unicamente los 
#elementos que cumplen con los criterios definidos, lo que facilita el procesamiento y analisis de datos al eliminar elementos no
#deseados o no relevantes.

#Generar una lista de estudiantes que aprobaron ambas asignaturas. Filtrado.
#Calcular el promedio de calificaciones para cada estudiante. Mapeo.
#Crear una lista de estudiantes con sus nombres y promedio de calificaciones. Mapeo.
