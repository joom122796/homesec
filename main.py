import secsys
from secsys import SecSys as Security
import keypad
import leave

pw = int(input('Is there a passcode set to lock/unlock the home security system\nEnter 1 for Yes and enter 2 for No \nEnter:  '))

if pw == 2:
  pw2 = int(input('Enter a four digit passcode to set as your security code: '))
  pwconf = int(input('Re-enter to confirm your four digit passcode: '))
  while pwconf != pw2:
    pwconf = int(input('Invalid entry!\nRe-enter to confirm your four digit passcode: '))
  else:
    print('Your passcode has updated.')
    keypad.password = pwconf
    leave.leaving()
else:
  leave.leaving()
