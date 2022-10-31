# dictionaries
# key, value pairs
# {Key: Value}

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  
}

# retrieve item from dictionary
print(programming_dictionary["Bug"])

# add new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# create an empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
# # good for clearing scores, etc
# programming_dictionary = {}

# loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key]) # value
  # # # ^^ retrieval code ^^