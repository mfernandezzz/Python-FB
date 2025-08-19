#Los diccionarios son otra forma de guardar elementos. Son parecidos a las listas, pero con la diferencia de que contienen
#informacion vinculada con otra y que a determinada informacion se accede a traves de su respectiva clave. Junto con las listas,
#se los conoce como estructuras de datos. Cada una tiene una utilidad especial, cada una sera mas util que otra dependiendo de la
#tarea a resolver. Hay muchas estructuras de datos diferentes aunque listas y diccionarios son las mas utilizadas.

animales = {'Vacas':2, 'Cerdo':3, 'Gallinas': 10}
print(animales)
#A diferencia de las listas, los elementos de los diccionarios no tienen posicion sino que accedemos a ellos a traves de un
#valor clave (key).
print(animales['Cerdo'])
#verificar la existencia de una clave
print('Cerdo' in animales)
print('cerdo' in animales)
print('Caballo' in animales)

#Tipos de claves y valores: las claves de los diccionarios pueden ser strings, numeros enteros, numeros decimales, tuplas y otros 
#objetos. Las listas no pueden usarse como clave. Los valores del diccionarios almacenados en cada clave pueden ser de cualquier tipo: 
diccionario2 = {
    10:[1,2,3], #clave con sus respectivos valores
    20:"cool",
    30:[3,2,1,0],
    40:[]
}
print(diccionario2[30]) #se accede a determinados elementos en base a su clave correspondiente

diccionario3 = {
    0.2345:"x",
    0.1209:"y",
    0.1122:"z"
}
print(diccionario3[0.1209])

diccionario4 = {
    ("juana",28):[0,0,0], #una tupla como clave y su elemento correspondiente
    ("pepe",27):[1,2,1]
}
print(diccionario4["juana",28])

#Modificar elementos
animales_sal = {
    'Leon':2, 
    'Tigre': 5, 
    'Pantera': 8
}
animales_sal['Tigre'] = 6 #se modifica el valor para la clave especificada
print(animales_sal)

#Agregar datos 
animales_sal['Rinoceronte'] = 11 #se agrega al diccionario una clave y su valor correspondiente
print(animales_sal)

#Eliminar un elemento
valor_pantera = animales_sal.pop('Pantera') #se elimina la clave y su valor se almacena en la variable
print(valor_pantera)#variable que almacena el valor que contenia la clave pantera
print(animales_sal)
animales_sal['Pantera'] = valor_pantera #vuelvo agregar pantera al diccionario con su valor previo
print(animales_sal)

#Usar una funcion para iterar en un diccionario
comidas = {
    0: 'Asado',
    1: 'Ravioles',
    2: 'Ensalada Rusa',
    3: 'Sopa',
    4: 'Pollo y Pescado'
}
def recorrerDict(comidas):
    for i in comidas:
        print(f'Clave: {i}, Valor: {comidas[i]}')
    return ' '
print(recorrerDict(comidas))

#Otras funciones para obtener los elementos de un diccionario
print('Obtener tuplas (clave, valor): ', comidas.items())
print('Obtener solo claves: ', comidas.keys())
print('Obtener solo valores: ', comidas.values())

#La funcion dict() permite crear diccionarios a partir de tuplas o listas
#Convertir lista de tuplas en diccionario
x = [("a",1), ("b",2), ("c",3)] #lista de tuplas
d = dict(x) #diccionario cuyas claves y valores se obtendran de la tupla anterior
print(d)

#Convertir la lista de listas en diccionario
j = [[1, 10], [2, 20], [3, 30]]
dicc = dict(j)
print(dicc)

#Crea una funcion que se llame crear_diccionario(l1, l2) que reciba dos parametros de tipo lista y devuelva un diccionario
#cuyas claves estaran dadas por l1 y los valores respectivos estaran dados por l2.
l1 = ['Jorge', 'Julian', 'Agustin', 'Esteban', 'Marcos']
l2 = [28, 34, 46, 52, 22]
def crearDiccionario(l1, l2):
    d = {}
    for i in l1:
        for j in l2:
            d[i] = j#los elementos obtenidos por i seran claves y los elementos obtenidos por j seran valores
    return d
