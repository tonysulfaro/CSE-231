########################################################################################
#   Project 11 - Gomoku
#
#
#
#
#
#
#
#
#
########################################################################################

import numpy as np

class GoPiece(object):

    def __init__(self, color='black'):
        self.__color = color
        if self.__color != 'black' and self.__color != 'white':
            raise MyError('Wrong color.')

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.__color == 'black':
            return ' ● '
        elif self.__color == 'white':
            return ' ○ '

    def get_color(self):
        return self.__color


class MyError(Exception):

    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return self.__value


class Gomoku(object):

    def __init__(self, board_size=15, win_count=5, current_player='black'):


        self.__board_size = board_size
        self.__win_count = win_count
        self.__current_player = current_player


        if type(self.__board_size) != int:
            raise ValueError('Board is not an integer')
        if type(self.__win_count) != int:
            raise ValueError('Win count is not an integer')

        self.__go_board = [[' - ' for j in range(self.__board_size)] for i in range(self.__board_size)]
        # if self.__current_player != 'black' or self.__current_player != 'white' or self.__current_player != '-':
        #   raise MyError('Wrong color.')

    def assign_piece(self, piece, row, col):
        if row > self.__board_size or col > self.__board_size:
            raise MyError('Invalid position.')
        elif self.__go_board[row - 1][col - 1] != ' - ':
            raise MyError('Position is occupied.')
        else:
            self.__go_board[row - 1][col - 1] = piece

    def get_current_player(self):
        return self.__current_player

    def switch_current_player(self):
        if self.__current_player == 'black':
            self.__current_player = 'white'
        else:
            self.__current_player = 'black'

    def __str__(self):
        s = '\n'
        for i, row in enumerate(self.__go_board):
            s += "{:>3d}|".format(i + 1)
            for item in row:
                s += str(item)
            s += "\n"
        line = "___" * self.__board_size
        s += "    " + line + "\n"
        s += "    "
        for i in range(1, self.__board_size + 1):
            s += "{:>3d}".format(i)
        s += "\n"
        s += 'Current player: ' + ('●' if self.__current_player == 'black' else '○')
        return s

    def current_player_is_winner(self):

        # iterate over the board horizontally
        for row in self.__go_board:
            horizontal_count = 0

            for item in row:

                # this is a board piece item and current_player should be same type
                item = str(item)
                current_player = str(' ● ' if self.__current_player == 'black' else ' ○ ')
                other_player = str(' ○ ' if self.__current_player == 'black' else ' ● ')

                if item == current_player:
                    horizontal_count += 1
                    if horizontal_count == self.__win_count:
                        return True
                else:
                    horizontal_count = 0

        # iterate over board vertically
        for x in range(self.__board_size):
            vertical_count = 0
            # print(self.__go_board[x])
            # iterate over the records in x number of columns
            for i in range(self.__board_size):
                # print(self.__go_board[i][x])
                board_piece = str(self.__go_board[i][x])
                current_player = str(' ● ' if self.__current_player == 'black' else ' ○ ')
                # print(board_piece,current_player)
                if board_piece == current_player:
                    vertical_count += 1
                    if vertical_count == self.__win_count:
                        return True
                else:
                    vertical_count = 0

        #iterate over the board diagonally both ways
        #https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
        matrix = np.array(self.__go_board)
        x,y = self.__board_size, self.__board_size
        np.arange(x * y).reshape(x, y)
        diags = [matrix[::-1, :].diagonal(i) for i in range(-matrix.shape[0] + 1, matrix.shape[1])]
        diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1] - 1, -matrix.shape[0], -1))
        diagonal_list = [n.tolist() for n in diags]

        for diagonal in diagonal_list:
            diagonal_count = 1
            for space in diagonal:
                space = str(space)
                current_player = str(' ● ' if self.__current_player == 'black' else ' ○ ')
                # print(board_piece,current_player)
                if space == current_player:
                    diagonal_count += 1
                    if diagonal_count == self.__win_count:
                        return True
                else:
                    diagonal_count = 0

        return False


def get_row_column(play, board):
    while True:

        if type(play) == str:
            if play.lower() == 'q':
                quit()

        try:
            play_list = play.strip().split(',')
            row = int(play_list[0])
            column = int(play_list[1])

            if row < 1 or column < 1:
                print('Invalid position.')
                print('Try again.')
                print(board)
                play = input("Input a row then column separated by a comma (q to quit): ")
            else:
                return row, column

        except (TypeError, ValueError, IndexError):
            print('Incorrect input.')
            print('Try again.')
            print(board)
            play = input("Input a row then column separated by a comma (q to quit): ")


def main():
    board = Gomoku()
    print(board)
    play = input("Input a row then column separated by a comma (q to quit): ")
    row, column = get_row_column(play, board)

    while play.lower() != 'q':

        try:

            player_color = board.get_current_player()
            player_piece = GoPiece(player_color)
            board.assign_piece(player_piece, row, column)

            if board.current_player_is_winner():
                print()
                print(board)
                print("{} Wins!".format(board.get_current_player()))
                quit()

            board.switch_current_player()
            print(board)
            play = input("Input a row then column separated by a comma (q to quit): ")
            row, column = get_row_column(play, board)

        except MyError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
            print(board)
            play = input("Input a row then column separated by a comma (q to quit): ")
            row, column = get_row_column(play, board)


if __name__ == '__main__':
    main()
