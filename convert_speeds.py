#########################
### convert length and speeds
### S.Weigl - 15.08.2016
### ver. 1.0 - german version
### python version 3.2.5 and 3.6.0a1
#########################

import math

get_kmh = None
get_mph = None

def kmh2mph(get_kmh):
  #
  print("\nConvert km/h to mp/h")
  get_kmh = input("put in km/h: ")
  get_kmh = float(get_kmh.replace(',','.'))
  #
  ans = get_kmh * 0.6213
  ans = round(ans, 4)
  print("\n", get_kmh, "km/h are", ans, "mp/h")
##

def mph2kmh(get_mph):
  #
  print("\nConvert mp/h to km/h")
  get_mph = input("put in mp/h: ")
  get_mph = float(get_mph.replace(',','.'))
  #
  ans = get_mph / 1.609344
  ans = round(ans, 4)
  print("\n", get_mph, "mp/h are",  ans, "km/h")
##

def to_end():
  print("\nnothing to do, so i'm")
  print("Done!!!")

## E-o-F
