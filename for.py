#La estructura for (durante o dado que) es parecida a while, con la diferencia de que se le puede asignar un rango para determinar la 
#cantidad de veces que se quiera iterar. Las variables utilizadas en for incrementaran en uno su valor por cada iteracion. 
#Iterar significa hacer algo muchas veces.
for x in range(2, 21, 2):#muestro en pantalla los números que sólo sean pares.
    print(x)
for i in range(3, 31, 3):#muestro en pantalla los múltiplos de 3.
    print(i)
for y in range(11, 0, -1):#muestro en pantalla la cuenta de números pero hacia atrás.
    print(y)
for c in range(20, 0, -2):#muestro en pantalla la cuenta de números hacia atrás de a dos.
    print(c)
for d in range(15, -16, -3):#muestro en pantalla la cuenta de números hacia atrás de a tres con negativos.
    print(d)

#Mostrar los elementos contenidos en una lista
colores = ["azul", "rojo", "verde", "amarillo", "violeta"]
for x in colores:#x es la variable de iteracion.
    print(x)

animales = ["Elefante", "Oso", "Leon", "Tigre", "Pantera", "Hiena", "Rinoceronte"]
for a in animales:
    print(a)

for x in range(11):#se determina un rango de valores que se mostrara en pantalla.
    print(x)
for x in range(2, 9):#rango de valores separados por coma.
    print(x)
for i in range(1, 6):#se cuenta hasta uno menos que el rango especificado.
    print (i)

#Crear una lista y, a cada elemento, sumarle uno. Mostrar en pantalla la nueva lista.
lista = [10, 20, 30, 40, 50]
for i in range(len(lista)):
    lista[i] += 1
print(lista)

#Crea un programa que muestre todos los colores de la LISTA COLORES que NO esten en la LISTA PRIMARIOS.
primarios = ["azul", "amarillo", "rojo"]
colores = ["blanco", "azul", "blanchedalmond", "violeta", "rojo", "naranja", "verde", "amarillo"]
def seleccion(primarios, colores):
    colores_secundarios = [c for c in colores if c not in primarios]#se declara la variable de iteracion seguido de la
    return colores_secundarios                                      #estructura for y la condicion.
#Forma numero dos
for c in colores:#la variable de iteracion almacena el valor de los elementos de la lista colores
    if c not in primarios:#la condicion
        print(c)

#Usando for con una lista de indices para acceder a elementos de otra lista.
lista = [10, 20, 30, 40, 50]
for p in [0, 1, 2]:
    lista[p] += 500 #se le suma 500 a los primeros tres elementos de la lista
print(lista)

#multiplicar todos los elementos de una lista
lista = [1, 2, 3, 4, 5]
def multiplicar(lista):
    multiplicacion = 1 #variable multiplicacion inicializada en 1
    for i in lista:
        multiplicacion *= i #establecemos que se va a multiplicar por cada elemento de la lista.
    return multiplicacion
print(multiplicar(lista))

import math
#Crear un codigo que calcule la suma de Gauss de un numero introducido por el usuario. La suma de Gauss es la suma de todos los
#numeros comprendidos entre el 1 y el numero indicado. Ejemplo: suma de Gauss de 100 es 5050.
numero = int(input('Escriba un numero entero para calcular su suma de Gauss: '))
def suma_Gauss(numero):
    suma = 0#variable que almacenara la suma de Gauss
    for i in range(1, numero + 1, 1):#el rango sera entre uno y un numero mas al especificado
        suma += i#a la variable se le suma el valor de la variable de iteracion, que se incrementa en uno dentro del rango.
    return suma
print(suma_Gauss(numero))
#Forma abreviada
def sumaGauss(numero):
    return (numero) * (numero + 1) / 2
print(sumaGauss(numero))

#Crear un codigo que obtenga los numeros de la sucesion de Fibonacci. Los numeros deben ser exportados a una lista y la cantidad de
#numeros a obtener debe ser especificada por el usuario.Ejemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
x = int(input('Ingrese la cantidad de numeros de la sucesion de Fibonacci que quiere obtener: '))
def fibonacci(x):
    sec_fibonacci = []
    for i in range(x):#el rango de numeros es el especificado por el usuario
        if i == 0:
            sec_fibonacci.append(0)
        elif i == 1:
            sec_fibonacci.append(1)
        else:
            #se crea la variable siguiente, que almacena la suma de los dos valores anteriores
            siguiente = sec_fibonacci[i - 1] + sec_fibonacci[i - 2]
            sec_fibonacci.append(siguiente)#se agrega el valor a la lista
    return sec_fibonacci
print(fibonacci(x))

#Crear un codigo que calcule el factorial de un numero brindado por el usuario sin utilizar la funcion predefinida de Python. El 
#factorial de un numero es el resultado (producto) de multiplicar todos los valores desde uno hasta determinado numero. Ejemplo: 
#factorial de 4 es 24.
numero = int(input('Ingrese un numero para calcular su factorial: '))
def factorial(numero):
    factorial = 1#se incializa la variable que almacenara el resultado en uno
    for i in range(numero):#el rango es el numero especificado por el usuario, determina la cantidad de veces que se va a multiplicar.
        factorial *= i + 1#el valor de i se incrementa en uno y se multiplica por el valor de la variable
    return factorial
print(factorial(numero))

#Utilizar la funcion factorial de la libreria math para verificar lo anterior.
numero_2 = int(input('Ingrese un numero para calcular su factorial: '))
def factorial2(numero):
    return math.factorial(numero)
print(factorial2(numero_2))
