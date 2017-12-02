##################################################################################################
#   Project 11 - Gomoku
#
#   import dependancies
#   class GoPiece
#       initializes object with a color
#       returns object color
#   class MyError
#       initializes exception as error
#   class Gomoku
#       __init__
#           initializes object with board size, win count, and current player
#           if any of the values are incorrect raise an error
#           initialize board as __go_board
#       assign piece function
#           checks if rows and columns are in range
#               raises error if not
#           assigns piece to spot on the board
#       get current player
#           returns current player
#       switch current player
#           switches current player directly
#       __str__
#           overrides string method to print player color as solid or hollow disk
#       current player is winner class
#           iterates through the board and finds pieces in a row that are of length win count
#   get row coloumn function
#       gets row and column from user input
#   main
#       initialize new board and prompt for user input
#       check if move is valid and check if is winner
#       switch players and prompt again
##################################################################################################

import numpy as np


class GoPiece(object):
    """
    __init__
        initialize new GoPiece object with color
    __repr__
        define object representation
    __str__
        format color value as board piece when printed
    get color function
        return color
    """

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
    """
    __init__
        initialize exception as value
    __str__
        return value of exception
    """
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return self.__value


class Gomoku(object):
    """
    __init__
        initialize game with board size, win count, and starting player
        raise any errors for incorrect values
    assign piece function
        check if location is valid
        assign piece to location on board
    get current player function
        returns current player
    switch player function
        changes value of player atrribute to whatever the current one is not
    __str__
        formats board to be printed as 2-D object with points
    current player is winner function
        loop over the board and find winning_number amount in a row
    """

    def __init__(self, board_size=15, win_count=5, current_player='black'):
        """
        initialize game object with board size, win count, and starting player
        :param board_size - int as length and width of board:
        :param win_count - int number of pieces in a row to win:
        :param current_player - string, starting player color:
        """

        self.__board_size = board_size
        self.__win_count = win_count
        self.__current_player = current_player

        player = str(self.__current_player)

        if player != 'black' and player != 'white':
            raise MyError('Wrong color.')
        if type(self.__board_size) != int:
            raise ValueError('Board is not an integer')
        if type(self.__win_count) != int:
            raise ValueError('Win count is not an integer')

        self.__go_board = [[' - ' for j in range(self.__board_size)] for i in range(self.__board_size)]

    def assign_piece(self, piece, row, col):
        """
        check if board values are correct
        assign board piece to place on board
        :param piece - string, player piece resolved from color:
        :param row - int, row as a number:
        :param col - int, column as a number:
        :return <none> :
        """
        if row > self.__board_size or col > self.__board_size:
            raise MyError('Invalid position.')
        elif self.__go_board[row - 1][col - 1] != ' - ':
            raise MyError('Position is occupied.')
        else:
            self.__go_board[row - 1][col - 1] = piece

    def get_current_player(self):
        """
        :return current player as string:
        """
        return self.__current_player

    def switch_current_player(self):
        """
        update player value to be other player
        :return <none> :
        """
        if self.__current_player == 'black':
            self.__current_player = 'white'
        else:
            self.__current_player = 'black'

    def __str__(self):
        """
        format board object to 2-D figure
        :return - string, board as string:
        """
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

        # iterate over the board diagonally both ways
        # https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
        matrix = np.array(self.__go_board)
        x, y = self.__board_size, self.__board_size
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
    """
    prompt for user input until its correct
    catch any letters or incomplete values in user input
    :param play - string, user command:
    :param board - object, board:
    :return row, column - int, locations on board in 2-D:
    """
    # loop until there is valid user input
    while True:

        if type(play) == str:
            if play.lower() == 'q':
                quit()

        try:
            play_list = play.strip().split(',')
            row = int(play_list[0])
            column = int(play_list[1])

            # row index out of range
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
    """
    intialize new game object
    print board and prompt for user input for location
    pass user input onto get row column function to extact row and column
    if player is a winner then halt the game and print they are a winner
    catch any error messages that may be raised and reprompt
    :return <none> :
    """
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
