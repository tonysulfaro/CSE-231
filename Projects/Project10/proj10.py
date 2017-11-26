

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
        add your function header here.
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
        add your function header here.
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
        add your function header here.
    """

    initial_mill_count = count_mills(board, player)
    #print('initial mill count ', initial_mill_count)
    other_player = get_other_player(player)

    is_valid_move = True

    while is_valid_move:

        try:

            if board.points[destination] == " ":
                #board.assingn_piece(destination)
                #board.clear_place(origin)
                board.points[destination] = player
                board.points[origin] = " "
                is_valid_move = False

            elif board.points[destination] == other_player:
                print("Invalid command: Origin point does not belong to player")
                print("Try again.")
                command = input("Move a piece (source,destination) :> ").strip().lower().split(" ")
                origin = command[0]
                destination = command[1]

            else:
                print("Invalid command: Not a valid point")
                print("Try again.")
                command = input("Move a piece (source,destination) :> ").strip().lower().split(" ")
                origin = command[0]
                destination = command[1]

        except (KeyError, IndexError):

            print("Invalid command: Not a valid point")
            print("Try again.")
            command = input("Move a piece (source,destination) :> ").strip().lower().split(" ")
            origin = command[0]
            destination = command[1]

    final_mill_count = count_mills(board, player)

    if initial_mill_count < final_mill_count:
        remove_piece(board, player)

    if is_winner(board, player):
        print(BANNER)
        quit()

    print(board)


def points_not_in_mills(board, player):
    """
        add your function header here.
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

def placed(board,player):
    """
        add your function header here.
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
        add your function header here.
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
        add your function header here.
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