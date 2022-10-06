import keypad

Alarm = False

def AlarmSys():
  Alarm = True
  if Alarm == True:
    print('*Alarm noise*')
    print('Sent notification to home owners device ')
    print('System lockdown')
    quit()
  else:
    print('System idle...')

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
        AlarmSys()
    else:
      print('System idle... ')
    movementUpper = int(input('Is there movement on the second floor?\nEnter 1 for Yes and enter 2 for No\nEnter: '))
    if movementUpper == 1:
      print('Movement on the second floor detected: enabling intrusion detection system')
      AlarmSys()
    else:
      print('System idle... ')
  else:
    print('System idle...')

fleave = int(input('Is the family leaving the house?\nEnter 1 for Yes and enter 2 for No \nEnter:  '))
if fleave == 1:
  SecSys()
else:
  print('Security system remains disabled.\nSystem idle...')
