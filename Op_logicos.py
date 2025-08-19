#El condicional if es una estructura de control que determina que codigo se va a ejecutar y cual no en base a una condicion.
#Ejercicio: defini una funcion llamada signo que devuelva 1 si el numero es positivo, 0 si el numero es 0 o -1 si el numero es negativo.
def signo(numero):
    if numero > 0:
        return 1
    elif numero == 0:
        return 0
    else:
        return -1
numero = int(input('Escriba un numero: '))
print(signo(numero))

#float permite la introduccion de un numero decimal.
n1, n2 = float(input("Introduce un número ")), float(input("Introduce otro número "))
if (n1 > n2):
    print('El primer número ingresado es más grande')
elif (n1 == n2):
    print('los numeros son iguales')
else:
    print('el segundo numero es mas grande')

def decision_con_moneda(moneda, comida1, comida2):
    if moneda == 'cara':
        return comida1
    else:
        return comida2
comida1 = str(input('Escriba una comida: '))
comida2 = str(input('Escriba otra comida: '))
print(decision_con_moneda('ceca', comida1, comida2))

#Ejercicio: crea una funcion llamada medalla_segun_puesto que le asigne la medalla correspondiente a los competidores
#dependiendo de su posicion.
def medalla_segun_puesto(posicion):
    if posicion == 1:
        return 'Oro'
    elif posicion == 2:
        return 'Plata'
    elif posicion == 3:
        return 'Bronce'
    else:
        return 'Sin medalla'
posicion = int(input('Posicion obtenida: '))
print(medalla_segun_puesto(posicion))

#Ejercicios:
#a and not b
print(True and (not(False))) #True
#a and b and not c
print(True and True and not(True)) #False
#not a and not b
print(not(True) and not(True)) #False
#a or (b and c)
print(True or (True and False)) #True
#a and b and not(c)
print(False and False and not(False)) #False
#a or (b y c)
print(True or (False and False)) #True
#(a or(b and c)) and not (a and b and c)
print(True or (True and False) and not(True and True and False)) #True

#Ejercicio: para Emma un numero es de la suerte si es positivo, es menor a 100 y no es el 15. Crear una funcion que tomando
#en cuenta esto determine si un numero es de la suerte o no.
def numero_suerte(numero):
    return (numero > 0) and (numero < 100) and (numero != 15)
numero = int(input('Ingrese un numero: '))
print(numero_suerte(numero))

#Ejercicio: defini una funcion llamada escribir_cartelito que tome un titulo, un nombre, un apellido y arme un unico string.
def escribir_cartelito(titulo, nombre, apellido):
    return (f'{titulo} {nombre} {apellido}')
titulo, nombre, apellido = str(input('Introduzca la abreviacion de su titulo: ')), str(input('Escriba su nombre: ')), str(input('Escriba su apellido: '))
print(escribir_cartelito(titulo, nombre, apellido))

#Ejercicio: tomando en cuenta el ejercicio anterior, crea una funcion que imprima un cartelito corto (titulo y apellido) o
#un cartelito completo.
def escribir_cartelito_2(titulo, nombre, apellido, tamaño):
    if tamaño:
        return (f'{titulo} {nombre} {apellido}')
    else:
        return (f'{titulo} {apellido}') 
tamaño = True
titulo, nombre, apellido = str(input('Introduzca la abreviacion de su titulo: ')), str(input('Escriba su nombre: ')), str(input('Escriba su apellido: '))
print(escribir_cartelito_2(titulo, nombre, apellido, tamaño))

#Ejercicio: defini la funcion crear_cartelito_optimo que reciba un titulo, nombre, apellido e invoque escribir_cartelito
#para generar un cartelito corto o largo. Si el nombre y el apellido tienen mas de 15 caracteres, el cartel debe ser
#corto, de lo contrario, el cartel sera largo.
def cartelito_optimo(titulo, nombre, apellido):
    return escribir_cartelito_2(titulo, nombre, apellido, (len(nombre) + len(apellido) < 15))#la condicion es el booleano
