# Author:   Tony Sulfaro
# Date :    8/31/2017
# Purpose:  This program solves the quadratic formula

import math

print("Hello this program calculates the two roots for a quadratic formula given user input.\n")

#read in user input as string
InputA = input("Please enter A:")
InputB = input("Please enter B:")
InputC = input("Please enter C:")

#Convert user input from string to float
A = float(InputA)
B = float(InputB)
C = float(InputC)

print( "\nThe coefficients of the equation:\n" )
print( "Coefficient A = ", A )
print( "Coefficient B = ", B )
print( "Coefficient C = ", C )

#calculate positve and negative root if it exists
PlusQuadCalc = (-B + math.sqrt(B ** 2 - 4 * A * C)) / 2 * A
MinusQuadCalc = (-B - math.sqrt(B ** 2 - 4 * A * C)) / 2 * A

#display output of calculation
print( "\nThe roots of the equation:\n" )
print("Root #1 = ", PlusQuadCalc)
print("Root #2 = ", MinusQuadCalc)
