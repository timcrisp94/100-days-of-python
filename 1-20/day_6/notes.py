def hal(str):
    print("Good morning, " + str)

hal("Dave")

def tab():
    print("we indent four spaces in python")

python = True
count = 1

while python and count == 1:
  tab()
  count -= 1

# reeborgs maze solution
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if right_is_clear() and front_is_clear():
#         move()
#     elif right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear(): 
#         move()            
#     else:
#         turn_left()