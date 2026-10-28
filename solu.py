from stockOnus import camaraStock,fueraDeServicio

onusDePrueba = ["""22081130E7
	A devolver	2208113109	
	A devolver	220811328A"""]

def chequeaSiEstan(stock,pendientes): #chequea si están o no. Devuelve las que están
    for pendiente in pendientes:
        for st in stock:
            if pendiente == st:
                print(pendiente)

onuPrueba=["""220811628A (no la trajeron)
22081164E7 (no la trajeron)"""]

def separaCadaElemento(texto): #Primer Funcion
    numeros =[1,2,3,4,5,6,7,8,9,0]
    numerosTexto= ["1","2","3","4","5","6","7","8","9","0"]
    letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    onusSinTexto = []
    for parrafo in texto:
        for caracter in parrafo:
            if caracter in numeros or caracter in numerosTexto or caracter in letras:
                onusSinTexto.append(caracter)
    return onusSinTexto
#LetrasYNumerosSeparados = separaCadaElemento(o)

def eliminaLetras(texto): #Segunda funcion
    listaConSoloNumeros = []

    while len(texto) != 0:
        contador = 0
        primerElemento = texto[0]
        if primerElemento == "2": 
            while contador != 10:
                listaConSoloNumeros.append(texto[0])
                texto.remove(texto[0])
                contador+=1
        else:
            texto.remove(texto[0])
    return listaConSoloNumeros
#soloNumerosPegados= eliminaLetras(letrasYNumerosSeparados)

def separaOnus(todasLasOnus): #Tercera funcion
    nuevaLista= []
    while len(todasLasOnus) != 0:
        if todasLasOnus[0] == "2":
            nuevaLista.append(todasLasOnus[0]+todasLasOnus[1]+todasLasOnus[2]+todasLasOnus[3]+todasLasOnus[4]+todasLasOnus[5]+todasLasOnus[6]+todasLasOnus[7]+todasLasOnus[8]+todasLasOnus[9])#agrego el primer elemento si empieza con 2
            todasLasOnus.remove(todasLasOnus[0]) #elimino ese primer elemento
            todasLasOnus.remove(todasLasOnus[0]) #elimino ese primer elemento
            todasLasOnus.remove(todasLasOnus[0])
            todasLasOnus.remove(todasLasOnus[0])
            todasLasOnus.remove(todasLasOnus[0])
            todasLasOnus.remove(todasLasOnus[0])
            todasLasOnus.remove(todasLasOnus[0])
            todasLasOnus.remove(todasLasOnus[0])
            todasLasOnus.remove(todasLasOnus[0])
            todasLasOnus.remove(todasLasOnus[0])
    return  nuevaLista
#separadas = separaOnus(soloNumerosPegados)

def final(prueba):
    return separaOnus((eliminaLetras(separaCadaElemento(prueba))))

res = final(onus2)

estaEnCamaras = chequeaSiEstan(listaCamaras,res)



