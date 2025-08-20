#Funciones: son un fragmento de código que se ejecutará cada vez que se la invoque. def: defining, definir
#Llamar a una funcion implica ejecutar el bloque de codigo de la funcion y realizar la tarea especifica que esta en ella.
#Parametro: es un valor que se espera como entrada a una funcion cuando se la declara. Es una variable que se utiliza en la
#definicion de la funcion para referirse a los datos que se pasan a la funcion cuando se la llama.
def funcion():#se define la función
    print("Contenido de la función")#el contenido de la función
    return True#se define el valor de la función, el cual devolverá

#Crea una función division_segura que reciba dos parametros y muestre la división del primero entre el segundo. Debe mostrar un error si
#el denominador es cero.
def division_segura(dividendo, divisor):
    while divisor == 0:
        print('No se puede dividir entre cero')
        dividendo = int(input('Ingrese el dividendo: '))
        divisor = int(input('Ingrese el divisor: '))
    return dividendo / divisor
dividendo = int(input('Ingrese un divisor: '))
divisor = int(input('Ingrese un dividendo: '))
print(division_segura(dividendo, divisor))

#A los parametros de una funcion se le pueden asignar valores por defecto. En el caso de que no se asignen valores a esos 
#parametros, se utilizaran los valores por defecto. 
#Crea una función que calcule el perimetro de un triangulo. La misma debe tener valores por defecto.
def perimetro_triangulo(lado1=2, lado2=5, lado3=8):
    return lado1 + lado2 + lado3
print(perimetro_triangulo())

#Crear una funcion que imprima una calificacion en base a un criterio de puntaje
def calificacion(puntos):
    if puntos >= 90 and puntos <= 100:
        return 'A'
    elif puntos >= 80 and puntos <= 89:
        return 'B'
    elif puntos >= 65 and puntos <=79:
        return 'C'
    elif puntos >= 50 and puntos <= 64:
        return 'D'
    elif puntos >= 25 and puntos <= 49:
        return 'E'
    elif puntos < 25 and puntos >= 1:
        return 'F'
    else:
        return 'Puntaje incorrecto'
puntos = int(input('Ingrese su puntaje: '))
print(calificacion(puntos))

#Estructura match case: se utiliza para comparar un valor con varios casos y ejecutar el bloque de codigo correspondiente al caso que
#coincida. Se utiliza para manejar tipos mas complejos y es util cuando se trabaja con enumeraciones o patrones especificos.
def descripcion_de_nota(nota):
    match nota:
        case 'A':
            print('Excelente')
        case 'B':
            print('Muy bueno')
        case 'C':
            print('Satisfactorio')
        case 'D':
            print('Regular')
        case 'E':
            print('Deficiente')
        case 'F':
            print('Insuficiente')
        case _:
            print('Calificacion incorrecta')
nota = input('Inserte su calificacion: ')
print(descripcion_de_nota(nota))

#Crear una funcion que reciba tres parametros: grado, previas, inasistencias. Puede aprobar si tiene maximo tres materias previas;
#si tiene mas de 3 y hasta 6 debera aprobarlas, de lo contrario reprueba. El parametro inasistencias debe ser un booleano, donde
#True es cantidad optima de asistencias y False es una cantidad mayor a la permitida. Se debe incluir un match case para indicar a
#que curso sera promovido el estudiante.
def aprobacion(grado, previas, inasistencias):
    if inasistencias:
        print('Cantidad de inasistencias optima')
        if previas <= 3:
            print('Cantidad de previas optima')
            match grado:
                case 1:
                    print(f'Promovido a 2 con {previas} materias previas.')
                case 2:
                    print(f'Promovido a 3 con {previas} materias previas.')
                case 3: 
                    print(f'Promovido a 4 con {previas} materias previas.')
                case _:
                    print('Error en el grado')
        elif previas > 3 and previas <= 6:
            print(f'Debe rendir {previas} examenes antes de poder aprobar')
        else:
            print(f'Reprueba el curso por exceso de materias previas ({previas})')
    else:
        print('Reprueba por excesiva cantidad de inasistencias')
    return 'Gracias por cursar'
grado = int(input('Inserte su grado: '))
previas = int(input('Ingrese su cantidad de materias previas: '))
inasistencias = True
print(aprobacion(grado, previas, inasistencias))

