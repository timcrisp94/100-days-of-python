################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2 
#   print(f"enemies inside function: {enemies}") # 2

# increase_enemies()
# print(f"enemies outside function: {enemies}") # 1

# Local scope - exists in functions
# def drink_potion():
#   strength = 2
#   print(strength)

# drink_potion()
# # print(strength) -> err name 'strength' is not defined

# Global scope
health = 10

# def drink_potion():
#   strength = 2
#   print(health)

# drink_potion() # 10

def game():
  def drink_potion():
    strength = 2
    print(health)

  drink_potion() # 10

game()

# There is no block scope

level = 3
enemies = ["skeleton", "zombie"]

if level < 5:
  new_enemy = enemies[0]

print(new_enemy) # skeleton

# # (Avoid) Modifying Global Scope
# enemies = 1

# def increase_enemies():
#   print(f"enemies inside function: {enemies}") # 2
#   return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}") # 1

# Global Constants
# all upper
PI = 3.1415
TWITTER_HANDLE = "@betteryet"

