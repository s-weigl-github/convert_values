################################
###   compute the temp of °C K °F
###   S.Weigl - 01.09.2016
###   ver. 1.2 - german version
###   python version 3.2.5
################################

fahr = None  # Grad Fahrenheit °F
cels = None  # Grad Celsius °C
kelv = None  # Kelvin K

## -- compute definitions -- ##
def to_celsius(fahr):
  #
  fahr = input("gib die Temperatur in °F an: ")
  fahr = float(fahr.replace(',', '.'))
  #
  ans = (fahr-32)/1.8000
  ans = round(ans, 3)
  print("  -- in °C =", ans)
##

def to_fahrenheit(cels):
  #
  cels = input("gib die Temperatur in °C an: ")
  cels = float(cels.replace(',', '.'))
  #
  ans = (cels*1.8000)+32
  ans = round(ans, 3)
  print("  -- in °F =", ans)
##
  
def to_kelvin(kelv):
  #
  choice = input("für °C gib 'c' oder 'f' für °F ein: ")
  if choice == 'c':
    #
    kelv = input("gib die Temperatur in °C an: ")
    kelv = float(kelv.replace(',', '.'))
    #
    if kelv > 0:
      #
      ans = (273.15)+(kelv)
      ans = round(ans, 3)
      print("kelvin ist =", ans)
    elif kelv < 0:
      #
      ans = (kelv)-(-273.15)
      ans = round(ans, 3)
      print("kelvin ist =", ans)
    else:
      print("falsche eingabe???")
  elif choice == 'f':
    #
    kelv = input("gib die Temperatur in °F an: ")
    kelv = float(kelv.replace(',', '.'))
    #
    if kelv > 0:
      #
      ans = ((kelv-32)/1.8000)+273.15
      ans = round(ans, 3)
      print("kelvin ist =", ans)
    elif kelv < 0:
      #
      ans = ((kelv-32)/1.8000)+273.15
      ans = round(ans, 3)
      print("kelvin ist =", ans)
    else:
      print("falsche eingabe???")
  else:
    print("bitte nur c oder f eingeben")
    print("Done!!!")
    #
##

def from_kelvin(kelv):
  #
  choice = input("für °C gib 'c' oder 'f' für °F ein: ")
  if choice == 'c':
    #
    kelv = input("gib die Temperatur in Kelvin an: ")
    kelv = float(kelv.replace(',', '.'))
    #
    ans = (kelv)-(273.15)
    ans = round(ans, 3)
    print("°C ist =", ans)
  #
  if choice == 'f':
    #
    kelv = input("gib die Temperatur in Kelvin an: ")
    kelv = float(kelv.replace(',', '.'))
    #
    ans = (kelv)-(273.15)
    ans = (ans*1.8000)+32
    ans = round(ans, 3)
    print("°F ist =", ans)
  #
##

## E-o-F
