def test( a, b ):
   ''' Parameters a and b are in the namespace of the function 'test' '''
   a = 7

   print( "In test, value of a:", a ) # Line 1

   print( "In test, value of b:", b ) # Line 2

   # x is not in the function's namespace so this is a global reference
   # Global references such as this are NOT allowed in CSE 231!
   print( "In test, value of x:", x ) # Line 3

   return a   # THIS LINE ADDED FOR THIS QUESTION

a = 1
b = 2
x = 5
y = test( a, b )

print( "In main, value of a:", a ) # Line 4

print( "In main, value of b:", b ) # Line 5

print( "In main, value of x:", x ) # Line 6

print( "In main, value of y:", y ) # Line 7