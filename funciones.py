#Funciones: son un fragmento de código que se ejecutará cada vez que se la invoque
#def: defining, definir
def funcion():#se define la función
    print("Contenido de la función")#el contenido de la función
    return True#se define el valor de la función, el cual devolverá

colores = ["azul", "blanco", "amarillo", "blanchedalmond", "rojo"]
def mostrar_color(i):#se define una funcion para mostrar en pantalla un color de la lista.
    print(colores[i])
def agregar_color(y):#se define una función para agregar un color a la lista utilizando append.
    colores.append(y)
agregar_color("violeta")#usamos ambas funciones
mostrar_color(5)
print(colores)

#Crea una función llamada division_segura que reciba dos parametros y muestre la división del primero entre el segundo. Debe mostrar
#un error si el denominador es cero.
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
def perimetr_triangulo(lado1=2, lado2=5, lado3=8):
    return lado1 + lado2 + lado3
print(perimetr_triangulo())

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
            print('Ecelente')
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

#Crear una funcion que reciba tres parametros: grado, previas, inasistencias. Puede aprobar si tiene maximo tres materias
#previas; si tiene mas de 3 y hasta 6 debera aprobarlas, de lo contrario reprueba. El parametro inasistencias debe ser un
#booleano, donde True es cantidad optima de asistencias y False es una cantidad mayor a la permitida. Se debe incluir un
#match case para indicar a que curso sera promovido el estudiante.
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

#la pizza perfecta no debe tener anana ni anchoas, debe tener pepperoni y/o champignones y no debe tener gluten.
#cada parametro es un booleano
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
print(f'La nota promedio obtenida en el curso fue de {str(float(promedio(notas)))}')

#Calcular el porcentaje que representa la cantidad de puntos obtenidos en el curso con respecto al maximo.
notas = [12, 11, 11, 12, 10, 10, 6, 8, 6, 12] #la cantidad de notas y su valor
nota = 12 #puntos maximos que tiene una nota
maxPuntos = len(notas) * nota #la cantidad maxima de puntos
puntosObtenidos = sum(notas) #la cantidad de puntos obtenidos
def porcentaje(puntosObtenidos, maxPuntos):
    return (puntosObtenidos * 100) / (maxPuntos)
print(f'El porcentaje de puntos obtenido en el curso fue {str(float(round(porcentaje(puntosObtenidos, maxPuntos))))}%')
