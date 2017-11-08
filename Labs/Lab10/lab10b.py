
import cards

# Create the deck of cards
import random
random.seed( 100 )

# Create a deck of cards

the_deck = cards.Deck()


# Shuffle the deck, then display it in 13 columns

the_deck.shuffle()
print( "===== shuffled deck =====" )
the_deck.display()


# Deal five cards to each player (alternating)

print( "Dealt five cards to each player (alternating)" )
print()

player1_list=[]
player2_list=[]
for i in range( 5 ):
    player1_list.append(the_deck.deal())
    player2_list.append(the_deck.deal())

# Display each player's cards and the cards still in the deck

print( "===== player #1 =====" )
print()
print( player1_list )
print()
print( "===== player #2 =====" )
print()
print( player2_list )
print()
print( "===== remaining cards in deck =====" )
the_deck.display()

user_choice = input("Would you like to continue/play?").lower()
winning_player = ""

while user_choice != 'n' and len(player2_list) != 0 and len(player1_list) != 0:
    # First card dealt to Player #1
    print("\n")
    player1_card = player1_list.pop( 0 )
    print("First card dealt to player #1:", player1_card )
    print("Player #1 hand", player1_list)


    # First card dealt to Player #2
    print()
    player2_card = player2_list.pop( 0 )
    print("Second card dealt to player #2:", player2_card )
    print("Player #2 hand", player2_list)



    # Compare the ranks of the two cards

    print()
    if player1_card.rank() == player2_card.rank():
        print( "Tie:", player1_card, "and", player2_card, "of equal rank" )
        player1_list.append(player1_card)
        player2_list.append(player2_card)
    elif player1_card.rank() > player2_card.rank():
        print( "Player #1 wins:", player1_card, "of higher rank than", player2_card )
        winning_player = "Player 1 was the winning player."
        player1_list.append(player1_card)
        player1_list.append(player2_card)
    else:
        print( "Player #2 wins:", player2_card, "of higher rank than", player1_card )
        winning_player = "Player 2 was the winning player."
        player2_list.append(player2_card)
        player2_list.append(player1_card)

    user_choice = input("Would you like to continue?").lower()

print()
print(winning_player)
the_deck = cards.Deck()
the_deck.shuffle()