titulo, nombre, apellido = str(input('Introduzca la abreviacion de su titulo: ')), str(input('Escriba su nombre: ')), str(input('Escriba su apellido: '))
print(cartelito_optimo(titulo, nombre, apellido))

#Ejercicio: crear una funcion llamada valor_envido que devuelva el valor de envido de las cartas de truco. Sabemos que las
#cartas del 1 al 7 valen su numeracion, las cartas del 10 al 12 inclusive valen 0, no se juegan con 8s y 9s.
def valor_envido(num_carta):
    if num_carta >= 1 and num_carta <= 7:
        return num_carta
    elif num_carta >= 10 and num_carta <= 12:
        return 0
    else:
        return 'no se juega con ochos o nueves'
num_carta = int(input('Introduzca el numero de una carta: '))
print(valor_envido(num_carta))

#Ejercicio: crear una funcion para calcular los puntos de envido sabiendo que si las dos cartas son del mismo palo, el
#valor de envido es la suma de sus valores de envido mas 20. De lo contrario, el valor de envido es el mayor valor de
#envido entre ellas.
def puntos_envido_totales(val, carta, val2, carta2):
    if (carta == carta2):
        return valor_envido(val) + valor_envido(val2) + 20
    elif (carta != carta2): #distinto
        return max(valor_envido(val), valor_envido(val2))
    else:
        return 'No se juega con esas cartas'
val = int(input('Ingrese el valor de la carta: '))
carta = str.lower(input('Escriba el palo de la carta: '))
val2 = int(input('Ingrese el valor de la segunda carta: '))
carta2 = str.lower(input('Ingrese el palo de la segunda carta: '))
print(puntos_envido_totales(val, carta, val2, carta2))
#Este codigo funciona siempre y cuando no se introduzca 8 o 9.

#Ejercicio: en el truco, los cantos tienen diferente valor. Truco vale 2, retruco vale 3 y vale cuatro vale 4.
#Crea una funcion que se llame valor_canto_truco que reciba el canto y devuelva su respectivo valor.
def valor_canto_truco(canto):
    if canto == 'truco':
        return 2
    elif canto == 'retruco':
        return 3
    elif canto == 'vale cuatro':
        return 4
    else:
        return 'eso no es un canto de truco'
canto = str.lower(input('Canto de truco: '))
print(valor_canto_truco(canto))

#Ejercicio: crear una funcion que determine si un numero es par o no y una funcion que determine lo contrario.
def es_par(numero):
    return numero % 2 == 0
#def es_impar(numero):
#    return numero % 2 != 0
def es_impar(numero):
    return not(es_par(numero)) #se invierte el valor de la condicion
print(es_par(8))
print(es_impar(8))

#Ejercicio: crea una funcion llamada mayor_de_edad y otra llamada menor_de_edad a partir de ella.
def mayor_de_edad(edad):
    return edad >= 18
def menor_de_edad(edad):
    return not(mayor_de_edad(edad))
edad = int(input('Ingrese su edad: '))
print(mayor_de_edad(edad))
print(menor_de_edad(edad))

#Ejercicio: defini una funcion que se llame es_peripatetica que tome el area en que se desempeña una persona, su pais de
#origen y la cantidad de kilometros que camina por dia. Una persona es peripatetica cuando se desempeña en filosofia, 
#su pais de origen es Grecia y le gusta pasear (camina mas de 2 kilometros por dia).
def es_peripatetica(area, pais, kilometros):
    return (area == 'filosofia') and (pais == 'grecia') and (kilometros >= 2)
area = str.lower(input('¿En que area de estudio se desempeña?'))
pais = str.lower(input('¿Cual es su pais natal?'))
kilometros = float(input('¿Cuantos kilometros camina por dia?'))
print(es_peripatetica(area, pais, kilometros))

#Ejemplo de disyuncion or
def gano(cumplio_objetivo, cantidad_paises_conquistados):
    return cumplio_objetivo or (cantidad_paises_conquistados >= 30)
cantidad_paises_conquistados = int(input('Cantidad de paises conquistados: '))
print(gano(False, cantidad_paises_conquistados))

