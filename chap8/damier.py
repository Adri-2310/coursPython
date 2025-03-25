__author__ = "Adrien Mertens"
__version__ = "1.0"


def delete_pawn_position(board) -> None:
    # Iterate over the board to find the pawn "X" and replace it with "0"
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                board[i][j] = "0"
                return


def update_pawn_position(board, new_x: int, new_y: int) -> None:
    # Update the board with the new pawn position
    board[new_y][new_x] = "X"


def display_board(board) -> None:
    # Display the board in reverse order
    for row in reversed(board):
        print(row)


def select_move_position(old_x: int, old_y: int) -> tuple:
    # Prompt the user to select a move direction
    response = 0
    while response not in (7, 9, 1, 3):
        response = int(
            input(
                "Veuillez choisir la direction (7 pour en haut à gauche, 9 pour en haut à droite, 1 pour en bas à gauche et 3 pour en bas à droite): "
            )
        )

    match response:
        case 7:
            old_x -= 1
            old_y += 1
        case 9:
            old_x += 1
            old_y += 1
        case 1:
            old_x -= 1
            old_y -= 1
        case 3:
            old_x += 1
            old_y -= 1

    return old_x, old_y


def checkerboard() -> None:
    # Initialize the 8x8 board with "0"
    board = [["0" for _ in range(8)] for _ in range(8)]
    display_board(board)
    position_x = -1
    position_y = -1
    game_over = True

    # Prompt for the starting position and check if it is valid
    while not (0 <= position_x < 8 and 0 <= position_y < 8):
        position_x = int(input("Sur quelle case voulez-vous être (1-8) ? ")) - 1
        position_y = int(input("Sur quelle ligne voulez-vous être (1-8) ? ")) - 1

    # Initialize the board with the starting position
    update_pawn_position(board, position_x, position_y)
    display_board(board)

    # Prompt for the move direction
    while game_over:
        position_x, position_y = select_move_position(position_x, position_y)
        delete_pawn_position(board)
        if 0 <= position_x < 8 and 0 <= position_y < 8:
            update_pawn_position(board, position_x, position_y)
            display_board(board)
        else:
            game_over = False

    print("Vous êtes sorti du damier (THE END)")


if __name__ == "__main__":
    checkerboard()
