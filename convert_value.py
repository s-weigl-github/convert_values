#########################
### convert length and speeds
### S.Weigl - 01.09.2016
### ver. 1.2 - german version
### python version 3.2.5 and 3.6.0a1
#########################

from convert_speeds import *
from convert_length import *
from convert_thermo import *


print("Mit diesem kleinen Programm kannst Du Werte umrechnen\n")

print("um cm in inch umzurechnen gib 'ci' ein")
print("um inch in cm umzurechnen gib 'ic' ein\n\n")

print("um km/h in mp/h umzurechnen gib 'km' ein")
print("um mp/h in km/h umzurechnen gib 'mk' ein\n\n")

print("Um °C in °F umzurechnen gib 'cf' ein")
print("Um °F in °C umzurechnen gib 'fc' ein\n\n")

print("Um °C oder °F in Kelvin umzurechnen gib 'tk' ein")
print("um Kelvin in °C oder °F umzurechnen gib 'fk' ein\n\n")

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

elif get_choice == 'cf':
  to_fahrenheit(cels)

elif get_choice == 'fc':
  to_celsius(fahr)

elif get_choice == 'tk':
  to_kelvin(kelv)

elif get_choice == 'fk':
  from_kelvin(kelv)

else:
  to_end()

## E-o-F
