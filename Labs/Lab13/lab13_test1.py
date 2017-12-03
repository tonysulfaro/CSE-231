
##
## Demonstrate some of the operations of the Pet classes
##

import pets


def main():
    
    try:

        A = pets.Pet( "hamster" )
        print( A )
              
        # Dog named Fido who chases Cats
        B = pets.Dog( "Fido" )
        print( B )

        # Cat named Fluffy who hates everything
        C = pets.Cat( "Fluffy", "everything" )
        print( C )

        D = pets.Pet( "pig" )
        print( D )
        
    except pets.PetError:
        
        print( "Got a pet error." )

main()

