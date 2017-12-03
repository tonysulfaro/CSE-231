
##
## Class PetError -- complete
##

class PetError( ValueError ):
    
    pass

##
## Class Pet -- not complete
##

class Pet( object ):
    
    def __init__( self, species=None, name="" ):
        
        if species:
            
            self.species_str = species.title()
            self.name_str = name.title()
            
        else:
            
            raise PetError()
            
    def __str__( self ):
        
        result_str = "species of {:s}".format(self.species_str)
        
        return result_str

##
## Class Dog -- not complete
##

class Dog( Pet ):

    pass

##
## Class Cat -- not complete
##

class Cat( Pet ):
    
    pass

