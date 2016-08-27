###########################
#  some easy progs maybe inch to cm or kmh to mph
#  or lightyear, time, speed of sound something like that ;-)
#  27.11.2013 ver. 0.1
###########################
import math

print("\nConvert km/h to mph!")
print("-  --  --  --  --  --  -")

kmh = input("put in km/h: ")
kmh = float(kmh.replace(",", "."))

mph = kmh * 0.6213
mph = round(mph, 4)

print("-  --  --  --  --  --  -- -")
print(kmh, "km/h are", mph, "mph")

print("\n#######################################################")

print("\nConvert mph to km/h!")
print("-  --  --  --  --  --  -")

mph = input("put in mph: ")
mph = float(mph.replace(",", "."))

kmh = mph / 1.609344 
kmh = round(kmh, 4)

print("-  --  --  --  --  --  -- -")
print(mph, "mph are", kmh, "km/h")
