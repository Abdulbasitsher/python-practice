print("Welcome to printing lists")

heights_of_students = input("Enter the height_of students ").split()

for n in range(0,len(heights_of_students)):
    heights_of_students[n] = int(heights_of_students[n])
aver = 0
highest = 0
for n in heights_of_students:
    if heights_of_students[n] > heights_of_students[n+1]:
        highest = heights_of_students[n]
    elif heights_of_students[n] == heights_of_students[n+1]:
        highest = heights_of_students[n]
    else:
        highest = heights_of_students[n+1]
print(highest)
