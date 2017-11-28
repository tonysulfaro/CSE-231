######################################################################################################
# Project 10 - Nine Men's Morris
#   import NMM class and initialize game banner and information
#   count_mills function
#       takes the board and a player and counts the number of mills the player is in
#       returns mill count as an integer
#   place piece and remove opponent function
#       try to assingn a place on the board
#       if its not valid placement print error and reprompt
#       if a mill is formed then call the remove_piece function
#   move piece function
#       while is a valid move, if the move isnt valid print error and reprompt
#       if the mills before and after the move are different
#           if the count of mills before the movement is less than or equal to the number of mills after
#               call the remove piece function
#       check if there is a winner
#           print banner and quit program if there is
#   points not in mills function
#       takes the board and a player
#       finds all the places where the player is on the board and not in a mill
#       returns the points as a list
#   placed function
#       takes the board and the player and finds all the places on the board where the player is
#       returns list of places where player is
#   remove piece function
#       take a board and a player
#       prompt for which place the user wants to remove an opponent
#       check if its a valid place to remove and if not print error and reprompt
#       remove the piece
#   is_winner function
#
#
#
#
#
#
#
#
#
#
#
######################################################################################################

import NMM #This is necessary for the project

BANNER = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""

RULES = """
  _   _ _              __  __            _       __  __                 _     
 | \ | (_)_ __   ___  |  \/  | ___ _ __ ( )___  |  \/  | ___  _ __ _ __(_)___ 
 |  \| | | '_ \ / _ \ | |\/| |/ _ \ '_ \|// __| | |\/| |/ _ \| '__| '__| / __|
 | |\  | | | | |  __/ | |  | |  __/ | | | \__ \ | |  | | (_) | |  | |  | \__ \
 |_| \_|_|_| |_|\___| |_|  |_|\___|_| |_| |___/ |_|  |_|\___/|_|  |_|  |_|___/
                                                                                        
    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to 
    make mills. When a mill (or mills) is made one opponent's piece can be 
    removed from play. In Phase 2 play continues by moving pieces to 
    adjacent points. 
    
    The game is ends when a player (the loser) has less than three 
    pieces on the board.

"""

MENU = """

    Game commands (first character is a letter, second is a digit):
    
    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game
    
"""
        
def count_mills(board, player):
    """
    for each mill in the board MILLS
        for each place in the mill
            if the value of the place is the player increment mill count
        if the mill count == 3 then its a mill
            increment the total_mill_count
    :param board - board as a dictionary:
    :param player - current player as a string:
    :return - count of mills as integer:
    """

    total_mill_count = 0

    for mill in board.MILLS:

        mill_count = 0

        for place in mill:

            place_value = board.points[place]

            if place_value == player:
                mill_count += 1

        if mill_count == 3:
            total_mill_count += 1

    return total_mill_count
            
def place_piece_and_remove_opponents(board, player, destination):
    """
    get initial mill count
    while is a valid move
        try to assingn the player to a place on the board
            print error if the space is not " "
            reprompt for destination
        except keyerror if they move to non-existent place on the board
            print error and reprompt.
        get final mill count after place
            if the count is more then call remove_piece
    :param board - board as a dictionary:
    :param player - player as a string:
    :param destination - destination for placement as a string:
    :return <none> :
    """

    initial_mill_count = count_mills(board, player)

    is_valid_move = True

    while is_valid_move:

        try:

            if board.points[destination] == " " and board.points[destination] != get_other_player(player) and board.points[destination] != player:
                board.points[destination] = player
                is_valid_move = False
            else:
                print("Error, you cannot move there")
                destination = input("Place a piece at :> ").strip().lower()

        except KeyError:

            print("Error, you cannot move there")
            destination = input("Place a piece at :> ").strip().lower()

    final_mill_count = count_mills(board, player)

    if initial_mill_count < final_mill_count:
        remove_piece(board, player)
     