#solucion 2
def crear_diccionario(l1, l2):
    return dict(zip(l1, l2))#con el metodo zip transformas las listas en tuplas y con dict se crea el diccionario.

#Crea una funcion key_in_dictionary(d, key) que reciba dos parametros, un diccionario y una clave. Se debe devolver True si
#la clave existe en el diccionario o False en caso contrario.
d = {'Alicia': 33, 'Bob': 35, 'Carla': 31}
key = 'Bob'
def key_in_dictionary(d, key):
    return (key in d)
print(key_in_dictionary(d, key))

#Crea una funcion valor_en_diccionario(d, valor) que reciba un diccionario y un valor. Devolver True si el valor existe en el
#diccionario o False en caso contrario.
d = {'Marcos': 12, 'Alan': 13, 'Alfonso': 15}
valor = 14
def value_in_dictionary(d, valor):
    return valor in d.values()
print(value_in_dictionary(d, valor))

#Crea una funcion eliminate_key(d, valor) que reciba un diccionario y una clave. Se debe eliminar la clave del diccionario y
#devolver el diccionario modificado.
d = {'Pedro': 34, 'Xavi': 24, 'Tom': 39}
key = 'Pedro'
def eliminarclave(d, key):
  if key in d:
    d.pop(key)
    return d
print(eliminarclave(d, key))

#Listas que contienen diccionarios
#Los diccionarios como los vistos hasta ahora pueden combinarse con las listas, lo que dara como resultado una lista que contiene
#diccionarios. Esto nos permite manejar bloques de datos, donde cada bloque de datos es un diccionario contenido dentro de una lista.
persona = {
    'nombre_apellido': 'Julián Rodríguez',
    'edad': 28,
    'estado_civil': 'casado'
}
print(persona['edad']) 
persona['nacionalidad'] = 'uruguayo'#así podemos agregar datos a un diccionario
persona['nombre_apellido'] = 'Mateo Hernández'#así se puede editar información a un diccionario
print(persona)

#Lista que contiene diccionarios
trabajadores = [{
        'nombre': 'Marcos',
        'apellido': 'Garcia',
        'edad': 26,
        'nacionalidad': 'Español',
        'identificador': 26891,
    },{
        'nombre': 'Agustin',
        'apellido': 'Alvarez',
        'edad': 22,
        'nacionalidad': 'Argentino',
        'identificador': 34278
    },{
        'nombre': 'Marcos',
        'apellido': 'Gonzalez',
        'edad': 34,
        'nacionalidad': 'Uruguayo',
        'identificador': 15932,
    },{
        'nombre': 'Julian',
        'apellido': 'Gonzalez',
        'edad': 26,
        'nacionalidad': 'Chileno',
        'identificador': 59143,
    },{
        'nombre': 'Evaristo',
        'apellido': 'Fernandez',
        'edad': 22,
        'nacionalidad': 'Argentino',
        'identificador': 62891,
    }]
#Cambiar un dato en un bloque de datos en el diccionario utilizando el identificador.
for t in trabajadores:
    if t['identificador'] == 26891:
        t['nombre'] = 'Ruben'

#Cambiar la edad a los trabajadores con apellido Gonzalez.
for t in trabajadores:
    if t['apellido'] == 'Gonzalez':
        t['edad'] = 25
#Cuando se modifica un dato utilizando como referencia otro dato repetido, se modificara el dato seleccionado
#a ambos bloque de datos.

#Cambiar la nacionalidad de un trabajador usando su id.
for t in trabajadores:
    if t['identificador'] == 34278:
        t['nacionalidad'] = 'Colombiano'

#Cambiar un dato sin usar el identificador.
for t in trabajadores:
    if t['nombre'] == 'Evaristo' and t['apellido'] == 'Fernandez':
        t['nacionalidad'] = 'Mexicano'

