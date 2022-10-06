import keypad.keypad as keypad

def SecSyst():
  Alarm = False
  SecuritySystem = True
  while SecuritySystem == True:
    movementGround = int(input('Is there movement on the ground?\nEnter 1 for Yes and enter 2 for No\nEnter: '))
    movementUpper = int(input('Is there movement on the second floor?\nEnter 1 for Yes and enter 2 for No\nEnter: '))
    if movementGround == 1:
      tries = 0
      while tries < 5:
        fhome = int(input('Enter keypad to disable alarm system: '))
        if fhome != keypad:
          tries = tries + 1
          total = 5 - tries
          print(f'Incorrect keypad entry. You have {total} tries left')
        else: 
          print('Family is home, disabling security system.')
          SecuritySystem = False
      else:
        print('Movement on the ground detected: enabling intrusion detection system')
        Alarm = True
        if Alarm == True:
          print('*Alarm noise*')
        print('Sent notification to home owners device ')
    else:
        print('System idle... ')

    if movementUpper == 1:
      print('Movement on the second floor detected: enabling intrusion detection system')
      Alarm = True
      if Alarm == True:
        print('*Alarm noise*')
      print('Sent notification to home owners device ')
    else:
      print('System idle... ')
  else:
    print('System idle...')

fleave = int(input('Is the family leaving the house?\nEnter 1 for Yes and enter 2 for No \nEnter:  '))
if fleave == 1:
  SecSyst()
else:
  print('Security system remains disabled.\nSystem idle...')
