largo = len("Programación Python")
titulo = "Programación Python"
print(largo)  #devuelve la cantidad de caracteres del titulo
print(titulo[0])  #devuelve el caracter en la posicion cero
print(titulo[-1])  #devuelve el ultimo caracter del string
print(titulo[:4])  #devuelve los primeros cuatro caracteres del titulo
print(titulo[5:])  #devuelve los caracteres desde la posicion cinco en adelante
print(titulo[2:6])  #devuelve los caracteres comprendidos entre el 2 y el 6

#funcion len() para calcular la cantidad de caracteres que tiene un string. Se cuentan los espacios en blanco. Esta funcion
#tiene diversos usos, no es exclusiva de los strings.
print(len('prosopopeya'))
print(len('Buenos dias a todo el mundo'))
print(len('¿No tenes 5 minutos?'))
var = len('prosopopeya')
var2 = len('Buenos dias a todo el mundo')
print(var > var2) #guardamos el largo de un string en una variable para despues hacer una comparacion.

print(len('bombo') == len('guitarra'))
print(len('timbal') == len('flauta'))
print(len('bahia de samborombon') > len('sierra grande'))
print(len('tierra del fuego') > len('santiago del estero'))

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

#Utilizacion del operador in para saber si un string se encuentra dentro de otro.
print('amor' in 'celos')
print('placer' in 'dolor')
print('historia' in 'prehistoria')
print('proteccion de las leyes' in 'El trabajo en sus diversas formas gozara de la proteccion de las leyes, las que aseguraran...')

#saber si un string empieza o termina con un string determinado.
print(str.startswith('Fundacion e Imperio', 'Fundacion')) #primero el string y luego el que queremos evaluar.
print(str.endswith('Bueno y si', 'y si'))
print(str.endswith('hola, ¿que tal', 'hola'))

letra_cancion = input("Escriba la letra de una cancion: ")
print(letra_cancion.count('tigres'))
#funcion count para contar la cantidad de veces que se repite una palabra en un string. La funcion count()
#debe tener como atributo la palabra que se quiera contar.

print(str.strip('     ¿Por que tantos espacios?     ')) #elimina los espacios antes y despues de un string.
print(str.lower('¡BAJA EL VOLUMEN!')) #pasa a minusculas un string.
print(str.upper('¡Ahora si!')) #pasa a mayusculas un string.

#El objetivo de este ejercicio es usar triple comillado, el carácter especial \n y la función print() para mostrar un menú de 
#opciones estático y un mensaje de despedida. En este caso, no hay interacción con el usuario.
#Requisitos:
#1 - Utilizar triple comillas para definir el texto del menú(vertical) de un sitio web.
#2 - Insertar \n para generar saltos de línea entre las opciones y los mensajes.
#3 - Imprimir el menú seguido de un mensaje de despedida utilizando print().
menu = """Menu de opciones
1. Comida de Olla\n
2. Platos Asados\n
3. Ensaladas\n
4. Postres\n"""
print(menu)
print('¡Buen provecho!')

print("""Menu de opciones
1. Agregar pelicula\n
2. Mostrar peliculas\n
3. Consultar informacionde una pelicula\n
4. Obtener titulos de todas las peliculas en el catalogo\n
5. Filtrar peliculas por genero\n
6. Pelicula mas visualizada\n
7. Pelicula con mayor duracion\n
8. Pelicula con menor duracion\n
9. Salir del menu""")