#Pedir al usuario su calificacion y decirle si aprobo o no. Para aprobar su nota debe ser mayor o igual a 6, si su nota
#es 4 o 5 debe rendir examen y si es 1, 2 o 3 reprueba la materia.
def aprobacion(nota):
    if nota >= 6:
        print(f'Aprobado con: {str(int(nota))}')
    elif nota == 5 or nota == 4:
        print(f'Su nota es: {str(int(nota))}. Debe rendir examen.')
    elif nota <= 3 and nota >= 1:
        print(f'Reprueba la materia con: {str(int(nota))}')
    else:
        print('La nota es incorrecta')
    return 'Fin'
nota = int(input('Ingrese su nota final: '))
print(aprobacion(nota)) 

#Crear una funcion que devuelva True si un numero es divisible por 3 y por 5
def divisible_3y5(num):
    return (num % 3 == 0) and (num % 5 == 0)
num = int(input('Ingrse un numero: '))
print(divisible_3y5(num))

#Crear una funcion que reciba un numero y devuelva True si el numero es par y False si el numero es impar.
def es_par(numero):
    return (numero % 2 == 0)
numero = int(input('Ingrese un numero entero: '))
print(es_par(numero))

#Crear una funcion llamada entre_100_y_ 999 que devuelva True si el numero ingresado esta en ese rango.
def esta_entre_100_y_999(numero):
    return (numero > 100) and (numero < 999)
numero = int(input('Ingrese un numero: '))
print(esta_entre_100_y_999(numero))

#La pizza perfecta no debe tener anana ni anchoas, debe tener pepperoni y/o champignones y no debe tener gluten.
#Cada parametro es un booleano.
def pizza_perfecta(anana, anchoas, pepperoni, champiñones, gluten):
    return not(anana or anchoas) and (pepperoni or champiñones) and not(gluten)
print(pizza_perfecta(False, False, True, False, False))

#Funcion para calcular areas de algunas figuras planas
import math
def area_triangulo(base, altura):
    return (base * altura) / 2
def area_cuadrado(lado):
    return (math.pow(lado, 2))
def area_rectangulo(base, altura):
    return (base * altura)

#Crear una calculadora de IMC
def calculo_imc(altura, peso):
    print('Calculadora de IMC')
    imc = (peso * 10000) / (altura**2)
    if imc >= 30:
        return 'Obesidad'
    elif imc >= 25:
        return 'Sobrepeso'
    elif imc >= 18:
        return 'Peso optimo'
    else:
        return 'Bajo peso'
altura = (float(input('Introduzca su altura en centimetros: ')))
peso = (float(input('Introduzca su peso en kilogramos: ')))
print(calculo_imc(altura, peso))

#Calcular la nota promedio del curso
notas = [12, 11, 11, 12, 10, 10, 6, 8, 6, 12]
def promedio(notas):
    return sum(notas) / len(notas)
print(f'La nota promedio obtenida en el curso fue de {promedio(notas}')

#Calcular el porcentaje que representa la cantidad de puntos obtenidos en el curso con respecto al maximo.
notas = [12, 11, 11, 12, 10, 10, 6, 8, 6, 12] #la cantidad de notas y su valor
maxPuntos = len(notas) * 12 #la cantidad maxima de puntos
puntosObtenidos = sum(notas) #la cantidad de puntos obtenidos
def porcentaje(puntosObtenidos, maxPuntos):
    return (puntosObtenidos * 100) / (maxPuntos)
print(f'El porcentaje de puntos obtenido en el curso fue {round(porcentaje(puntosObtenidos, maxPuntos))}%')

#Ejercicio Conversión de Temperaturas: Crea una función que convierta una temperatura en grados Celsius a Fahrenheit.
#La fórmula de conversión es: °F=(°C×1,8)+32°F
def convertir_farenheit(celsius):
    return (f'La temperatura ingresada equivale a {((celsius * 1.8) + 32)} Farenheit')
temperatura = float(input('Ingrese un valor de temperatura en grados celsius: '))
print(convertir_farenheit(temperatura))

#¿Cual es la relacion entre la funcion principal y la funcion anidada en terminos de flujo de ejecucion?
#El flujo cambia a la funcion anidada y luego cambia a la funcion principal. Al finalizar la ejecucion de una funcion el
#flujo retorna al punto siguiente al que fue llamada, sea esto dentro de otra funcion, o no.