def move_piece(board, player, origin, destination):
    """
    get initial mill list, and other player
    while is valid move
        if point to move is the other player or anything else but a blank point
            print error and reprompt
        catch some key and index errors
            print error and reprompt
    get final mill list
    if the mill lists are different and the final is greater than or equal to the initial list
        call the remove function
    check if is winner
        print banner and halt program if true
    print board
    :param board - board as an object:
    :param player - player as a string:
    :param origin - origin on board as a string:
    :param destination - destination on board as a string:
    :return <none> :
    """

    inital_mill_list = get_mill_list(board, player)
    other_player = get_other_player(player)

    is_valid_move = True

    #this is pretty jank sorry you have to look at this
    while is_valid_move:

        try:

            if board.points[origin] == other_player:
                print("Invalid command: Origin point does not belong to player")
                print("Try again.")
                print(board)
                print(player + "'s turn!")
                command = input("Move a piece (source,destination) :> ").strip().lower().split(" ")
                origin = command[0]
                destination = command[1]

            elif board.points[destination] == " ":
                board.assign_piece(player,destination)
                board.assign_piece(" ", origin)
                is_valid_move = False

            else:
                print("Invalid command: Not a valid point")
                print("Try again.")
                print(board)
                print(player + "'s turn!")
                command = input("Move a piece (source,destination) :> ").strip().lower().split(" ")
                origin = command[0]
                destination = command[1]

        except (KeyError, IndexError):

            print("Invalid command: Not a valid point")
            print("Try again.")
            print(board)
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower().split(" ")
            origin = command[0]
            destination = command[1]

    final_mill_list = get_mill_list(board, player)

    if inital_mill_list != final_mill_list and len(inital_mill_list) <= len(final_mill_list):
        remove_piece(board, player)

    if is_winner(board, player):
        print(BANNER)
        quit()

    print(board)

def points_not_in_mills(board, player):
    """
    intitialize occupied places and mill points as a set
    for place in the board
        if the value is the player add it to the occupied set
    for mill in board mills
        for place in mill
            if the value at the place == player
                then add it to mill values
        if player in mill set and length of mill set == 1:
            it means the player is in the mill
            add it to the mill points
    find difference of sets and make it a list
    :param board - board as an object:
    :param player - player as a string:
    :return - set difference as a list:
    """

    occupied_places = set()
    mill_points = set()

    #generates a set of where all the player values are
    for space in board.points:
        value = board.points[space]
        if value == player:
            occupied_places.add(space)

    #generates a set of where all the values that are also mills are
    for mill in board.MILLS:

        mill_values = list()

        for place in mill:
            value = board.points[place]
            mill_values.append(value)
        #all locations have to have player for each of them
        if player in set(mill_values) and len(set(mill_values)) == 1:
            for item in mill:
                mill_points.add(item)

    difference = list(occupied_places-mill_points)

    return difference

def placed(board, player):
    """
    for each mill in mill list
        for place in mill
            if the player is there add it to the list
    take the set of the list to get only unique values
    reutrn the list from the set
    :param board - board as an object:
    :param player - player as a string:
    :return location_list - list of points where a player is:
    """

    location_list = list()

    for mill in board.MILLS:

        for place in mill:

            place_value = board.points[place]

            if place_value == player:

                location_list.append(place)

    location_list = set(location_list)

    return location_list
    
def remove_piece(board, player):
    """
    get current placed and other player
    print header and board
    prompt where to remove piece
    check if its a valid place to remove or if it exists
        print error if there is a problem with the place and reprompt
    :param board - game board as an object:
    :param player - player as a string:
    :return <none> :
    """
    is_valid_position = True
    current_placed = placed(board, player)
    player = get_other_player(player)

    print("A mill was formed!")
    print(board)

    while is_valid_position:

        destination = input("Remove a piece at :> ")

        #desired_place = board.points[destination] #this is actually just the value at that place..
        not_in_mills = points_not_in_mills(board, player)

        if destination not in board.points:
            print("Invalid command: Not a valid point")
            print("Try again.")
        elif destination in current_placed:
            print("Invalid command: Point does not belong to player")
            print("Try again.")
        elif board.points[destination] == " ":
            print("Invalid command: Point does not belong to player")
            print("Try again.")
        #if destination is a valid point to remove
        elif destination in not_in_mills:
            board.points[destination] = " "
            #print(board)
            break
        #if destination is in a mill but its the only option to remove
        elif destination not in not_in_mills and len(not_in_mills) == 0:
            board.points[destination] = " "
            #print(board)
            break
        #if the destination is in a mill and there are other options to remove
        elif destination not in not_in_mills and len(not_in_mills) != 0:
            print("Invalid command: Point is in a mill")
            print("Try again.")

