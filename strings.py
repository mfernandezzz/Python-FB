largo = len("Programación Python")
titulo = "Programación Python"
print(largo)  #devuelve la cantidad de caracteres del titulo
print(titulo[0])  #devuelve el caracter en la posicion cero
print(titulo[-1])  #devuelve el ultimo caracter del string
print(titulo[:4])  #devuelve los primeros cuatro caracteres del titulo
print(titulo[5:])  #devuelve los caracteres desde la posicion cinco en adelante
print(titulo[2:6])  #devuelve los caracteres comprendidos entre el 2 y el 6

saludo = len("¿Como estas?")
print(saludo)

comparacion = len("Tierra del Fuego") == len("Santiago del Estero")
print(comparacion)

comparacion2 = len("un_string") > len("otro_string")
print(comparacion2)

nombre_completo = input("Por favor, escribe tu nombre completo ")
postre_favorito = input("¿Cuál es tu postre favorito? ")
comida_favorita = input("¿Cual es tu comida favorita? ")
print(f'La primer respuesta tiene {str(int(len(nombre_completo)))} caracteres.')
print(f'La segunda respuesta tiene {str(int(len(postre_favorito)))} caracteres.')
print(f'La tercera respuesta tiene {str(int(len(comida_favorita)))} caracteres.')

nombre = str.capitalize(input("Escriba su nombre: "))
apellido = str.capitalize(input("su apellido: "))
edad = int(input("su edad: "))
nacionalidad = str(input("su nacionalidad: "))
país_de_residencia = str.capitalize(input("país donde reside: "))
departamento_o_región_residencia = str.capitalize(input("Departamento o región donde reside: "))
estado_civil = str(input("¿Cuál es su estado civil?: "))
print (f'Los datos ingresados son: {nombre} - {apellido} - {edad} - {nacionalidad} - {país_de_residencia} - {departamento_o_región_residencia} - {estado_civil}')

nombre = input('inserte su nombre: ')
print(nombre.capitalize())#La funcion capitalize devuelve el valor de un texto con el primer caracter en mayuscula.
nombre = input('inserte su nombre: ').capitalize()
print(nombre)

text = "historia" in "prehistoria" #operador in para verificar si un string se encuentra dentro de otro.
print(text)

text = str.startswith("Fundación e imperio", "Fundación")
print(text) #funcion que determina si un string empieza o no con la palabra o caracter asignado. Devuelve un booleano.

text = str.endswith("Hola, ¿qué tal?", "Hola")
print(text) #funcion que determina si un string termina o no con la palabra o caracter asignado. Devuelve un booleano.

letra_cancion = input("Escriba la letra de una cancion: ").count('comian')
print(letra_cancion)
letra_cancion = input("Escriba la letra de una cancion: ")
print(letra_cancion.count('tigres'))
#funcion count para contar la cantidad de veces que se repite una palabra en un string. La funcion count()
#debe tener como atributo la palabra que se quiera contar.

espaciado = str.strip("    ¿Por qué tantos espacios?       ")
print(espaciado) #funcion que elimina los espacios antes y despues de un string.

volumen = str.lower('BAJÁ EL VOLUMEN')
print(volumen) #la funcion lower vuelve todo el string en minuscula.

now = str.upper('¡Ahora sí!')
print(now) #la funcion upper vuelve todo el texto a mayuscula.

#Escribe un programa que pida al usuario su nombre, edad y devuelva un mensaje.
nombre, edad = str(input('Escriba su nombre: ')), int(input('Ingrese su edad: '))
def saludo(nombre, edad):
    return (f'Hola, tu nombre es {nombre} y tu edad es {edad} años')
print(saludo(nombre, edad))
