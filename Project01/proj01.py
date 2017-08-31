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
time_to_walk = round(miles/(walking_speed/60),3)

#output calculations
print("Conversions:")
print("Meters: ", round(rod_meters,3))
print("Feet: ", feet)
print("Miles: ", round(miles,3))
print("Furlongs: ",furlongs)
print("Minutes to walk ", rods, " rods: ", time_to_walk)