# Author:   Tony Sulfaro
# Date :    8/31/2017
# Purpose:  This program solves the quadratic formula

import math

print("Hello this program calculates the two roots for a quadratic formula given user input.")

#read in user input as string
string_a = input("Please enter A:")
string_b = input("Please enter B:")
string_c = input("Please enter C:")

#Convert user input from string to float
float_a = float(string_a)
float_b = float(string_b)
float_c = float(string_c)

#calculate positve and negative root if it exists
positive_quad_calc = (-float_b + math.sqrt(float_b**2-4*float_a*float_c))/2*float_a
negative_quad_calc = (-float_b - math.sqrt(float_b**2-4*float_a*float_c))/2*float_a

#display output of calculation
print("Root #1 = ", positive_quad_calc)
print("Root #2 = ", negative_quad_calc)
