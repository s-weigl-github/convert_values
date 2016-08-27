#########################
### convert length and speeds
### S.Weigl - 15.08.2016
### ver. 1.0 - german version
### python version 3.2.5 and 3.6.0a1
#########################

from convert_speeds import *
from convert_length import *


print("Mit diesem kleinen Programm kannst Du Werte umrechnen\n")

print("um cm in inch umzurechnen gib 'ci' ein")
print("um inch in cm umzurechnen gib 'ic' ein\n\n")

print("um km/h in mp/h umzurechnen gib 'km' ein")
print("um mp/h in km/h umzurechnen gib 'mk' ein\n\n")

get_choice = str(input("Was soll berechnet werden?: "))
print("\n")

if get_choice == 'ci':
  cm2inch(get_cm)

elif get_choice == 'ic':
  inch2cm(get_inch)

elif get_choice == 'km':
  kmh2mph(get_kmh)

elif get_choice == 'mk':
  mph2kmh(get_mph)
  
else:
  to_end()

## E-o-F
