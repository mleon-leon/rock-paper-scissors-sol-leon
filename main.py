import random

# Opciones disponibles en el juego
OPTIONS = ["piedra", "papel", "tijera"]
POINTS_TO_WIN = 2


def get_player_choice():
    """Solicita y valida la elección del jugador."""
    player_choice = input("Elige piedra, papel o tijera: ").lower()

    while player_choice not in OPTIONS:
        print("Opción no válida. Intenta nuevamente.")
        player_choice = input("Elige piedra, papel o tijera: ").lower()

    return player_choice


def get_computer_choice():
    """Genera una elección aleatoria para la computadora."""
    return random.choice(OPTIONS)


def get_round_winner(player_choice, computer_choice):
    """Determina quién ganó una ronda."""
    if player_choice == computer_choice:
        return "empate"

    player_wins = (
        (player_choice == "piedra" and computer_choice == "tijera")
        or (player_choice == "papel" and computer_choice == "piedra")
        or (player_choice == "tijera" and computer_choice == "papel")
    )

    if player_wins:
        return "jugador"

    return "computadora"


def play_game():
    """Ejecuta una partida: gana quien llegue primero a 2 puntos."""
    player_score = 0
    computer_score = 0

    print("\n=== PIEDRA, PAPEL O TIJERA ===")
    print("Regla: gana quien consiga 2 puntos primero.\n")

    # Repite rondas hasta que alguien consiga 2 puntos
    while player_score < POINTS_TO_WIN and computer_score < POINTS_TO_WIN:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        winner = get_round_winner(player_choice, computer_choice)

        print("\n--- RESULTADO DE LA RONDA ---")
        print(f"Tu elección: {player_choice}")
        print(f"Elección de la computadora: {computer_choice}")

        if winner == "empate":
            print("Empate. No se asignan puntos.")
        elif winner == "jugador":
            player_score += 1
            print("¡Ganaste esta ronda!")
        else:
            computer_score += 1
            print("La computadora ganó esta ronda.")

        print(f"\nMarcador: Usuario {player_score} - Computadora {computer_score}\n")

    print("=== RESULTADO FINAL ===")

    if player_score == POINTS_TO_WIN:
        print("¡Felicidades! Ganaste el juego.")
    else:
        print("La computadora ganó el juego.")


def play_again():
    """Pregunta al jugador si desea iniciar otra partida."""
    answer = input("\n¿Deseas jugar otra partida? (si/no): ").lower()

    while answer not in ["si", "no"]:
        print("Respuesta no válida. Escribe si o no.")
        answer = input("¿Deseas jugar otra partida? (si/no): ").lower()

    return answer == "si"


# Bucle principal: permite iniciar varias partidas
continue_playing = True

while continue_playing:
    play_game()
    continue_playing = play_again()

print("\nGracias por jugar. ¡Hasta pronto!")