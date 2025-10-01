import random

def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res
def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")    
    return eleccion_usuario
def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijeras" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"
def jugar():
    print("¡Bienvenido a Piedra, Papel o Tijeras!")
    puntuacion_usuario=0
    puntuacion_ordenador=0
    while puntuacion_usuario < 3 and puntuacion_ordenador < 3:
        eleccion = usuario_decide_jugada()
        while eleccion not in ["piedra", "papel", "tijeras"]:
            print("Elección no válida. Por favor, elige piedra, papel o tijeras.")
            eleccion = usuario_decide_jugada()
        print("El usuario eligió:", eleccion)
        print()
        eleccion1 = ordenador_decide_jugada()
        print("El ordenador eligió:", eleccion1)
        print()
        if eleccion == eleccion1:
            print("Empate")
        elif eleccion == "tijeras" and eleccion1 == "papel":
            puntuacion_usuario += 1
            print("El usuario gana esta ronda")
        elif eleccion == "papel" and eleccion1 == "piedra":
            puntuacion_usuario += 1
            print("El usuario gana esta ronda")
        elif eleccion == "piedra" and eleccion1 == "tijeras":
            puntuacion_usuario += 1
            print("El usuario gana esta ronda")
        else:
            puntuacion_ordenador += 1
            print("El ordenador gana esta ronda")
        print("La puntuacion del usuario es:", puntuacion_usuario, "y la del ordenador es:", puntuacion_ordenador)
    if puntuacion_usuario == 3:
        print("El usuario gana la partida")
    elif puntuacion_ordenador == 3:
        print("El ordenador gana la partida")