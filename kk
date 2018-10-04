# kółko i krzyżyk
# komputer gra w kółko i krzyżyk przeciwko człowiekowi

# stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    """Wyświetl instrukcję gry."""
    print(
    """
    Witaj w największym intelektualnym wyzwaniu wszech czasów, jakim jest
    gra 'Kółko i krzyżyk'. Będzie to ostateczna rozgrywka między Twoim ludzkim
    mózkiem, a moim krzemowym procesorem.

    Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
    Liczba ta odpowiada pozyzji na p;anszy zgodnie z poniższym schematem:

            0 | 1 | 2
            ---------
            3 | 4 | 5
            ---------
            6 | 7 | 8

    Przygotuj się, Człowieku. Ostateczna batalia niebawem się rozpocznie.\n
    """
    )

def ask_yes_no(question):
    """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
    respone = None
    while respone not in("t", "n"):
        respone = input(question).lower()
    return respone

def pieces():
    """Ustal, czy pierwszy ruch należy do gracza, czy do komputera."""
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? (t/n): ")
    if go_first == "t":
        print("\nWięc pierwszy ruch należy do Ciebie. Będzie Ci potrzebny.")
        human = X
        computer = 0
    else:
        print("\nTwoja odwaga Cię zgubi... Ja wykonuję pierwszy ruch.")
        computer = X
        human = 0
    return computer, human

def new_board():
    """Utwórz nową plansze gry."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Wyświetl planszę gry na ekranie."""
    print("\n\t", board [0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    """Utwórz listę prawidłowych ruchów."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
        return moves

def winner(board):
    """Ustal zwycięzcę gry."""
    WAY_TO_WIN = ((0, 1, 2),
                  (3, 4, 5),
                  (6, 7, 8),
                  (0, 3, 6),
                  (1, 4, 7),
                  (2, 5, 8),
                  (0, 4, 8),
                  (2, 4, 6))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    """Odczytaj ruch człowieka."""
    legal = lega_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Jaki będzie Twój ruch (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nTo pole jest już zajęte, niemądry Człowieku. Wybierz inne.\n")
    print("Znakomicie....")
    return move
    
