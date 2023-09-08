def isLeapYear(year):
  if(year%4==0):
    return True
  else:
    return False
year=int(input("Enter the year:"))
if isLeapYear(year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year.'.format(year))