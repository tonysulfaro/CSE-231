# Author:   Tony Sulfaro
# Date :    8/31/2017
# Purpose:  This program covers examples given in the pre-lab05 quiz

import math

AAA = 8
BBB = 20
C = BBB + AAA
print( C )

AAA = 8
BBB = 20
C = BBB * AAA
print( C )

AAA = 8
BBB = 20
A = BBB / AAA
print( A )

AAA = 8
BBB = 20
B = BBB // AAA  # Note the double slash
print( B )      # 8 goes into 20 2 times

AAA = 8
BBB = 20
C = BBB % AAA   #leftover of putting 8 into 20 is 4
print( C )

AAA = 2
BBB = 5
C = BBB ** AAA  #exponent
print( C )

F = 5
F += 1
print( F )

YYY = 17.9
H = int(YYY)    #cating an int cuts off the decimal
print( H )

ZZZ = 2
J = float(ZZZ)  #casting to a float adds a decimal to an int
print( J )
