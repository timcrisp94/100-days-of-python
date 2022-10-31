from art import logo
from os import system, name

# import sleep to show output for some time period
from time import sleep

# clear function
def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

bidders = {}

print(logo)
print("Welcome to the silent auction program.")

name = input("What is your name? ")
print("SILENCE! This is a SILENT auction!")
sleep(1)

bid = int(input(f"Just kidding {name}, what is your bid? $"))
bidders[name] = bid

bidding_over = False
while not bidding_over:
  others = input("Are there any other bidders? Type 'yes' or 'no' ")
  if others == "yes":
    clear()
    new_name = input("What is your name? ")
    new_bid = int(input("What is your bid? "))
    bidders[new_name] = new_bid
  else:
    bidding_over = True

high_bid = 0
for key in bidders:
  if int(bidders[key]) > high_bid:
    high_bid = bidders[key]
    highest_bidder = key

print(f"The winning bidder is {highest_bidder}")
  















