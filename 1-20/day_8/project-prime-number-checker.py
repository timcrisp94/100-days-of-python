#Write your code below this line 👇

def prime_checker(number):
  if number <= 2:
    print("it's a prime number")
  else:  
    if not number % 2 == 0:
      print("it's a prime number")
    else:
      print("it's not a prime number")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


# their code
# * just taking a moment to appreciate my own growth
# * the recursive solution i wrote came very simply, 
# * did not have to think too hard to know it was good and efficient


def checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number")
  else:
    print("It's not a prime number")
