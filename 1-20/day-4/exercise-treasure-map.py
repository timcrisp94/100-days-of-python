# You are going to write a program which will mark a spot with an X.

# In the starting code, you will find a variable called ```map```.

# This ```map``` contains a nested list.
# When ```map``` is printed this is what the nested list looks like:
# ```
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
# ```
# In the starting code, we have used new lines (```\n```) to format the three rows into a square, like this:
# ```
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ```
# This is to try and simulate the coordinates on a real map. 

# First your program must take the user input and convert it to a usable format. 
# Next, you need to use it to update your nested list with an "x". 
# # Example Input 1

# column 2, row 3 would be entered as:

# ```
# 23
# ```

# # Example Output 1

# ```
# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', 'X', '⬜️']
# ```

# # Example Input 2

# column 3, row 1 would be entered as:

# ```
# 31
# ```

# # Example Output 2

# ```
# ['⬜️', '⬜️', 'X']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']
# ```


# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

row = int(position[0]) - 1
col = int(position[1]) - 1

map[col][row] = "X "
print(f"{row1}\n{row2}\n{row3}")
