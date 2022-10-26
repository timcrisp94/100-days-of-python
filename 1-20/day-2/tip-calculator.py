#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

welcome = "Welcome to the tip calculator."
print(welcome)

bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 18, 20, or 25?\n"))
people = int(input("How many people split the bill?\n"))

total = tip / 100 * bill + bill
each_pays = round(total/people, 2)

message = f"Each person should pay: ${each_pays}"
print(message)