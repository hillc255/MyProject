# Title:        TicTacToe Game
# Date:         12/30/2019
# Author:       Claudia Hill
# Purpose:      Create TicTacToe Game with Python
#               Milestone 1 - Udemy Python Bootcamp
#               My first Python program (IDE PyCharm)
# Assignment Description:
# 1. Two players should be able to play the game
# (both sitting at the same computer)
# 2. The board should be printed out every time a player makes a move
# 3. You should be able to accept input of the player position and
# 4. then place a symbol on the board

class TicTacToe:

    def board(self):
        print(f"\n  {result[0]}  |  {result[1]}  |  {result[2]}   \n_____|_____|_____\n  {result[3]}  |  {result[4]}  |  {result[5]}   \n_____|_____|_____\n  {result[6]}  |  {result[7]}  |  {result[8]}   \n     |     |     \n")

    def playercheckwin(self):
        temp = result.copy()
        # list comprehension - print pattern x
        if player == 'X':
            xindex = [i for i, d in enumerate(temp) if d == 'X']
            playpattern = xindex
        else:
            oindex = [i for i, d in enumerate(temp) if d == '0']
            playpattern = oindex

        # Check all elements in winning plays with playerX moves
        for i in range(0, 8):
            winsublist = wins[i]
            if all(elem in playpattern for elem in winsublist):
                print(f"Player {player} wins!")
                quit()
        # No winning play continue game
        else:
            return

if __name__ == '__main__':

    my_tictactoe = TicTacToe()
    print("\nWelcome TicTacToe players!\n")
    count = 0
    loc = 0
    q = True
    tiles = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    temp, playpattern, winsublist = [],[],[]
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    #Display initial board
    my_tictactoe.board()

    #Loop for the gamee
    while q:
        # Alternate between players using odd and even number
        if count % 2 == 0:
            player = "X"
        else:
            player = "0"

        # Player inputs available tile
        action = input(f"Player {player}, select a numbered tile: ")
        while not action:
            action = input(f"Player {player}, select a numbered tile: ")
        if action not in tiles:
            print("Invalid input, try again: ")
            continue
        else:
            count += 1
            tiles.remove(action)

            # Display selected tiles on board
            loc = int(action)
            for n, i in enumerate(result):
                if i == loc:
                    result[n] = player

                    # Display board
                    my_tictactoe.board()

                    # Check for winning play
                    if count > 4:
                        my_tictactoe.playercheckwin()

                    # Make sure all tiles are used
                    if count >= 9:
                        print("Game over - Draw!")
                        q = False




