# Comandos b´asicos de pilas:
# from queue import LifoQueue as Pila
# p: Pila[T] = Pila()
# #crear pila de tipo T

# p.put(elem) # apilar elemento

# p.get() # desapilar

# elemento: T = p.get() #guardar elemento desapilado

# p.empty() # preguntar si esta vacia (True o False)

import random
from queue import LifoQueue as pila
from queue import Queue as cola

#1 Pilas
#1.1
def generar_nros_al_azar(cantidad:int , desde:int, hasta:int):
    p = pila()
    i = 0
    while i < cantidad:
        num = random.randint(desde, hasta)
        p.put(num)
        i += 1
    print (p.queue)
    return p

def generar_nros_al_azar2(cantidad: int, desde: int, hasta: int) -> pila[int]:
    p: pila = pila()  # creo una pila vacia

    for k in range(cantidad):  # range(cantidad) = range(0, cantidad)
        n: int = random.randint(desde, hasta)
        p.put(n)
    return p

def mostrar_pila(p: pila[int])->pila[int]:
    nueva_p:pila[int]=pila()#creo la pila
    pila_auxiliar:pila[int]=pila()#Creo otra pila
    while not p.empty(): #se repite hasta que la pila esté vacía
        elemento:int=p.get() #saco el ultimo elemento de la pila p y se la asigno a la variable elemento
        print(elemento) #lo muestro
        pila_auxiliar.put(elemento) #ese elemento se lo agrego a mi nueva pila auxiliar

    while not pila_auxiliar.empty():
        elemento2:int=pila_auxiliar.get() #desapilo la nueva funcion auxiliar para dejarla como la original
        p.put(elemento) #dejo la pila p como estaba
        nueva_p.put(elemento2) #creo una copia exacta de p 

#resultado = mostrar_pila(p) muestro elementos 

# Ejercicio 2. Implementar una solucion para el siguiente problema.
# problema cantidad_elementos (in p: Pila) : Z {requiere: {True}
#                               asegura: {res es igual a la cantidad de elementos que contiene p}}
def cantidadElementos(p:pila[int])->int:
    contador = 0
    while not p.empty():
        p.get()
        contador +=1
    return contador

#elementos = cantidadElementos(p)
#print(elementos) muestro cantidad de elementos

# Ejercicio 3. Implementar una soluci´on para el siguiente problema.
# problema buscar_el_maximo (in p: Pila[Z]) : Z {
#                     requiere: {p no esta vacıa}
#                     asegura: {res es un elemento de p}
#                     asegura: {res es mayor o igual a todos los elementos de p}}
def buscar_maximo(p:pila[int])->int:
    elemento:int=p.get() #saco el tope de la pila
    pilaAux:pila[int]=pila() #creo una pila auxiliar para guardar lo que saco de la original
    pilaAux.put(elemento) # agrego lo que saqué de la original
    
    while not p.empty():
        ultimoElemento:int=p.get()
        pilaAux.put(ultimoElemento)
        if elemento <= ultimoElemento:
            elemento = ultimoElemento
    
    while not pilaAux.empty():
        ele:int=pilaAux.get()
        p.put(ele)
    return elemento

# Creamos la pila y cargamos datos
p:pila[int] = pila()
p.put(1)
p.put(2)
p.put(3)
p.put(7)
p.put(10)
p.put(8)
# Probamos la función
maxElemento = buscar_maximo(p)
#print(maxElemento) descomentar para imprimir la funcion

# Ejercicio 4. Implementar una soluci´on para el siguiente problema.
# problema buscar_nota_maxima (in p: Pila[seq⟨Char⟩×Z]) : seq⟨Char⟩ ×Z {
#         requiere: {p no est´a vac´ıa}
#         requiere: {los elementos de p no tienen valores repetidos en la segunda posici´on de las tuplas}
#         asegura: {res es una tupla de p}
#         asegura: {No hay ning´un elemento en p cuya segunda componente sea mayor que la segunda componente de res }
def buscarNotaMaxima(p:pila[tuple[str,int]])-> tuple[str,int]:
    copiaPila:pila[tuple[str,int]]=pila()
    elemento:int=p.get()
    while not p.empty():
        nuevo_elemento:int=p.get()
        if elemento[1] <= nuevo_elemento[1]:
            elemento = nuevo_elemento
    return elemento
    
pi = pila()
pi.put(["mati",7])
pi.put(["vale",9])
pi.put(["eze",8])
pi.put(["sofi",10])

n = buscarNotaMaxima(pi)
# print(n) # descomentar para imprimir
