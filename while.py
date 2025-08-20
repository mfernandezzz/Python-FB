#While es una estructura de control utilizada para repetir un bloque de codigo en base a una condicion inicial. El bucle generado 
#finaliza cuando la condicion inicial ya no se cumpla (o si).
num_entero = int(input("Escriba un número entero par: "))
while (num_entero % 2 != 0):#el bucle se repite hasta que se introduzca un numero par.
    print("El número es impar")
    num_entero = int(input("Escriba un número entero par: "))
print("El número es par")

#Utilizar while para mostrar en pantalla los numeros del 1 al 5
i = 1
while i <= 5:
    print(i)
    i += 1
print("Fin")

#Crea una funcion que reciba dos numeros enteros como parametros para despues devolver una lista con el conteo de los numeros
#introducidos, sin contar el ultimo. Se deben contemplar los conteos regresivos.
primero, segundo = int(input('Ingrese un numero: ')), int(input('Ingrese otro numero: '))
def conteo(primero, segundo):
    while primero < segundo:
        for i in range(primero, segundo):
            print(i)
        return ''
    for e in range(primero - 1, segundo - 1, -1):
        print(e)
    return ''
print(conteo(primero, segundo))

#Pedir un numero al usuario y despues mostrar la suma de todos los numeros hasta el introducido por el usuario.
num = int(input('Escriba un numero entero: '))
i, suma = 1, 0 #i es la variable de iteracion. La variable suma almacena el resultado final
while num > 1 and i <= num: #la condicion
    suma += i #a suma se le suma el valor de i
    i += 1 #la variable de iteracion incrementa su valor en uno
print(f'La suma de todos los numeros hasta el ingresado es: {suma}')

#Crear una funcion que muestre y cuente los numeros multiplos de tres entre dos numeros dados.
num = int(input('Ingrese un numero entero: '))
num2 = int(input('Ingrese un numero entero mayor al anterior: '))
def multiplos3(num, num2):
    c = 0
    while num > num2:
        print('El segundo numero debe ser mayor al anterior.')
        num = int(input('Ingrese un numero entero: '))
        num2 = int(input('Ingrese un numero entero mayor al anterior: '))
    for i in range(num, num2 + 1):
        if i % 3 == 0:
            print(i)
            c += 1
    return (f'La cantidad de multiplos de tres entre los numeros ingresados es: {c}')
print(multiplos3(num, num2))

#crea una funcion que sume todos los elementos de una lista, utilizando while
listaNum = [2, 4, 6, 8]
def sumar(listaNum):
    suma, s = 0, 0
    while s < len(listaNum):
        suma += listaNum[s]
        s += 1
    return suma
print(sumar(listaNum))

#crea una funcion que multiplique todos los elementos de una lista, utilizando while
def mult(listaNum):
    mult, m = 1, 0 #la variable m sera de iteracion y se inicia en 0
    while m < len(listaNum): 
        mult *= listaNum[m] #se multiplica por cada elemento de la lista
        m += 1 #la variable de iteracion se incrementa en uno
    return mult
print(mult(listaNum))

#crear una funcion que utilize un while para contar y sumar los numeros pares de una lista
numReales = [1, 4, 5, 7, 8, 32, 41, 60, 25, 12]
def contarPares(numReales):
    sumPares, conteo, i = 0, 0, 0
    while i < len(numReales):
        if numReales[i] % 2 == 0: #si un numero de la lista es par
            sumPares += numReales[i] #se le suma su valor a suma pares
            conteo += 1 #se le suma uno a la variable que cuenta los numeros pares
        i += 1 #la variable de iteracion se incrementa en uno
    return (f'La suma de los numeros pares es {sumPares} y la cantidad de numeros pares es {conteo}')
print(contarPares(numReales))

#suma de Gauss usando while
numero = int(input("Introduzca un número entero: "))
while numero >= 1:
    sumaGauss = int(numero*(numero + 1)) /2
    print(f'La suma de Gaus del numero seleccionado es {sumaGauss}')
    numero = int(input("Introduzca un número entero o digite 0 para finalizar: "))
print("Fin")

#Acceso de usuario usando while
usuario, contraseña = 'Matias', 3232
usuario_input = str(input('Escriba su nombre de usuario: '))
contraseña_input = int(input('Escriba su contraseña: '))
def acceso_usuario(usuario_input, contraseña_input):
    while (usuario_input != usuario) or (contraseña_input != contraseña):
        print('Usuario o contraseña incorrectos')
        usuario_input = str(input('Escriba su nombre de usuario: '))
        contraseña_input = int(input('Escriba su contraseña: '))
    return 'Acceso autorizado'
print(acceso_usuario(usuario_input, contraseña_input))
