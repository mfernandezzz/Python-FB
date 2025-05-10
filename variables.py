#Variables: encargadas de guardar los datos con los que vamos a trabajar. Pueden ser de tipo numerico, texto
#o booleanas. Python es considerado un lenguaje con poca fuerza en su tipado, es decir, que se le pueden asignar
#diferentes valores a una variable a lo largo del codigo.

#Variable de texto (strings):
mensaje_1 = 'Hola Mundo'
mensaje_2 = "Hola Python"
varias_lineas = """Este es un texto de ejemplo 
para el Bootcamp de Lumetrio 
en el módulo de Programación con Python"""
nombre_estudiante = input("Por favor, escriba su nombre ")
print(f'{mensaje_1}, {mensaje_2}')
print(varias_lineas)
print(f'Su nombre es {nombre_estudiante}')

#Variable numerica
variable1 = 23  
variable2 = 10.28

#Variable booleana: estas variables tienen una logica binaria, por lo que solo pueden almacenar dos valores:
#verdadero o falso (True or False).
boolean1 = True
boolean2 = False

#Otra forma de declarar variables
variable1, variable2, variable3 = 23, 10.28, 'Un numero entero y un numero decimal'
#se escriben de un lado los nombres de las variables separados con coma, se utiliza el operador de
#asignacion y los valores de las variables respectivamente tambien separados con coma.

variable3 = variable4 = 5
#esta forma se utiliza cuando dos o mas variables pudieran tener el mismo valor.

#si se quiere asignar nuevos valores a una variable, por ejemplo para aumentar o disminuir su valor, hay dos formas de
#hacerlo:
mi_variable = 5
mi_variable += 1
print(mi_variable)

edad_str = input('Ingresa tu edad: ')
edad_int = int(edad_str)
print(edad_int)

x = 3
x = x + 6 #Ejemplo de operación suma larga
print(x)
x = 3
x += 7
print(x) #Ejemplo de operación suma corta

fac = 8
fac *= 3
print(fac) #Ejemplo de multiplicacion.

y = 7#el numero que se quiere elevar
y**= 2#el valor de la potencia
print (y)

z = 7
z /= 2
print (z) #Cálculo de división decimal.
z = 7
z //= 2
print (z) #Calculo de division entera.
s = 7
s //= 8
print(s)

a = 13
a /= 2
print (round(a)) #Devuelve un resultado que fuese a ser decimal como entero.
print(round(3.5))

num = 20
num -= 15
print(num) #Ejemplo de resta.
b = 15
b -= 25
print (abs(b))#Devuelve un valor negativo como positivo. #Numeros absolutos: es el mismo numero pero siempre con el signo positivo.

numero = float(input("Digite un numero: "))
resto = numero % 5#el operador % devuelve el resto de una division.
print(resto)

import math
numero = input('Introduzca un número: ')
print (f'Escribiste el numero {numero}')
print (f"El doble del número que escribiste es: {str(int(numero)*2)}")#se transforma el valor numerico en string.

num = max(8, 7)#Devuelve el numero mas alto.
print(num)
num = min(6, 5)#Devuelve el numero mas bajo.
print(num)

variable = math.ceil(9.4)#Devuelve el siguiente valor entero mas grande al introducido.
print(variable)

variable = math.floor(8.9)#Devuelve un decimal en entero, eliminmando la coma.
print(variable)

variable = math.isqrt(64)#Devuelve la raiz cuadrada del numero ingresado.
print(variable)

#Escribi un programa que despliegue un calendario
import calendar
year = int(input('Ingresar el año: ')) 
month = int(input('Ingresar el mes(numero): '))
cal = calendar.month(year, month)
print(cal)

#Escribi un programa que cambie el valor entre dos variables usando una variable "pivot".
variable = 5
variable2 = 10
print(f'valores originales: variable = {variable}, variable2 = {variable2}')
temp = variable #le asigno a temp el valor de variable
variable = variable2 #le asigno a variable el valor de variable2
variable2 = temp #le asigno a variable2 el valor almacenado en temp
print(f'valores nuevos: variable = {variable}, variable = {variable2}')

#Escribi un programa que cambie el valor de dos variables sin usar una variable pivot
a = 8
b = 18
print(f'valores originales: a={a}, b={b}')
a, b = 18, 8
print(f'valores nuevos: a={a}, b={b}')
