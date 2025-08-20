#Numeros aleatorios
#A continuacion se trabajara en la creacion de numeros aleatorios utilizando la libreria random en Python.
#Una libreria es un conjunto de funciones y clases que otra persona o personas han escrito y que estan disponibles para su 
#uso. Para utilizar una libreria se debe usar la palabra reservada import y el nombre de la libreria.
import random
#Escribi un programa que genere un numero random
print(f'numero random: {random.randint(1, 100)}')
print(random.randrange(0, 11))#genera un numero entero entre un numero inicial y final (este ultimo no incluido)

#Utilizar un for para generar una secuencia de diez numeros comprendidos entre 1 y 5.
for i in range(10):
    r = random.randrange(1, 6)
    print(r)

#Los numeros aleatorios generados por las computadoras no son totalmente aleatorios, sino que son pseudoaleatorios.
#Esto significa que dado un numero inicial llamado semilla (seed), un generador de numeros pseudoaleatorios genera siempre
#la misma secuencia de numeros pero cada numero generado tiene la misma posibilidad de salir que cualquiera de los otros.
#Si se cambia la semilla, se generara una nueva secuencia de numeros aleatorios.
random.seed(0)
for i in range(42):
    h = random.randrange(1, 6)
    print(h)

#Con la funcion randrange se pueden simular procesos aleatorios. Por ejemplo, se puede simular tirar una moneda mil veces
#y contar la cantidad de veces que sale de un lado y del otro para luego calcular su probabilidad.
intentos, contador_cara, contador_numero = 1000, 0, 0
for intento in range(intentos):
    moneda = random.randrange(0, 2)
    if moneda == 0:
        contador_cara += 1
    else:
        contador_numero += 1
print(f'Cantidad de veces que salio cara: {contador_cara}')
print(f'Probabilidad de que saliera cara: {contador_cara/intentos * 100}')
print(f'Cantidad de veces que salio numero: {contador_numero}')
print(f'Probabilidad de que saliera numero: {contador_numero/intentos * 100}')

import random
#Ejercicio: simula tirar mil veces dos dados. Calcula la probabilidad de obtener 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 y 12
#con la suma de ambos.
intentos = 1000
contador_suma_dados = [0]*13 #se determina la cantidad de elementos que tendra la lista. 
for i in range(intentos):
    dado_1 = random.randrange(1, 7)
    dado_2 = random.randrange(1, 7)
    suma = dado_1 + dado_2 #la variable suma almacenara la suma de lo obtenido por los dados
    contador_suma_dados[suma] += 1#se almacena en una lista la cantidad de veces que se obtuvo cada suma posible entre dos
    #dados. Es decir, la posicion 2 en la lista representa la cantidad de veces que los dados sumaron 2, mientras que
    #en la posicion 12 se almacena la cantidad de veces que los dos dados sumaron 12.
for i in range(2, 13):#todos los valores que se pueden obtener de la suma de dos dados
    print(f'La probabilidad de que la suma de los dos dados sea {i} es {contador_suma_dados[i]/intentos * 100}')
#Por ultimo, se muestra la probabilidad de que se obtenga cada suma posible entre la suma de lo obtenido por los dos
#dados.

#Ejercicio: simula tirar una moneda cien veces y calcula la probabilidad de que salgan cinco veces seguidas la misma cara.
intentos = 100
contador_cara_5veces = 0 #la cantidad de veces que la misma cara saldra cinco veces seguidas
for i in range(intentos):
    tirada1 = random.randrange(0, 2)
    tirada2 = random.randrange(0, 2)
    tirada3 = random.randrange(0, 2)
    tirada4 = random.randrange(0, 2)
    tirada5 = random.randrange(0, 2)
    if tirada1 == 1 and tirada2 == 1 and tirada3 == 1 and tirada4 == 1 and tirada5 == 1:
        contador_cara_5veces += 1
print(f'Cantidad de veces que salio la misma cara cinco veces seguidas: {contador_cara_5veces}')
print(f'La probabilidad de que la misma cara salga cinco veces seguidas es: {contador_cara_5veces/intentos * 100}')

#Otras funciones de la libreria random
#random.choice(lista), elige aleatoriamente un numero de la lista
lista01 = [2, 4, 6, 8, 10]
print(random.choice(lista01))
print(random.choice(lista01))

#random.choice(lista, k), elije aleatoriamente k elementos de una lista
print(random.choices(lista01, k=3))
print(random.choices(lista01, k=2))

#random.sample(lista, k), elije aleatoriamente k elementos distintos de una lista, por lo que k debe ser igual o menor al 
#tamaño de la lista.
print(random.sample(lista01, k=3))

#random.shuffle(lista), mezcla los elementos de una lista
lista_03 = [3, 6, 9, 12, 15, 18, 21]
random.shuffle(lista_03)
print(lista_03)

#random.random(), genera un numero decimal aleatorio entre 0 y 1
print(random.random())

#random.uniform(inicio, fin), genera un decimal aleatorio entre los numeros comprendidos, el ultimo incluido
print(random.uniform(2, 8))

#Ejercicio: crear una funcion seleccionar_aleatoriamente(lista, n) que reciba una lista y un numero n, para devolver
#una lista con n elementos seleccionados aleatoriamente de la lista. Los elementos seleccionados pueden ser repetidos.
lista, n = [3, 6, 9, 12, 15, 18, 21], 3
def seleccionar_aleatoriamente(lista, n):
    return random.choices(lista, k=n)
repetidos = seleccionar_aleatoriamente(lista, n)
print(f'La lista con numeros aleatorios repetidos es: {repetidos}')
#Solucion 2
def seleccion_aleatoria(lista, n):
    numeros = []
    for i in range(n):#i va a iterar la cantidad de veces dispuesta por el parametro n
        i = random.randrange(0, len(lista))#i recibe un valor posicional
        numeros.append(lista[i])#i toma un elemento dentro de la lista en base a su posicion y lo agrega a la lista
    return numeros
print(f'La lista con numeros aleatorios que pueden ser repetidos es: {seleccion_aleatoria(lista, n)}')

#Ejercicio: crear una funcion que sea muy similar a la anterior, con la diferencia que esta vez los valores generados 
#para la lista no pueden repetirse.
lista2 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
n = int(input('Ingrese la cantidad de numeros para seleccionar aleatoriamente: '))
def seleccionarAleatoriamente2(lista2, n):
    while n > len(lista2):
        print('La cantidad ingresada no puede ser superior a la cantidad de elementos de la lista.')
        n = int(input('Ingrese la cantidad de numeros para seleccionar aleatoriamente: '))
    salida = random.sample(lista2, k=n)
    return salida
print(seleccionarAleatoriamente2(lista2, n))

#Ejercicio: crear una funcion llamada contar_veces(semilla) que reciba un parametro entero llamado semilla y que genere
#numeros aleatorios entre 0 y 99 utilizando random.randrange(0, 100). Previamente ejecutar random.seed(int). La funcion 
#debera devolver el numero de intentos generados hasta generar el numero 42. 
#input: semilla 1 output: 68
def contar_veces(seed):
    random.seed(seed)
    r = random.randrange(0, 100)#se genera un numero aleatorio entre 0 y 99
    contador = 1#se sumara de a 1 por cada intento de generar el 42
    while r != 42:#mientras el numero aleatorio sea diferente del numero que quiero generar, 42
        r = random.randrange(0, 100)#vuelvo a generar un numero aleatorio
        contador += 1#a contador le sumo 1
    return contador
print(contar_veces(1))