#Agregar informacion a un bloque de datos.
for t in trabajadores:
    if t['identificador'] == 26891:
        t['rango'] = 'Senior Back-End'

#Ordenar el diccionario trabajadores en orden ascendente por el valor de sus ID
def obtenerID(i): #funcion que obtendra el valor de todos identificadores
    return i['identificador']
trabajadores.sort(key=obtenerID) #se ordena el diccionario por valor de ID ascendente
print(trabajadores)
#en caso de querer ordenar los ID en orden descendente, se debe utilizar especificar en el metodo sort
trabajadores.sort(key=obtenerID, reverse=True)
print(trabajadores)

#Diccionario con informacion de alumnos
alumnos = [{
    'nombre': 'Karla',
    'apellido': 'González', 
    'nota': 7,
    'inasistencias': 8, 
},{
    'nombre': 'Andrés',
    'apellido': 'Rodríguez',
    'nota': 10,
    'inasistencias': 1,
},{
    'nombre': 'Thiago',
    'apellido': 'Hernández',
    'nota': 9,
    'inasistencias': 2,
},{
    'nombre': 'Carolina',
    'apellido': 'Goicoechea',
    'nota': 11,
    'inasistencias': 4,
},{
    'nombre': 'Juan',
    'apellido': 'Alcaraz',
    'nota': 9,
    'inasistencias': 4
}]

for a in alumnos:
    if a['nombre'] == 'Karla':
        a['nombre'] = 'Sofía' #cambiar el nombre a un alumno

for b in alumnos:
    if b['apellido'] == 'González':
        b['apellido'] = 'Esteche' #cambiar el apellido a un alumno

#Modificá la nota de Juan a 12 usando su apellido con el fin de diferenciarlo de otros alumnos que tambien se puedan llamar Juan.
for a in alumnos:
    if a['nombre'] == 'Juan' and a['apellido'] == 'Alcaraz':
        a['nota'] = 12
print(alumnos)

#Agregar a Punku Nose al diccionario de alumnos. Su nota es de 4 y tuvo 13 inasistencias.
nuevo_alumno = {
    'nombre': 'Punku',
    'apellido': 'Nose',
    'nota': 4,
    'inasistencias': 13
}
alumnos.append(nuevo_alumno)
print(alumnos)

#Ejemplo simple de uso de diccionarios para almacenar informacion
def solicitar_datos():#Solicitar nombre y comentario al usuario
    nombre = input("¿Cuál es tu nombre? ")
    comentario = input("¿Cuál es tu comentario sobre el curso? ")
    datos = { #Almacenar los datos en un diccionario
        'Nombre': nombre,
        'Comentario': comentario
    }
    return datos
def main():
    datos_usuario = solicitar_datos() #llamar a la función para obtener los datos
    print("Datos almacenados:") #Mostrar los datos para confirmación
    for clave, valor in datos_usuario.items():
        print(f"{clave}: {valor}")
    return 'Fin'
print(main())

#diccionarios
edades = {
    'Juan': 28,
    'Maria': 26,
    'Julian': 35
}
del edades['Juan']#funcion de Python para eliminar un elemento de un diccionario
print(edades)

pelicula = {
    'titulo': 'Avatar',
    'director': 'James Cameron',
    'estreno': '2009'
}
print(pelicula['director']) #acceder a un valor de la lista
pelicula['estreno'] = 2010 #modificar un valor en base a su clave. Tambien podemos cambiar el tipo de valor, de string a integer en este caso.
print(pelicula)

pelicula['genero'] = ['Ciencia Ficcion', 'Accion', 'Drama', 'Fantasia']#agregar una clave y su valor al diccionario
print(pelicula['genero'])#se muestra el valor asociado a la clave 'genero'
print(pelicula['genero'][2])#se accede a un valor en particular asociado a la clave 'genero'

