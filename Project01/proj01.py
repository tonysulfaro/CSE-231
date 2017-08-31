# Author:   Tony Sulfaro
# Date :    8/31/2017
# Purpose:  This program converts rods to other distances

#prompt for user input for number of rods
user_rods = input("What will the distance in rods be? ")
rods = float(user_rods)        #one rod is 5.0292 meters
print("You input ", rods, " rods.")
print()

#constants for calculations
rod_meters = 5.0292
walking_speed = 3.1 #miles per hour

#calculate units of other measurements
furlongs = rods/40
miles = rods*rod_meters/1609.34
feet = rod_meters/.3048
time_to_walk = miles/(walking_speed/60)

#output calculations
print("Conversions:")
print("Meters: ", rod_meters)
print("Feet: ", feet)
print("Miles: ", miles)
print("Furlongs: ",furlongs)
print("Minutes to walk ", rods, " rods: ", time_to_walk)