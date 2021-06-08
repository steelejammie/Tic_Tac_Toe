# Tic Tac Toe Final Project
# IS-201 Fundamentals of Computing
# Jammie Steele, Henok Mekonnen, Chirstian Morris
# June 10 2021

import sys

# Set global variables. List for the board, variables to represent players
board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "] # This list is the actual game board. All moves will be stored here and the program uses this list to create a visual representation of the game board
print("Enter the names of the two players-")
first_player = input("\nEnter the name of first player: \n")
second_player = input("\nEnter the name of the second player: \n")


def game_board(board):
    """Creates a visual representation of the game board. Uses acsii characters and index slices from the board list
    to draw a tic tac toe board"""
    print(board[7] + " |" + board[8] + " |" + board[9])
    print("--+--+--")
    print(board[4] + " |" + board[5] + " |" + board[6])
    print("--+--+--")
    print(board[1] + " |" + board[2] + " |" + board[3])


def welcome_screen():
    """Welcomes the player to the game and presents the instructions"""
    print("""Welcome to Tic Tac Toe presented by Team X!!
Instuctions: Player 1 is X and player 2 is O.
The first player to get their mark in three places in a row wins the game.
The spaces in the game board correspond to the number keys in the following way.
 7 | 8 | 9
 --+---+--
 4 | 5 | 6
 --+---+--
 1 | 2 | 3
 Select the number to place your mark in the space you want""")
    input("Press enter to begin the game.") # Pauses code so user can read instructions


def win_the_game(turn):
    """Message informing the players of the game winner. Will look at the last move made and print message to screen
    containing appropriate players name"""
    game_board(board)
    print("Winner, Winner, Chicken Dinner")
    if turn == "X":
        print("Congratulations " + first_player + " is the winner!!")
    else:
        print("Congratulations " + second_player + " is the winner!!")


def play():
    """Main game logic. Brings everything together to allow game play."""

    welcome_screen()

    # Local variables that will be used throughout the play() function. Sets the first turn and player.
    # Informs players who is first and who is second. Also sets file name to save move list in.
    turn = "X"
    count = 0
    active_player = first_player
    print(first_player + " is X")
    print(second_player + " is O")
    move_list = "tictactoe.txt"


    # Logic to take players move. Asks player to enter a number between 1 and 9.
    for space in range(10):
        game_board(board)
        print(active_player + " Select a space using 1 - 9: ")
        move = int(eval(input()))
        # Code to check if the move is valid. If the user selects a number out of range or that is already
        # used an error message will print and ask the user to try again
        if not 1 <= move <= 9:
            print("Invalid input. Select a number between 1-9")

        elif board[move] == " ":
            board[move] = turn
            count += 1

        else:
            print("\nThat space has been taken.\n")
            print("\nSelect an open spot.\n")
            continue

        # Logic to determine a winner. To increase efficiency will only check after five moves. If any of these spaces are
        # filled at the same time the player who made the last move will be declared the winner. Checks all the possible
        # winning combinations
        if count >= 5:
            if board[7] == board[8] == board[9] != " ":  # top win
                win_the_game(turn)
                break
            elif board[4] == board[5] == board[6] != " ":  # middle win
                win_the_game(turn)
                break
            elif board[1] == board[2] == board[3] != " ":  # bottom win
                win_the_game(turn)
                break
            elif board[1] == board[4] == board[7] != " ":  # left side win
                win_the_game(turn)
                break
            elif board[2] == board[5] == board[8] != " ":  # down the center win
                win_the_game(turn)
                break
            elif board[3] == board[6] == board[9] != " ":  # right side win
                win_the_game(turn)
                break
            elif board[7] == board[5] == board[3] != " ":  # diagonal top left to bottom right win
                win_the_game(turn)
                break
            elif board[1] == board[5] == board[9] != " ":  # diagonal bottom left to top right win
                win_the_game(turn)
                break

        # Logic to determine if there is a tie. If all spaces are full and none of the winning conditions are met the
        # game will be declared a tie. Will record moves to external file
        if count == 9:
            print("\nThe board is full.\nThe game is a tie.")
            with open(move_list, 'a') as p_moves:
                p_moves.write("\n123456789\n")
                for selection in board:
                    p_moves.write(selection)

                print("\nMoves saved to tictactoe.txt\n")

            p_moves.close()

            # Ask players if they want to play again. If y is entered board is cleared and a new game started.
            # If not the program closes.
            replay = input("\nPlay another game? (y/n): ")
            if replay == "y" or replay == "Y":
                for spot in board:
                    board[board.index(spot)] = " "
                play()
            else:
                print("Thanks for playing")
                exit()

        # Logic to change players turn. Looks at the current player and switches to the other player.
        # Does this by reassigning the active_player variable.
        if turn == "X":
            turn = "O"
            active_player = second_player
        else:
            turn = "X"
            active_player = first_player
    # Records the moves each player made to external file assigned to move_list variable
    with open(move_list, 'a') as p_moves:
        p_moves.write("123456789\n")
        for selection in board:
            p_moves.write(selection)

        print("\nMoves saved to tictactoe.txt\n")

    p_moves.close()

    # Ask players if they want to play again
    # Ask players if they want to play again. If y is entered board is cleared and a new game started.
    # If not the program closes.
    replay = input("\nPlay another game? (y/n): ")
    if replay == "y" or replay == "Y":
        for spot in board:
            board[board.index(spot)] = " "
        play()

    else:
        print("Thanks for playing")
        exit()

# Initializes the program
if __name__ == "__main__":
    play()