#¿En que se diferencia un procedimiento de una funcion? Los procedimientos no tienen un retorno, pero si tienen un
#efecto al ser invocados.

#saber si un string es una pregunta o no, si la pregunta es en español, empieza y termina con un signo de interrogacion.
def es_pregunta(oracion):
    return str.startswith(oracion, '¿') and str.endswith(oracion, '?')
oracion = input('Escriba una oracion (puede ser una pregunta): ')
print(es_pregunta(oracion))

def suma_longitudes(string, string2):
    return (f'La suma de los caracteres de ambas palabras es: {(len(string)) + (len(string2))}')
string = input('Escriba un string: ')
string2 = input('Escriba otro string: ')
print(suma_longitudes(string, string2))

def son_las_doce(hora):
    return hora == 12
la_hora = int(input('Ingrese una hora: '))
print(son_las_doce(la_hora))

#Invocar funciones dentro de otra funcion
def doble(numero): #creamos la funcion que devuelve el doble de un numero ingresado como parametro
    return numero * 2
def siguiente_del_doble(numero): #creamos la funcion que tome la funcion anterior y le sume 1
    return doble(numero) + 1
numero = float(input('Ingrese un numero: '))
print(siguiente_del_doble(numero))

#Ejercicio: define una funcion anterior (que recibe un numero y devuelve uno menos), triple (el triple de un numero) y
#anterior del triple que recibe el numero triplicado y le resta 1
def anterior(entero):
    return entero - 1 #recibe un numero y le resta uno
def triple(entero):
    return entero * 3 #recibe un numero y lo multiplica por tres
def anterior_del_triple(entero):
    return anterior(triple(entero)) #recibe un numero, lo multiplica por tres y le resta uno
entero = int(input('Ingrese un numero entero: '))
print(anterior_del_triple(entero))

#Ejercicio: crear una funcion que reciba tres numeros como parametros y devuelva un booleano determinando si el primer numero es
#mayor o igual al segundo y menor o igual al tercer. Luego crear otra funcion que haga lo contrario a la primera.
def estaEntre(num, num2, num3):
    return (num >= num2) and (num <= num3)
def estaFueraRango(num, num2, num3):
    return (num <= num2) and (num >= num3)
num = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un segundo numero: '))
num3 = int(input('Ingrese un tercer numero: '))
print(estaEntre(num, num2, num3))
print(estaFueraRango(num, num2, num3))

#Ejercicio: crea una funcion que reciba un string y lo devuelva en mayusculas y entre signos de exclamacion.
def mayusculas(string):
    return (f'¡{str.upper(string)}!')
string = str(input('Escriba una palabra o palabras: '))
print(mayusculas(string))

#Ejercicio: escribi una funcion que tome un dia de semana y devuela un booleano dependiendo de si es fin de semana o no.
def es_fin_de_semana(dia):
    return dia == 'sabado' or dia == 'domingo'
dia = str.lower(input('Escriba un dia de semana: '))
print(es_fin_de_semana(dia))

#¿Que hace el siguiente codigo?
def funcionA():
    print(1)
    def funcionB():
        print(2)

def funcionC():
    def funcionD():
        print(3)

    print(4)
    funcionD()

def funcionE():
    funcionA()

print(5)
funcionC()
#Explicacion:
#Primero se imprime el numero 5. Luego se llama a la funcionC, que contiene la declaracion de la funcionD() un print y la llamada
#a la funcionD(). Por lo que primero se ejecuta el print con el numero 4 y luego la funcionD que imprime en pantalla el numero 3.
#Por lo tanto, el codigo lo que hace es mostrar el 543.

#Explicacion2:
#El flujo inicia en la línea 16 imprimiendo 5, ya que antes solo hay definiciones. Luego llama a funcionC(), por lo que el flujo 
#salta a la línea 6, allí lo primero que no es una definición es la línea 10, que indica imprimir un 4. En la línea 11 se llama a 
#funcionD(), y el código pasa a la línea 7. en funcionD() se indica imprimir 3. Luego finaliza la ejecución de funcionD(), por lo 
#que el flujo vuelve a la línea 11. Finaliza funcionC(), y el código vuelve a la línea 17, y finaliza el programa. El flujo nunca 
#pasa por el resto de las líneas.
