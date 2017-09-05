secs_str = input("Input seconds: ") # do not change this line
seconds = int(secs_str)

SECS_PER_MIN = 60
SECS_PER_HOUR  = 3600

hours = seconds // SECS_PER_HOUR
mins = seconds // SECS_PER_MIN
minutes = mins % SECS_PER_MIN
seconds = seconds % SECS_PER_MIN
print(hours,":",minutes,":",seconds) # do not change this line