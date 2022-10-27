fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit + " Pie")

# "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, saute it. There's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, shrimp burger, shrimp sandwich. That- that's about it."

it = ["barbeque", "boil", "broil", "bake", "saute"]
shrimp_dash = ["-kababs", "creole", "gumbo"]
fried = ["pan", "deep", "stir-"]
fruit = ["pineapple", "lemon", "coconut", "pepper"]
dish = ["soup", "stew", "salad", "and potatoes", "burger", "sandwich" ]


# for number in range(1, 10):
#   print(number) #prints 1-9

# for number in range(1, 11):
#   print(number) # 1-10

# for number in range(1, 11, 2):
#   print(number) #increments by 2

total = 0
for number in range(1, 101):
  total += number
print(total)

even_total = 0
for number in range(2, 101, 2):
  even_total += number

print(even_total)

odd_total = 0
for number in range(1, 100, 2):
  odd_total += number

print(odd_total)