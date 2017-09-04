# Author:   Tony Sulfaro
# Date :    8/31/2017
# Purpose:  This program converts rods to other distances

#prompt for user input for number of rods
Rods = float(input("Input rods: "))       #one rod is 5.0292 meters
print("You input ", Rods, " rods.")
print()

#constants for calculations
RodMeters = 5.0292
walking_speed = 3.1 #miles per hour

#calculate units of other measurements
Meters = RodMeters * Rods
Furlongs = Rods / 40
Miles = Rods * RodMeters / 1609.34
Feet = Meters / .3048
TimeToWalk = Miles / (walking_speed / 60)

#output calculations (round answers to 3 decimal places)
print("Conversions:")
print("Meters: ", round(Meters, 3))
print("Feet: ", round(Feet, 3))
print("Miles: ", round(Miles, 3))
print("Furlongs: ", round(Furlongs, 3))
print("Minutes to walk ", Rods, " rods: ", round(TimeToWalk, 3))