#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:

password = ""

for letter in range(0, nr_letters):
  password += letters[random.randint(0, len(letters) - 1)]

for symbol in range(1, nr_symbols + 1):
  password += symbols[random.randint(0, len(symbols) - 1)]

for number in range(1, nr_numbers + 1):
  password += numbers[random.randint(0, len(numbers) - 1)]

print("Here is your password: " + ''.join(random.sample(password, len(password))))

# alt method

alt_pw = []
for char in range(1, nr_letters + 1):
  alt_pw.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
  alt_pw.append(random.choice(symbols))
for num in range(1, nr_numbers + 1):
  alt_pw.append(random.choice(numbers))

random.shuffle(alt_pw)
alt_pw_shuffled = ""

for char in alt_pw:
  alt_pw_shuffled += char

print(f"Your alt password is {alt_pw_shuffled}")