def prime_checker(number):
  
  notPrime = False
  #if number ==  1 or number == 2 :
      #notPrime = False

  
  for dividor in range(2,number-1):
    if( (number%dividor)==0 ):
      notPrime = True


  if (notPrime == False):
    print(f"{number} is a prime ")
  else:
    print(f"this, {number} is not a prime")    

n = int(input("Check this number: "))
prime_checker(number=n)



