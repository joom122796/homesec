import keypad
import leave
from leave import leaving as leaving

def setup():
  if keypad.password == '0000':
    pw2 = int(input('It seems to be your first time using the home security system.\nEnter a four digit passcode to set as your security code: '))
    pwconf = int(input('Re-enter the four digit passcode to confirm your security code: '))
    while pwconf != pw2:
      pwconf = int(input('Invalid entry!\nRe-enter to confirm your four digit security code: '))
    else:
        print('Your passcode has updated.')
        keypad.password = pwconf
        leaving()
  else: 
    pw = int(input('There currently is a passcode set to lock/unlock the home security system. Would you like to reset your password? \nEnter 1 for Yes and enter 2 for No \nEnter:  '))
    if pw == 1:
      reset = int(input('Enter the current passcode to reset your security code: '))
      while reset != keypad.password:
        reset = int(input('Invalid password!\nEnter four digit passcode to reset your security code: '))
      else:
        pw2 = int(input('Enter a four digit passcode to set as your security code: '))
        pwconf = int(input('Re-enter to confirm your four digit security code: '))
        while pwconf != pw2:
          pwconf = int(input('Invalid entry!\nRe-enter to confirm your four digit security code: '))
        else:
          print('Your passcode has updated.')
          keypad.password = pwconf
          leaving()
    else:
      leaving()
