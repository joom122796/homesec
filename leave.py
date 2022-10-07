import secsys
from secsys import SecSys as Security
def leaving():
  fleave = int(input('Is the family leaving the house?\nEnter 1 for Yes and enter 2 for No \nEnter:  '))
  if fleave == 1:
    Security()
  else:
    print('Security system remains disabled.\nSystem idle...')
