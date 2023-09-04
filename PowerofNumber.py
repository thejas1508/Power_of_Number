  Base_Number = int(input("Enter a Base Number:"))
  Exponent = int(input("Enter the Power of the Number:"))
  Storage = Base_Number
  Extra = Exponent
  while(Exponent>1):
      Storage = Storage*Base_Number
      Exponent = Exponent-1
  print("The Base of",Base_Number,"to Power of",Extra,"is",Storage)