netflix = []
pelicula1 = {
    'titulo': 'Rapido y Furioso 9',
    'genero': 'Accion', 
    'estreno': 2021,
    'director': 'Justin Lin'
}
pelicula2 = {
    'titulo': 'Deadpool',
    'genero': 'Comedia', 
    'estreno': 2016,
    'director': 'Tim Miller'
}
netflix.append(pelicula1)
netflix.append(pelicula2)
print(netflix)
print(netflix[0]['titulo'])#dentro de la lista, se accede a el diccionario de una pelicula y al valor de una clave especifica.

#Crear un diccionario a partir de una lista de listas
x = [['smartphone', 4], ['Tablet', 8], ['Pc_Escritorio', 6], ['Laptop', 5]]
dispElectronicos = dict(x)
print(dispElectronicos)

#Crear un diccionario a partir de dos listas
d = ['BMW', 'Mercedes-Benz', 'Hyundai', 'Fiat', 'Jeep']
q = [4, 10, 8, 11, 3]
autos = dict(zip(d, q))
print(autos)

#Crea un diccionario que almacene datos de un producto: Nombre, Precio, Stock disponible. Modifica el precio del producto.
producto = {
    'nombre': 'Mostaza',
    'precio': 75,
    'stock disponible': 80
}
print(producto)
producto['precio'] = 82
print(producto)

#Diccionarios anidados
#Los campos tipo diccionarios en diccionarios permiten crear estructuras de datos jerarquicas. Esto es util cuando se necesita
#representar datos complejos con niveles de anidamiento.
registro = { #diccionario principal
    'usuario': { #clave usuario que contiene un diccionario como valor
        'nombre': 'Gianfranco',
        'edad': 30,
        'direccion': { #valor direccion que a su vez es una clave con otro diccionario como valor
            'calle': '18 Julio',
            'ciudad': 'Montevideo'
        }
    }
}#un diccionario principal y dos anidados.
print(registro['usuario']['direccion']['ciudad'])#se accede a un dato especifico
print(registro['usuario']['direccion'])

#Escribe un programa que almacene ciudades de Uruguay en una lista con diccionarios. El usuario debe poder ingresar un departamento 
#para ver la ciudad perteneciente al mismo.
ciudadesUy = [{
        'nombre': 'Libertad',
        'departamento': 'San Jose'
    },{
        'nombre': 'Piriapolis',
        'departamento': 'Maldonado'
    },{
        'nombre': 'Toledo',
        'departamento': 'Canelones'
    },{
        'nombre': 'La paloma',
        'departamento': 'Rocha'
    },{
        'nombre': 'Colonia del Sacramento',
        'departamento': 'Colonia'
    }]

def mostrarCiudadDept(listDict):#se listan todas las ciudades con su respectivo departamento.
    for d in listDict:
        print(f'Ciudad: {d['nombre']}, Departamento: {d['departamento']}')
    return ''
print(mostrarCiudadDept(ciudadesUy))

dept = str.capitalize(input('Ingrese un departamento para ver una de sus ciudades: '))
def consulta(departamento, listDict):#se recibe un departamento y se devuelve la ciudad perteneciente al mismo.
    for i in listDict:
        if i['departamento'] in departamento:
            print(i['nombre'])
    return ''
#Si la funcion no devuelve nada, es por que no hay registros. En caso de tener registros de los 19 departamentos, la funcion
#siempre devolvera una ciudad.
print(consulta(dept, ciudadesUy))

