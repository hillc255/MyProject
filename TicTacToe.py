# Title: TicTacToe Game
# Date:  12/30/2019
# Purpose:  Create TicTacToe Game with Python
# Description:  2 players should be able to play the game
# (both sitting at the same computer)
# The board should be printed out every time a player makes a move
# You should be able to accept input of the player position and
# then place a symbol on the board

class TicTacToe:


    def board(self):
        print(f"\n  {result[0]}  |  {result[1]}  |  {result[2]}   \n_____|_____|_____\n  {result[3]}  |  {result[4]}  |  {result[5]}   \n_____|_____|_____\n  {result[6]}  |  {result[7]}  |  {result[8]}   \n     |     |     \n")

    def playerX(self):
        temp = result.copy()
        print(f"This is temp - same as result:  {temp}")

        #list comprehension
        xloc = [i for i, d in enumerate(temp) if d == 'X']
        print(f"This is xloc pattern:  {xloc}")

        xlocthree = xloc[-3:]
        print(f"This is xloc 3 pattern:  {xlocthree}")

        if all(x in wins for x in xlocthree):
                print(f"Player {player} wins!")
                quit()
        else:
            pass


    def player0(self):
        temp2 = result.copy()
        print(f"This is temp - same as result:  {temp2}")

        # list comprehension
        oloc = [i for i, d in enumerate(temp2) if d == '0']
        print(f"This is oloc pattern:  {oloc}")

        if all(x in wins for x in oloc):
            print(f"Player {player} wins!")
            quit()
        else:
            pass


if __name__ == '__main__':

    my_tictactoe = TicTacToe()
    print("\nWelcome TicTacToe players!\n")
    count = 0
    loc = 0
    q = True
    tiles = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    temp = []
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    #print the initial board
    my_tictactoe.board()

    while q:
        # Alternate between players using odd and even number
        if count%2 == 0:
            player = "X"
        else:
            player = "0"

        # Player selects available tile
        action = input(f"Player {player}, select a numbered tile: ")
        while not action:
            action = input(f"Player {player}, select a numbered tile: ")
        if action not in tiles:
            print("That number is not available")
            continue
        else:
            count += 1
            tiles.remove(action)
            #print(tiles)

            # Display selected tiles on board
            loc = int(action)
            for n, i in enumerate(result):
                if i == loc:
                    result[n] = player
                    #print(result)

                    # Display board
                    my_tictactoe.board()
                    if count > 4:

                    # Check for winning list
                       if player == "X":
                           my_tictactoe.playerX()
                       else:
                           my_tictactoe.player0()

                       #print(f"This is player {player}")
                       #print(f"This is result {result}")

                    # Make sure all tiles are used
                    if count >= 9:
                        print("Game over - Draw!")
                        q = False




