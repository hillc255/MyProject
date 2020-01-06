import random

# Title:        TicTacToe Game - Solution Given
# Date:         1/1/2020
# Author:       Udemy Python Bootcamp
# Purpose:      Create TicTacToe Game with Python
#               Milestone 1 - Udemy Python Bootcamp
# Description:  Original solution in Jupiter Notebooks - adapted to this IDE

class SolutionTicTacToe:

    print('Welcome to Tic Tac Toe!')


    def display_board(self,board):
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def player_input(self):
        marker = ''
        while not (marker == 'X' or marker == 'O'):
            marker = input('Player 1: Do you want to be X or O? ').upper()
        if marker == 'X':
            return ('X', 'O')
        else:
            return ('O', 'X')

    def place_marker(self,board, marker, position):
        board[position] = marker

    def win_check(self,board, mark):
        return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
                (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
                (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
                (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
                (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
                (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
                (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
                (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

    def choose_first(self):
        if random.randint(0, 1) == 0:
            return 'Player 2'
        else:
            return 'Player 1'

    def space_check(self, board, position):
        return board[position] == ' '

    def full_board_check(self,board):
        for i in range(1, 10):
            if self.space_check(board, i):
                return False
        return True

    def player_choice(self,board):
        position = 0
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not self.space_check(board, position):
            position = int(input('Choose your next position: (1-9) '))
        return position

    def replay(self):
        return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

if __name__ == "__main__":

    my_tictactoe = SolutionTicTacToe()

    while True:
        # Reset the board
        theBoard = [' '] * 10
        player1_marker, player2_marker = my_tictactoe.player_input()
        turn = my_tictactoe.choose_first()
        print(turn + ' will go first.')

        play_game = input('Are you ready to play? Enter Yes or No.')

        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                # Player1's turn.
                my_tictactoe.display_board(theBoard)
                position = my_tictactoe.player_choice(theBoard)
                my_tictactoe.place_marker(theBoard, player1_marker, position)

                if my_tictactoe.win_check(theBoard, player1_marker):
                    my_tictactoe.display_board(theBoard)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if my_tictactoe.full_board_check(theBoard):
                        my_tictactoe.display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player2's turn.
                my_tictactoe.display_board(theBoard)
                position = my_tictactoe.player_choice(theBoard)
                my_tictactoe.place_marker(theBoard, player2_marker, position)

                if my_tictactoe.win_check(theBoard, player2_marker):
                    my_tictactoe.display_board(theBoard)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if my_tictactoe.full_board_check(theBoard):
                        my_tictactoe.display_board(theBoard)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'

        if not my_tictactoe.replay():
            break