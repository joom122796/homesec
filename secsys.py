import alarmsys
from alarmsys import AlarmSys as Alarm
import keypad

def SecSys():
  SecuritySystem = True
  while SecuritySystem == True:
    movementGround = int(input('Is there movement on the ground?\nEnter 1 for Yes and enter 2 for No\nEnter: '))
    if movementGround == 1:
      fhome = int(input('Enter passcode to disable alarm system: '))
      if fhome == keypad.password:
        SecuritySystem = False
        print('Family is home, disabling security system.')
      else:
        print('Movement on the ground detected: enabling intrusion detection system')
        Alarm()
    else:
      print('System idle... ')
    movementUpper = int(input('Is there movement on the second floor?\nEnter 1 for Yes and enter 2 for No\nEnter: '))
    if movementUpper == 1:
      print('Movement on the second floor detected: enabling intrusion detection system')
      Alarm()
    else:
      print('System idle... ')
  else:
    print('System idle...')
