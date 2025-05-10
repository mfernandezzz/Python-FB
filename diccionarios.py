#Los diccionarios son otra forma de guardar elementos. Son parecidos a las listas, pero con la diferencia de que
#contienen informacion vinculada con otra y que a dterminada informacion se accede a traves de su respectiva clave. 
#Junto con las listas, se los conoce como estructuras de datos. Cada una tiene una utilidad especial, cada una sera 
#mas util que otra dependiendo de la tarea a resolver. Hay muchas estructuras de datos diferentes aunque listas y 
#diccionarios son las mas utilizadas.

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
#cuyas claves estaran dadas por l1 y los valores respectivos estaran dados por l2. l1 y l2 tendran la misma cantidad de valores.
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

#Crea una funcion eliminate_key(d, valor) que reciba un diccionario y una clave. Se debe eliminar la clave del diccionario que
#y devolver el diccionario modificado. Utilizar la funcion pop(valor) que poseen los objetos de tipo diccionario.
d = {'Pedro': 34, 'Xavi': 24, 'Tom': 39}
key = 'Pedro'
def eliminarclave(d, key):
  if key in d:
    d.pop(key)
    return d
print(eliminarclave(d, key))


#Listas que contienen diccionarios
#Los diccionarios como los vistos hasta ahora pueden combinarse con las listas, lo que dara como resultado una lista que 
#contiene diccionarios. Esto nos permite manejar bloques de datos, donde cada bloque de datos es un diccionario contenido
#dentro de una lista.
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

#Modificá la nota de Juan a 12 usando su apellido con el fin de diferenciarlo de otros alumnos que tambien se puedan
#llamar Juan.
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
