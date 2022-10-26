print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number. 

# For Love Scores **less than 10** or **greater than 90**, the message should be:
# `"Your score is **x**, you go together like coke and mentos."` 
# For Love Scores **between 40** and **50**, the message should be:
# `"Your score is **y**, you are alright together."`

combined_string = name1.lower() + name2.lower()

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
true = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
  print(f"Your love score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together")
else:
  print(f"Your score is {love_score}...hot")