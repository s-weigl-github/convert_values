###########################
#  some easy progs maybe inch to cm or kmh to mph
#  or lightyear, time, speed of sound something like that ;-)
#  27.11.2013 ver. 0.1
###########################
import math

print("\nConvert Inch to cm!")
print("-  --  --  --  --  --  -")

inch = input("put in inch: ")
inch = float(inch.replace(",", "."))

cm = inch * 2.54
cm = round(cm, 4)

print("-  --  --  --  --  --  -- -")
print(inch, "inch are", cm, "cm long")

print("\n#######################################################")

print("\nConvert cm to Inch!")
print("-  --  --  --  --  --  -")

cm = input("put in cm: ")
cm = float(cm.replace(",", "."))

inch = cm * 0.393700787
inch = round(inch, 4)

print("-  --  --  --  --  --  -- -")
print(cm, "cm are", inch, "inch long")