#Elegir 5 animales y para cada uno crear un diccionario anidado con la siguiente informacion:
#"sonido": El sonido que emite el animal.
#"genero_musical": Un género musical que te recuerde al sonido o a la personalidad del animal.
#"cancion_representativa": Una canción que asocies con ese animal o con su sonido.
#"artista": El artista de la canción representativa.
#Crea un diccionario principal llamado "playlist_animal" que contenga los 5 diccionarios anidados que creaste.
#Escribe el código para responder a las siguientes preguntas:
#¿Qué canción representativa elegiste para el "animal 3"?
#¿Qué género musical asociaste con el "animal 1"?
#Solucion 1
playlist_animal = [{
    'animal': 'leon',
    'sonido': 'sonido de leon',
    'genero_musical': 'Rock',
    'cancion_representativa': 'cancion de Rock',
    'artista': 'artista de Rock'
},{
    'animal': 'pantera',
    'sonido': 'sonido de pantera',
    'genero_musical': 'Rock Alternativo',
    'cancion_representativa': 'cancion de Rock Alternativo',
    'artista': 'artista de Rock Alternativo'
},{
    'animal': 'tigre',
    'sonido': 'sonido de tigre',
    'genero_musical': 'Power Metal',
    'cancion_representativa': 'cancion de Power Metal',
    'artista': 'artista de Power Metal'
},{
    'animal': 'aguila',
    'sonido': 'sonido de aguila',
    'genero_musical': 'musica Country',
    'cancion_representativa': 'cancion de musica Country',
    'artista': 'artista de Country'
},{
    'animal': 'liebre',
    'sonido': 'sonido de liebre',
    'genero_musical': 'musica Electronica',
    'cancion_representativa': 'cancion de musica Electronica',
    'artista': 'artista de musica Electronica'
}]
#cancion representativa para el animal 3 y genero musical para el animal 1
print(playlist_animal[2]['cancion_representativa'])
print(playlist_animal[0]['genero_musical'])

#Solucion 2
playlist_animal = {
    'leon': {
        'sonido': 'sonido de leon',
        'genero_musical': 'Rock',
        'cancion_representativa': 'cancion de Rock',
        'artista': 'artista de Rock'
    },
    'pantera': {
        'sonido': 'sonido de pantera',
        'genero_musical': 'Rock Alternativo',
        'cancion_representativa': 'cancion de Rock Alternativo',
        'artista': 'artista de Rock Alternativo'
    },
    'tigre': {
        'sonido': 'sonido de tigre',
        'genero_musical': 'Power Metal',
        'cancion_representativa': 'cancion de Power Metal',
        'artista': 'artista de Power Metal'
    },
    'aguila': {
        'sonido': 'sonido de aguila',
        'genero_musical': 'musica Country',
        'cancion_representativa': 'cancion de musica Country',
        'artista': 'artista de Country'
    },
    'liebre': {
        'sonido': 'sonido de liebre',
        'genero_musical': 'musica Electronica',
        'cancion_representativa': 'cancion de musica Electronica',
        'artista': 'artista de musica Electronica'
}}
#¿Qué canción representativa elegiste para el "animal 3"?
animales = list(playlist_animal.keys())#obtengo las claves del diccionario y las agrego a una lista
print(animales[2])#obtengo al tercer animal en el diccionario
print(playlist_animal['tigre']['cancion_representativa'])#obtengo la cancion representativa para el animal
#¿Qué género musical asociaste con el "animal 1"?
print(animales[0])#obtengo al primer animal en el diccionario
print(playlist_animal['leon']['genero_musical'])#obtengo el genero musical para el animal


