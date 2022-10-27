import random
import my_module

print(my_module.pi)

random_int = random.randint(1, 10)
print(random_int)

# 0.00 - 0.9999
random_float = random.random()
print(random_float)

# for a number between 0 and 5
random_float * 5 # 0.00 - 4.99999

love_score = random.randint(1, 100)
print(f"your love score is {love_score}")

# import modules
# learn random module functions for integers and floats