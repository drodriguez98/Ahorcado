#   https://www.youtube.com/watch?v=tWnyBD2src0

import random 
import string

from palabras import palabras
from diagramas import vidas_diccionario_visual


def obtener_palabra_valida(lista_palabras):

    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:

        palabra = random.choice(palabras)
    
    return palabra.upper()


def main():

    print ("=================================")
    print ("Bienvenido al juego del ahorcado")
    print ("=================================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:

        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]

        print(vidas_diccionario_visual[vidas])

        print (f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:

            letras_adivinadas.add(letra_usuario)

            if letra_usuario in letras_por_adivinar:

                letras_por_adivinar.remove(letra_usuario)
                print('')
            
            else: 

                vidas = vidas - 1
                print(f"\n La letra {letra_usuario} no está en la palabra.")
        
        elif letra_usuario in letras_adivinadas:

            print("\n Ya escogiste esta letra. Por favor, introduce una nueva.")

        else:

            print("\n Esta letra no es válida.")

    if vidas == 0:

        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado! La palabra era {palabra}")

    else:

        print(f" Enhorabuena! Adivinaste la palabra.")

main()