#Ejercicio: crear una funcion (o funciones) que determine si un banco esta abierto o esta cerrado. Se debe tomar en cuenta
#que el horario bancario es de 10 a 15, si es fin de semana y si es feriado.
def horarioBancario(horario):
    return horario >= 10 and horario <= 15
def esDiaHabil(dia):
    return not(dia == 'sabado' or dia == 'domingo')
def esFeriado(feriado):
    return not(feriado == 'si')
def estaAbierto(horario, dia, feriado):
    return (horarioBancario(horario) and esDiaHabil(dia) and esFeriado(feriado))
horario = int(input('Ingrese la hora en punto sin los minutos: '))
dia = str.lower(input('Ingrese un dia de la semana: '))
feriado = str.lower(input('¿Es un dia feriado? si/no: '))
if (estaAbierto(horario, dia, feriado)):
    print('La sucursal bancaria esta abierta.')
else:
    print('La sucursal bancaria esta cerrada.')

#Ejercicio: crea una funcion llamada tiene_contraste, que reciba como argumentos el color de la letra y el color de fondo
#de la pagina. La misma tiene contraste si el fondo es claro y la letra no o viceversa.
def es_tono_claro(color):
    return (color == 'rosado') or (color == 'amarillo') or (color == 'blanco') or (color == 'celeste') or (color == 'gris')
#El operador != determina que habra contraste, debido a que ambos colores tienen diferente tonalidades, ademas de ser diferentes.
def tiene_contraste(color_letra, color_fondo):
    return es_tono_claro(color_letra) != es_tono_claro(color_fondo)
color_letra = str.lower(input('Color de letra: '))
color_fondo = str.lower(input('Color de fondo: '))
print(tiene_contraste(color_letra, color_fondo))
#El ejercicio anterior corresponde a la disyuncion logica xor, y su operador es el ^. Si los valores booleanos son
#iguales el resultado sera False, y si son diferentes sera True.
#print(False ^ False)
#print(True ^ False)

#Precedencia: cuando una operacion matematica tiene varios operadores, las multiplicaciones y divisiones se efectuaran antes que las
#sumas y las restas. Al igual que en matematica, cuando se usan operadores logicos, se evaluan en un orden determinado llamado precedencia.

#Ejercicio: crea la funcion para que determinar una persona se puede concentrar o no. Para que se pueda concentrar la infusion 
#debe ser mate a 80Cº o te a exactamente 95Cº mas el booleano que determina si esta programando o no.
def se_puede_concentrar(bebida, temperatura, programando):
    return (bebida == 'mate' and temperatura == 80) or (bebida == 'te' and temperatura >= 95) and programando
bebida = str.lower(input('¿Que bebida esta tomando? '))
temperatura = int(input('¿A que temperatura? '))
programando = True
print(se_puede_concentrar(bebida, temperatura, programando))

#Ejercicio: establecer una funcion que determine si una persona puede subirse o no a una montaña rusa. Los requisitos para
#subir son: estatura minima de 1.5 metros (o 1.2 si esta acompañado) y no tener afecciones cardiacas. Por lo tanto, la funcion
#tendra tres parametros: la altura, si esta acompañado por un adulto y si tiene afecciones cardiacas.
def puedeSubirse(estatura, acompañado, afeccion):
    return ((estatura >= 1.5) or (estatura >= 1.2 and acompañado)) and not(afeccion)
estatura = float(input('Ingrese la estatura: '))
acompañado = False
afeccion = True
if puedeSubirse(estatura, acompañado, afeccion):
    print('Se puede subir.')
else:
    print('No se puede subir.')

#opcion 2
estatura = float(input('Ingrese la estatura: '))
acompañado = str.lower(input('¿La persona esta acompañada por un mayor? si/no: '))
afeccion = str.lower(input('¿La persona tiene alguna afeccion cardiaca? si/no: '))
if acompañado == 'si':
    acompañado = True
elif acompañado == 'no':
    acompañado = False
else:
    print('Dato incorrecto.')

if afeccion == 'si':
    afeccion = True
elif afeccion == 'no':
    afeccion = False
else:
    print('Dato incorrecto')

if puedeSubirse(estatura, acompañado, afeccion):
    print('Se puede subir.')
else:
    print('No se puede subir.')
    
