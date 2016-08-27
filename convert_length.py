#########################
### convert length and speeds
### S.Weigl - 15.08.2016
### ver. 1.0 - german version
### python version 3.2.5 and 3.6.0a1
#########################

import math

get_cm = None
get_inch = None

def inch2cm(get_inch):
  #
  print("\nConvert inch to cm")
  get_inch = input("put in inch: ")
  get_inch = float(get_inch.replace(',','.'))
  #
  ans = get_inch * 2.54
  ans = round(ans, 4)
  print("\n", get_inch, "inch are", ans, "cm")
##

def cm2inch(get_cm):
  #
  print("\nConvert cm to inch")
  get_cm = input("put in cm: ")
  get_cm = float(get_cm.replace(',','.'))
  #
  ans = get_cm * 0.393700787
  ans = round(ans, 4)
  print("\n", get_cm, "cm are",  ans, "inch")
##

##def to_end():
##  print("\nnothing to do, so i'm")
##  print("Done!!!")

## E-o-F
