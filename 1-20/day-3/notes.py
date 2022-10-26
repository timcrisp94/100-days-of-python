print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
price = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7")
  elif age >= 45 and age <= 55:
    print("Eveything's going to be okay. Have a free ride on us")
  else:
    bill = 12
    print("Adult tickets are $12")

  wants_photo = input("Do you want a photo taken? Y or N  ")
  if wants_photo == "Y" or wants_photo == "y":
    bill += 3

  print(f"Total will be {bill}")
else:
  print("Sorry, you have to grow taller before you can ride")
