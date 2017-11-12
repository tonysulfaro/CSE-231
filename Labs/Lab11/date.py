
###########################################################################
## Class Date
###########################################################################

class Date( object ):

    __name = [ "Invalid", "January", "February", "March", "April", 
        "May", "June", "July", "August", "September", "October", 
        "November", "December" ]

    __days = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    
    def __init__( self, month=0, day=0, year=0 ):
        
        """ Construct a Date using three integers. """
            
        self.__month = month
        self.__day   = day
        self.__year  = year
        self.__valid = self.__validate()

    def __repr__( self ):

        """ Return a string as the formal representation a Date. """

        out_str = "Class Date: {:02d}/{:02d}/{:04d}" \
            .format( self.__month, self.__day, self.__year )

        return out_str

    def __str__( self ):

        """ Return a string (mm/dd/yyyy) to represent a Date. """

        out_str = "{:02d}/{:02d}/{:04d}" \
            .format( self.__month, self.__day, self.__year )

        return out_str

    def __validate( self ):

        # Check the month, day and year for validity
        # (does not account for leap years)

        flag = False

        if (1 <= self.__month <= 12) and \
           (1 <= self.__day <= Date.__days[self.__month] ) and \
           (0 <= self.__year):
            
               flag = True
            
        return flag

    def is_valid( self ):

        """ Return Boolean flag (valid date?) """

        return self.__valid

    def from_iso( self, iso_str ):

        """ Convert a string (yyyy-mm-dd) into a Date. """

        year, month, day = [ int( n ) for n in iso_str.split( '-' )]
            
        self.__month = month
        self.__day   = day
        self.__year  = year
        self.__valid = self.__validate()


    def from_mdy( self, mdy_str ):

        """ Convert a string (Mmmmm dd, yyyy) into a Date. """

        mdy_list = mdy_str.replace(",","").split()
                    
        self.__month = Date.__name.index( mdy_list[0] )
        self.__day   = int( mdy_list[1].strip() )
        self.__year  = int( mdy_list[2].strip() )
        self.__valid = self.__validate()

    def to_iso( self ):

        """ Return a string (yyyy-mm-dd) to represent a Date. """

        iso_str = "{:04d}-{:02d}-{:02d}" \
            .format( self.__year, self.__month, self.__day )

        return iso_str

    def to_mdy( self ):

        """ Return a string (Mmmmm dd, yyyy) to represent a Date. """

        mdy_str = "{:s} {:d}, {:04d}" \
            .format( Date.__name[self.__month], self.__day, self.__year )

        return mdy_str

