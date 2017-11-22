

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

    player_origin = " "

    if board.points[destination] == " ":
        move_piece(board, player, player_origin, destination)
     
def move_piece(board, player, origin, destination):
    """
        add your function header here.
    """

    initial_mill_count = count_mills(board, player)

    if board.points[destination] == " ":
        board.assingn_piece(destination)
        board.clear_place(origin)

        #board.points[destination] = player
        #board.points[origin] = " "

    else:
        print("Error, you cannot move there")

    final_mill_count = count_mills(board, player)

    if initial_mill_count != final_mill_count:
        destination = input("Choose where you want to remove your opponent.")
        place_piece_and_remove_opponents(board, player, destination)
    
def points_not_in_mills(board, player):
    """
        add your function header here.
    """

    point_not_mill_list = list()
    mill_list = list()


    for mill in board.MILLS:

        temp_list = list()

        for place in mill:

            place_value = board.points[place]

            if place_value == player:
                temp_list.append(place)
                point_not_mill_list.append(place)

        if len(temp_list) == 3:
            mill_list.extend(temp_list)

    for item in point_not_mill_list:
        if item in mill_list:
            point_not_mill_list.remove(item)

    point_not_mill_list = set(point_not_mill_list)-(set(mill_list))

    return point_not_mill_list

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
    is_valid_position = False
    current_placed = placed(board, player)

    while is_valid_position:

        destination = input("Where would you like to move to?")
        desired_place = board.points[destination]

        if destination not in current_placed or desired_place != " ":
            print("Hey you can't remove your own piece or remove a blank piece.")

        else:
            board.points[destination] = " "
            is_valid_position = True


           
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

    if x_count <= 3 or o_count <= 3:
        return True
    else:
        return False
   
def get_other_player(player):
    """
    Get the other player.
    """
    return "X" if player == "O" else "O"
    
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
        print()
        #Until someone quits or we place all 18 pieces...
        while command != 'q' and placed_count != 18:
            try:
                
                pass  # stub; delete and replace it with your code
                
            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
            #Prompt again
            print(board)
            print(player + "'s turn!")
            if placed_count < 18:
                command = input("Place a piece at :> ").strip().lower()
            else:
                print("**** Begin Phase 2: Move pieces by specifying two points")
                command = input("Move a piece (source,destination) :> ").strip().lower()
            print()
        
        #Go back to top if reset
        if command == 'r':
            continue
        # PHASE 2 of game
        while command != 'q':
            # commands should have two points
            command = command.split()
            try:
                
                pass  # stub; delete and replace it with your code
                
            #Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))         
            #Display and reprompt
            print(board)
            #display_board(board)
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower()
            print()
            
        #If we ever quit we need to return
        if command == 'q':
            return

            
if __name__ == "__main__":
    main()
