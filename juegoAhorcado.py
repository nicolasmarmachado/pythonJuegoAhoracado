import random

def obtenerPalabras() -> str: 
    palabras = ['Python','Java','JavaScript','Django','Git']
    return random.choice(palabras).lower()

def mostrarProgreso(palabraSecreta, letrasUsadas):
    adivinado= ''

    for letra in palabraSecreta:
        if letra in letrasUsadas:
            adivinado += letra
        else:
            adivinado += '_'
    return adivinado

def juegoAhorcado():
    palabraSecreta = obtenerPalabras()
    letrasUsadas = []
    intentos = 8
    juegoTerminado = False
    print('Bienvenido al juego del Ahorcado')
    print(f'Tenés {intentos} intentos para adivinar')
    print(mostrarProgreso(palabraSecreta, letrasUsadas))

    while not juegoTerminado and intentos > 0:
        letra = input('Introduce una letra: ').lower()
        if  len(letra)!=1 or not letra.isalpha(): #validaciones
            print('Escribir una sola letra')
        elif letra in letrasUsadas: #validaciones
            print('ya has usado esa letra')
        else:
            letrasUsadas.append(letra) #controla la letra

            if letra in palabraSecreta:
                print(f'Has acertado, la letra {letra} está presente en la palabra')
            else:
                intentos-=1
                print(f'Lo siento, la letra {letra} no está presente en la palabra. Te quedan {intentos} intentos.')
        progresoActual= mostrarProgreso(palabraSecreta, letrasUsadas)
        print(progresoActual)
        
        if '_' not in progresoActual:
            juegoTerminado = True
            print(f'Has ganado! la palabra secreta es {palabraSecreta}')
            
    if intentos == 0:
        print(f'Lo sentimos mucho, no tenés más intentos. La palabra secreta era {palabraSecreta}')

juegoAhorcado()