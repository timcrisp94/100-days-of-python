print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
name = input("what is your name?\n")

left_or_right = input(f"You're at a crossroads, {name}. Do you wish you go left or right?\nL or R? ")

if left_or_right == "L":
  swim_or_wait = input(f"There is a lake and an island. Do you wish to wait for a boat or swim across the lake?\nS or W? ")
  if swim_or_wait == "W":
    which_door = int(input(f"You make it to a house on the island. There is a house with 3 doors, which one do you pick?\n1, 2, or 3 "))
    if which_door == 2:
      print(f"You found the treasure! Way to go {name}")
    else:
      print(f"the door exploded and you're super dead now {name}")
  else:
    print(f"You shoulda waited {name} cuz you're super dead now")
else:
  print(f"You're dead, {name}")

