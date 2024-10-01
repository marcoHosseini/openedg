from random import randrange


# Funktion, um das Spielfeld anzuzeigen
def display_board(board):
    def draw_horizontal():
        print("+-------+-------+-------+")

    def draw_row(row):
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")

    draw_horizontal()
    draw_row(0)  # Zeichnet die erste Reihe
    draw_horizontal()
    draw_row(1)  # Zeichnet die zweite Reihe
    draw_horizontal()
    draw_row(2)  # Zeichnet die dritte Reihe
    draw_horizontal()


# Funktion, um den Zug des Benutzers zu verarbeiten
def enter_move(board):
    while True:
        try:
            move = int(input("Enter a number between 1 and 9: "))
            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] not in ['X', 'O']:
                board[row][col] = 'O'
                break
            else:
                print("Field is already occupied. Choose a different field.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 9.")


# Funktion, um alle freien Felder zu finden
def make_list_of_free_fields(board):
    free_fields = []  # Liste, um die freien Felder zu speichern

    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))

    return free_fields


# Funktion, um zu überprüfen, ob jemand gewonnen hat
def victory_for(board, sign):
    # Zeilen überprüfen
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return f"{sign} wins!"

    # Spalten überprüfen
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return f"{sign} wins!"

    # Diagonalen überprüfen
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return f"{sign} wins!"
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return f"{sign} wins!"

    # Überprüfen, ob es noch freie Felder gibt
    if make_list_of_free_fields(board):
        return "The game continues."

    return "It's a tie!"


# Funktion, um den Zug des Computers zu verarbeiten
def draw_move(board):
    if board[1][1] not in ['X', 'O']:  # Computer fängt immer mit der Mitte an
        board[1][1] = 'X'
    else:
        free_fields = make_list_of_free_fields(board)
        if free_fields:
            random_index = randrange(len(free_fields))
            row, col = free_fields[random_index]
            board[row][col] = 'X'
        else:
            print("No more free fields. The game should be over.")


# Hauptspielfunktion
def play_game():
    # Initiales Spielfeld
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Der Computer beginnt mit dem ersten Zug
    draw_move(board)
    display_board(board)

    # Spielschleife: Abwechselnd Benutzer und Computer, bis das Spiel endet
    while True:
        # Benutzerzug
        enter_move(board)
        display_board(board)
        result = victory_for(board, 'O')
        if result != "The game continues.":
            print(result)
            break

        # Computerzug
        draw_move(board)
        display_board(board)
        result = victory_for(board, 'X')
        if result != "The game continues.":
            print(result)
            break


# Spiel starten
play_game()