#Define un diccionario llamado estudiantes donde:
#Cada clave es el nombre de un estudiante y el valor asociado es otro diccionario con las siguientes claves:
#"edad": un número entero que representa la edad del estudiante.
#"materia": el nombre de la materia que cursa.
#"calificacion": un número que representa su nota actual.
#Escribe una función llamada actualizar_calificacion (nombre_estudiante, nueva_calificacion) que:
#Verifique si el estudiante existe en el diccionario.
#Si existe, actualice su calificación.
#Si no existe, muestre un mensaje indicando que el estudiante no fue encontrado.
estudiantes = {
    'Gianfranco': {
        'edad': 19,
        'materia': 'matematica',
        'calificacion': 8
    },
    'Julian': {
        'edad': 22,
        'materia': 'biologia',
        'calificacion': 10
    },
    'Sofia': {
        'edad': 20,
        'materia': 'dibujo',
        'calificacion': 11
    }
}
print(estudiantes)#se muestra el diccionario antes de su modificacion
nombre_estudiante = str.capitalize(input('Ingrese el nombre de un estudiante: '))#los nombres deben tener mayuscula
nueva_calificacion = int(input('Ingrese la nueva calificacion: '))
def actualizar_calificacion(estudiante, nota):
    while estudiante not in estudiantes:#mientras el nombre ingresado no este en el diccionario
        print('Alumno no encontrado.')#mensaje de error, el usuario debe volver a introducir los datos
        estudiante = str.capitalize(input('Ingrese el nombre de un estudiante: '))
        nota = int(input('Ingrese la nueva calificacion: '))
    estudiantes[estudiante]['calificacion']=nota#se realiza la modificacion
    return (f'Se le ha modificado la nota a el alumno {estudiante}, su nueva nota es: {nota}.')#mensaje de salida

print(actualizar_calificacion(nombre_estudiante, nueva_calificacion))
print(estudiantes)#se muestra el diccionario modificado

#Crea un programa que gestione una lista de estudiantes donde cada estudiante esté representado por un diccionario. 
#El programa debe recorrer la lista para mostrar el nombre de todos los estudiantes, calcular el promedio de sus edades y contar
#cuantos estudiantes tienen una calificacion mayor a 70.
estudiantes = [{
    'nombre': 'Martin',
    'edad': 14,
    'calificacion': 72
},{
    'nombre': 'Fernando',
    'edad': 13,
    'calificacion': 94
},{
    'nombre': 'Mateo',
    'edad': 16,
    'calificacion': 49
},{
    'nombre': 'Jazmin',
    'edad': 19,
    'calificacion': 100
},{
    'nombre': 'Xiomara',
    'edad': 15,
    'calificacion': 85
}]

#1. Mostrar nombres de estudiantes
def nombresEstudiantes(diccionario):
    for n in diccionario:
        print(n['nombre'])

#2. Calcular promedio de sus edades
def promedioEdad(diccionario):
    edades = []
    for p in diccionario:
        edades.append(p['edad'])
    print(f'El promedio de edad de los alumnos es de: {(sum(edades) / len(edades))}.')

#3. Cantidad estudiantes con nota mayor a 70.
def alumnosAprobados(diccionario):
    contador = 0
    for a in diccionario:
        if a['calificacion'] > 70:
            contador += 1
    print(f'Los usuarios con nota mayor a 70 son {contador}.')

def principal(diccionario):
    while True:
        print('Menu de opciones')
        print('Opcion 1: Mostrar nombres de los estudiantes')
        print('Opcion 2: Mostrar el promedio de los estudiantes')
        print('Opcion 3: Mostrar la cantidad de alumnos aprobados (nota mayor a 70)')
        print('Opcion 4: Salir del programa')
        opcion = int(input('Ingrese el numero de la opcion: '))
        if opcion == 1:
            nombresEstudiantes(diccionario)
        elif opcion == 2:
            promedioEdad(diccionario)
        elif opcion == 3:
            alumnosAprobados(diccionario)
        elif opcion == 4:
            print('Saliendo del programa')
            break
        else:
            print('No se encontro la opcion')
    return ''

print(principal(estudiantes))

#Ejercicio, Control de Inventario: Crea un diccionario que represente un inventario de una tienda, donde las claves sean los nombres 
#de los productos y los valores sean las cantidades disponibles. Agrega una función que permita consultar la cantidad de un producto.
productos_tienda = {'huevos': 120, 'bizcochos': 84, 'bidon de agua': 38, 'bolsa de papas': 42, 'barritas de cereales': 88, 'comida para perro': 32}
producto = str.lower(input('Ingrese el producto al que quiere consultar disponibilidad: '))
def consultar_stock(productos):
    for p in productos.keys():
        if p == producto:
            return(productos[p])
    return 'Producto no encontrado'
print(consultar_stock(productos_tienda))
