#El condicional if es una estructura de control que determina que codigo se va a ejecutar y cual no en base a una condicion.
clima = input('¿Me puedes decir como esta el clima afuera? ¿Esta despejado o nublado? ')
if clima == 'despejado':
    print('Entonces salgo de manga corta')
else:
    print('Llevare abrigo y paraguas')

#Estructura if con variable booleana.
esta_lloviendo, esta_nublado = False, False
if esta_lloviendo:
    print('Uso el paraguas')
elif esta_nublado:
    print('Llevo el paraguas')
else:
    print('No va a llover')

#utilizando int, determino que lo introducido por el usuario será una variable numérica(entero), de lo contrario,
#será considerado como un string y contara la cantidad de caracteres.
n1, n2 = int(input("Introduce un número entero: ")), int(input("Introduce otro número entero: "))
if (n1 > n2):
    print ("n1 es más grande")
elif (n1 == n2):
    print ("los numeros son iguales")
else:
    print ('n2 es mas grande')

#float permite la introduccion de un numero decimal.
n1, n2 = float(input("Introduce un número ")), float(input("Introduce otro número "))
if (n1 > n2):
    print('El primer número ingresado es más grande')
elif (n1 == n2):
    print('los numeros son iguales')
else:
    print('el segundo numero es mas grande')

#if a and not b
tiempo_libre, mucho_frio = False, False
if tiempo_libre and not mucho_frio:
    print("Salgo a correr")
elif not tiempo_libre and mucho_frio:
    print("Esta lindo para cocinar")
else:
    print("Hago ejercicio en casa")

#if a and b and not c
dia_soleado, andar_bicicleta, dia_de_semana = True, True, False
if dia_soleado and andar_bicicleta and not dia_de_semana:
    print ("Salgo a andar en bicicleta")
else:
    print ("Me quedo en casa")

#if not a and not b
comida_preparada, ingredientes = False, True
if not comida_preparada and not ingredientes:
    print("Pido delivery")
elif comida_preparada and ingredientes:
    print("Como lo que haya")
else:
    print("Preparo comida")

#if a or (b and c)
hacer_tramite, hacer_compras, pagar_facturas = False, False, False
if hacer_tramite or (hacer_compras and pagar_facturas):
    print('Salgo a cumplir obligaciones')
elif hacer_tramite == False and hacer_compras or pagar_facturas:
    print('Voy a la tienda o al local de cobranzas')
else:
    print('No tengo que salir de casa')

#Operador logico and: retorna True si se cumplen todas las condiciones y False si no se cumple una.
caracol = str.startswith("caracol", "cara") and str.endswith("caracol", "col")
print(caracol)

#Operador logico not: sirve para colocar el valor opuesto de la condicion.
estoy_cansado = True
if not(estoy_cansado):
    print ("Me acuesto a dormir")
else:
    print ("Sigo despierto")
cumpleaños = False
if not(cumpleaños):
    print("Feliz cumpleaños")
else:
    print("No es su cumpleaños")

#Operador logico or: devuelve True si se cumple una de las condiciones y False si no se cumple ninguna.
saludo_despedida = str.lower("HOLA") == "hola" or str.lower("adiós") == "adiós"
print(saludo_despedida)
comp = len("hola") > 5 or abs(-5) == 5
print(comp)

#Condicion para que se cumpla a, se cumpla b pero no se cumpla c
dia_soleado, tiempo_libre, tareas = True, True, True
if (dia_soleado and tiempo_libre) and not tareas:
    print("Salgo andar en bicicleta")
else:
    print("Hago las tareas")

#Condicion para que se cumpla a o b y c juntas
ingredientes, tiempo_libre, no_hay_cena = False, True, False
if ingredientes or (tiempo_libre and no_hay_cena):
    print("Preparo algo de comer")
else:
    print("Hago otra cosa")

#Condicion para que se cumpla a o b y c juntas pero no si se cumplen las tres
#(a or(b and c)) and not (a and b and c) 
a, b, c = False, False, True
if a or (b and c) and not(a and b and c):
    print('Se cumple')
else:
    print('No se cumple')
