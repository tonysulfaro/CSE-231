# DO NOT COPY AND PASTE FROM YOUR BROWSER. 
# YOU MUST DOWNLOAD THIS FILE.

class GoPiece(object):
    ''' Comment goes here.'''
    def __init__(self,color):
        ''' Comment goes here.'''
        pass  # replace and delete
    
    def __str__(self):
        ''' Comment goes here.'''
#  Two strings to help you
#            return ' ● '
#            return ' ○ '
        pass  # replace and delete
    
    def get_color(self):
        ''' Comment goes here.'''
        pass  # replace and delete
            
class MyError(Exception):
    def __init__(self,value):
        self.__value = value
    def __str__(self):
        return self.__value

class Gomoku(object):
    ''' Comment goes here.'''
    def __init__(self,board_size,win_count,current_player):
        ''' Comment goes here.'''
        pass  # replace and delete
#        self.__go_board = [ [ ' - ' for j in range(self.__board_size)] for i in range(self.__board_size)]
#            raise MyError('Wrong color.')    
            
    def assign_piece(self,piece,row,col):
        ''' Comment goes here.'''
        pass  # replace and delete
#            raise MyError('Invalid position.')
#            raise MyError('Position is occupied.')
            
    def get_current_player(self):
        ''' Comment goes here.'''
        pass  # replace and delete
    
    def switch_current_player(self):
        ''' Comment goes here.'''
        pass  # replace and delete
        
    def __str__(self):
        s = '\n'
        for i,row in enumerate(self.__go_board):
            s += "{:>3d}|".format(i+1)
            for item in row:
                s += str(item)
            s += "\n"
        line = "___"*self.__board_size
        s += "    " + line + "\n"
        s += "    "
        for i in range(1,self.__board_size+1):
            s += "{:>3d}".format(i)
        s += "\n"
        s += 'Current player: ' + ('●' if self.__current_player == 'black' else '○')
        return s
        
    def current_player_is_winner(self):
        ''' Comment goes here.'''
        pass  # replace and delete
        
def main():

    board = Gomoku()
    print(board)
    play = input("Input a row then column separated by a comma (q to quit): ")
    while play.lower() != 'q':
        play_list = play.strip().split(',')
        try: 
            
                    pass  # replace and delete

#                raise MyError("Incorrect input.")
#                print("{} Wins!".format(board.get_current_player()))


        except MyError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
        print(board)
        play = input("Input a row then column separated by a comma (q to quit): ")

if __name__ == '__main__':
    main()
