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

class GoPiece(object):

    def __init__(self, color='black'):
        self.__color = color
        # if self.__color != 'black' or self.__color != 'white':
        # raise MyError('Wrong color.')

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
        self.__go_board = [[' - ' for j in range(self.__board_size)] for i in range(self.__board_size)]

        if type(self.__board_size) != int:
            raise ValueError('Board is not an integer')
        if type(self.__win_count) != int:
            raise ValueError('Win count is not an integer')
        # if self.__current_player != 'black' or self.__current_player != 'white' or self.__current_player != '-':
        # raise MyError('Wrong color.')

    def assign_piece(self, piece, row, col):
        if row > self.__board_size or col > self.__board_size:
            raise MyError('Invalid position.')
        if self.__go_board[row-1][col-1] != ' - ':
            raise MyError('Position is occupied.')
        self.__go_board[row-1][col-1] = piece

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

        # iterate over the board and find winner
        for row in self.__go_board:
            horizontal_count = 0
            #print(row)
            for item in row:
                #this is a board piece item and current_player should be same type
                current_player = '●' if self.__current_player == 'black' else '○'
                if item == current_player:
                    horizontal_count += 1
                    if horizontal_count == 5:
                        return True
                else:
                    horizontal_count = 0

        # iterate over the columns in the board
        for x in range(self.__board_size):
            pass

def get_row_column(play):

    while True:

        try:
            play_list = play.strip().split(',')
            row = int(play_list[0])
            column = int(play_list[1])
            return row, column

        except (TypeError,ValueError):
            print('Incorrect input.')
            print('Try again.')

def main():
    board = Gomoku()
    print(board)
    play = input("Input a row then column separated by a comma (q to quit): ")

    while play.lower() != 'q':

        row, column = get_row_column(play)

        try:

            player_color = board.get_current_player()
            player_piece = GoPiece(player_color)
            board.assign_piece(player_piece, row, column)

        #                raise MyError("Incorrect input.")
            if board.current_player_is_winner():
                print("{} Wins!".format(board.get_current_player()))
                quit()

        except MyError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))

        board.switch_current_player()
        print(board)
        play = input("Input a row then column separated by a comma (q to quit): ")


if __name__ == '__main__':
    main()