def is_winner(board, player):
    """
    for each mill in board mills
        for each place in the mill
            add place to set
    for each place in the mill set
        get value at that place
        if the place is x or O add it to their counts
    if either of the counts is less than 3 return true
    :param board - board as an object:
    :param player - player as a string:
    :return boolean - status if game is won or not:
    """
    x_count = 0
    o_count = 0
    mill_set = set()

    for mill_triple in board.MILLS:
        for mill in mill_triple:
            mill_set.add(mill)

    for place in mill_set:
        place_value = board.points[place]

        if place_value == 'X':
            x_count += 1
        elif place_value == 'O':
            o_count += 1

    if x_count < 3 or o_count < 3:
        return True
    else:
        return False
   
def get_other_player(player):
    """
    Get the other player.
    """
    return "X" if player == "O" else "O"

def get_mill_list(board, player):

    mill_points = list()

    # generates a set of where all the values that are also mills are
    for mill in board.MILLS:

        mill_values = list()

        for place in mill:
            value = board.points[place]
            mill_values.append(value)

        # all locations have to have player for each of them
        if player in set(mill_values) and len(set(mill_values)) == 1:
            mill_points.append(mill)

    return mill_points

def main():

    #Loop so that we can start over on reset
    while True:

        #Setup stuff.
        print(RULES)
        print(MENU)
        board = NMM.Board()
        print(board)
        player = "X"
        placed_count = 0 # total of pieces placed by "X" or "O", includes pieces placed and then removed by opponent

        #TESTING
        count_mills(board, player)
        points_not_in_mills(board, player)


        # PHASE 1
        print(player + "'s turn!")
        #placed = 0
        command = input("Place a piece at :> ").strip().lower()

        if command == 'h':
            print(MENU)
            command = input("Place a piece at :> ").strip().lower()
        elif command == 'r':
            continue
        print()

        #Until someone quits or we place all 18 pieces...
        while command != 'q' and placed_count != 18:
            try:

                place_piece_and_remove_opponents(board, player, command)
                placed_count += 1


            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:

                print("{:s}\nTry again.".format(str(error_message)))

                #Prompt again
                place_piece_and_remove_opponents(board, player, command)


            print(board)
            player = get_other_player(player)
            print(player + "'s turn!")

            if placed_count < 18:
                command = input("Place a piece at :> ").strip().lower()
                if command == 'h':
                    print(MENU)
                    command = input("Place a piece at :> ").strip().lower()
                elif command == 'r':
                    break
            else:
                print("**** Begin Phase 2: Move pieces by specifying two points")
                command = input("Move a piece (source,destination) :> ").strip().lower()
            print()

            #Change player

        #Go back to top if reset
        if command == 'r':
            continue

        # PHASE 2 of game
        while command != 'q':

            # commands should have two points

            command = command.split(" ")
            initial_position = ""
            final_position = ""
            command_is_valid = True

            while command_is_valid:

                try:
                    initial_position = command[0]
                    final_position = command[1]
                    command_is_valid = False
                except IndexError:
                    print("Invalid number of points")
                    print("Try again.")
                    print(board)
                    print(player + "'s turn!")
                    command = input("Move a piece (source,destination) :> ").strip().lower().split(" ")

            try:

                move_piece(board, player, initial_position, final_position)
                if is_winner(board,player):
                    print(BANNER)
                    quit()

                
            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))         
            #Display and reprompt
            #print(board)
            #display_board(board)
            player = get_other_player(player)
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower()
            print()
            
        #If we ever quit we need to return
        if command == 'q':
            return

if __name__ == "__main__":
    main()