# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total = 0
length = 0

for height in student_heights:
  total += height
  length += 1

print(round(total / length))


# 156 178 165 171 187